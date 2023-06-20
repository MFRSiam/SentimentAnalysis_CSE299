from django import forms


class Data(forms.Form):
    sentence = forms.CharField(label="Sentiment", max_length=100)