from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import BotChatForm
import apiai, codecs, json


def apiai_integration(CLIENT_ACCESS_TOKEN, message):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'de' #Default : English
    msgText = message
    request.query = msgText
    response = request.getresponse()
    reader = codecs.getdecoder("utf-8")
    obj = json.load(response)
    reply = obj['result']['fulfillment']['speech']
    return reply

def bot_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BotChatForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            reply = apiai_integration('b23b241d2c2d4a96a15757a596b66435', form.cleaned_data['box'])
            return render(request, 'reply.html', {'reply':reply})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BotChatForm()

    return render(request, 'index.html', {'form': form})
