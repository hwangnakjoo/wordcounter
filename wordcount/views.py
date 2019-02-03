
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

""" 실습내용

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    count_dictionary = {}

    for word in words:
        if word in count_dictionary:
            #increase
            count_dictionary[word]+=1
        else:
            #add 
            count_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total':len(words), 'dictionary' : count_dictionary.items()})
    
"""

def result(request):
    text = request.GET['fulltext']
    words = len(text)

    none_space = 0

    for i in text:
        if i not in [" ", "\n"]:
            none_space += 1

    return render(request, 'result.html', {'full':text, 'total':words, 'none_space': none_space})