from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hello")
    # params = {'name': 'sam', 'age': 24}
    return render(request, 'index.html')

def analyze(request):
    # Analyze the text 
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowcaps = request.POST.get('lowcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        
    
    if(lowcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Changed to Lowercase', 'analyzed_text': analyzed}
        djtext = analyzed
        

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces between Text', 'analyzed_text': analyzed}
    
    if(removepunc != "on" and fullcaps != "on" and lowcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error, Please select any operation")


    return render(request, 'analyze.html', params)
