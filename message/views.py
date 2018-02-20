from django.shortcuts import render, redirect
from .forms import SendForm
from .models import Send

# Create your views here.

response = {}
def index(request):
    sends = Send.objects.all()
    response['sends'] = sends
    response['SendForm'] = SendForm
    return render(request, 'index.html', response)

def send_new(request):
    if request.method == "POST":
        form = SendForm(request.POST or None)
        if form.is_valid():
            response['sender'] = request.POST['sender']
            response['receiver'] = request.POST['receiver']
            response['text'] = request.POST['text']
            send = Send(sender=response['sender'],receiver=response['receiver'],text=response['text'])
            send.save()
            return redirect('index')
    else:
        return redirect('index')
