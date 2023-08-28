from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    analyze = ""

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        djtext = analyze
        analyze= ""
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': djtext}

    if fullcaps =="on":
        for char in djtext:
            analyze = analyze + char.upper()
        djtext = analyze
        analyze= ""
        params = {'purpose':'Change to Uppercase', 'analyzed_text': djtext}
    if newlineremover=="on":
        for char in djtext:
            if char !="\n":
                analyze=analyze+char
        djtext = analyze
        analyze= ""
        params = {'purpose': 'Removed NewLines', 'analyzed_text': djtext}
    if extraspaceremover=="on":
        index = 0
        for char in djtext:
            if char[index] != " " and char[index + 1] != " ":
                analyze = analyze + char
                if index < len(djtext):
                    index += 1
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyze}

    return render(request, 'analyze.html', params)

    
def removepunc(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse('remove punc')

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")