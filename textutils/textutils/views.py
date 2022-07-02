# Made by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    exspaceremover = request.POST.get('exspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-{}[];:'"\\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
    if exspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                continue
            else:
                analyzed += char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcount == "on":
        count = 0
        for char in djtext:
            if char != ' ' and char != '\n':
                count += 1
        params = {'purpose': 'Total no. of Characters', 'analyzed_text': count}

    if removepunc == fullcaps == newlineremover == exspaceremover == charcount == "off":
        return HttpResponse('<h2>Please select atleast one operation and try again!!!</h2>')
    return render(request, 'analyze.html', params)
