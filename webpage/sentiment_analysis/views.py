from django.shortcuts import render, HttpResponse
from flair.data import Sentence
from flair.nn import Classifier
from .forms import Data
from .Trial import get_aspect_eval
from .models import History
# Create your views here.


def HomePageView(request):
    if request.method == 'GET':
        history = History.objects.all()
        form = Data()
        return render(request,'index.html',{'form':form,'history':history})
    else:
        form = Data(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['sentence']
            sentence = Sentence(subject)
            # load the NER tagger
            tagger = Classifier.load('sentiment')
            print(subject)
            # run NER over sentence
            tagger.predict(sentence)
            
            sentiment_value = sentence.labels[0].value
            junk,aspect = get_aspect_eval(subject)
            new_form = Data()
            
            new_history = History(sentence = subject , sentiment= sentiment_value, aspect = aspect )
            new_history.save()
            
            all_history = History.objects.all().order_by('-id')[:5]
            
            cont = {
                'sentiment': sentiment_value,
                'show' : True,
                'aspect': aspect,
                'form' : new_form,
                'history': all_history
            }
            
            return render(request,'index.html',context=cont)
        else:
            return HttpResponse("Shit didnt work")


def AboutsPageView(request):
    
    return render(request,'abouts.html')

def ContactUs(request):
    
    return render(request,'contact.html')