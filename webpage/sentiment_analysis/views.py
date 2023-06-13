from django.shortcuts import render, HttpResponse

# Create your views here.


def HomePageView(request):
    broadcaster = "This Will Be broadcasted"
    status = {
        'var' : broadcaster
    }
    return render(request,'index.html', context=status)


def AboutsPageView(request):
    
    return render(request,'abouts.html')