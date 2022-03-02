#I have created this file---Chetan
from itertools import count
import re
from django.http import HttpResponse    #Chetan---------  
from django.shortcuts import render
from pytest import param     #Chetannnn----


# def about(request):
#     return HttpResponse('''<h1>Hello Chetan Bhai</h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">
#     Click Me</a>''')    

def index(request):
   return render(request,'index.html')

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')

    #checkbox vale  
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    spaceremover=request.POST.get('spaceremover','off')
    countt=request.POST.get('countt','off')
    

    if removepunc=="on":
        punctucations=''':()-{},."<>^"\@?$*#&%'''
        analyzed=""
        for char in djtext:
            if char not in punctucations:
                analyzed=analyzed+char
        print(analyzed)            
        param={"purpose":"Remove Puncation","analyzed_text":analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',param)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        param={"purpose":"Change to uppercase","analyzed_text":analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',param)
            
    if spaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not( djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        param={"purpose":"Remove new lin","analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',param)
    
    if newline=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        param={"purpose":"Remove new lin","analyzed_text":analyzed}
        djtext=analyzed

    # if countt=="on":
    #     analyzed=0
    #     for i in djtext:
    #         if i!=" ":
    #             analyzed+=1
    #     param={"purpose":"Total Count","analyzed_text":analyzed}
    #     djtext=analyzed   

    if(removepunc!="on" and countt!="on" and newline!="on" and spaceremover!="on" and fullcaps!="on"):
        return  render(request,'Error.html')  
              
    return render(request,'analyze.html',param)        


