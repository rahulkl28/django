from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hello")
    # params = {'name': 'sam', 'age': 24}
    return render(request, 'index.html')

def analyze(request):
    # Analyze the text 
    djtext = request.GET.get('text', 'default')
    remove = request.GET.get('removepunc', 'off')
    print(remove)
    print(djtext)
    return HttpResponse("Remove punc")

