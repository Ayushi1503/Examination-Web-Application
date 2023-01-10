from django.shortcuts import render
from examapp.models import Questions
from examapp.models import Answers

def showQuestions(request):
    all_que=Questions.objects.all()
    que_list={}
    mark=['first', 'second', 'third', 'fourth', 'fifth']
    index = 0
    for q in all_que:
        que_list[mark[index]]=q.que
        index+=1
    
    answers={}
    for key,value in request.GET.items():
        answers[key] = value
        a = Answers(ans_no=key, ans=value)
        a.save()
    print(answers)

    return render(request, "examapp/exam.html", que_list)

def showResult(request):
    result = calculate()
    context = {'result':result}
    return render(request,'examapp/showResult.html',context)


from django.shortcuts import render

# Calculate document distance given two files
# Uses cosine formula described on Wikipedia: https://en.wikipedia.org/wiki/Cosine_similarity

import math
import re
from collections import Counter

import nltk
from nltk.corpus import stopwords

# regular expression
# \w matches any alphanumeric character and the underscore
# + causes the RE to match 1 or more repetitions of the preceding RE
WORD = re.compile(r'\w+')
nltk.download("stopwords")
answer = {}

def textToVector(text):
    words = WORD.findall(text)
    # unordered collection where elements are stored as dict keys, and counts are stored as dict vals
    return Counter(words)

def cosDistance(vector1, vector2):
    # set of unordered collection of unique items
    intersection = set(vector1.keys()) & set(vector2.keys())  # return set with elements in intersection
    numerator = sum([vector1[x] * vector2[x] for x in intersection])

    sum1 = sum([vector1[x] ** 2 for x in vector1.keys()])
    sum2 = sum([vector2[x] ** 2 for x in vector2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def readFile(fileName):
    return open("examapp/" + fileName, 'r').read()

def calculate():
    pass
