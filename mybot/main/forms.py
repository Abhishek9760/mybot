from django import forms

class BotChatForm(forms.Form):
    box = forms.CharField(label='Ask Me', max_length=100)
