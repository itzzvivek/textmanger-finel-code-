#created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def ex1(request):
    sites = ['''<h1>For Entertainment</h1><a href = "https://www.youtube.com">youtube video</a>''',
             '''<h1>For Interaction</h1><a href = "https://www.facebook.com">Facebook</a>''',
             '''<h1>For Insight </h1><a href = "https://www.ted.com/talks">Ted Talk</a>''',
             '''<h1>For Intership </h1><a href = "https://internshala.com">Inrtenship</a>''',
           ]
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed



    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed


    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        if(removepunc != "on" and newlineremover != "on" and fullcaps != "on" and fullcaps != "on"):
            return HttpResponse("Error")



    return render(request, 'analyze.html', params)




