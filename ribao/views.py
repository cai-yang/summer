from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from ribao.models import Article, Daily
from ribao.serializers import ArticleSerializer, DailySerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, renderers, viewsets
#from backend.permissions import *


# Create your views here.
def homepage(request):
    return render_to_response('index.html')


def article(request,num='1'):
    a = Article.objects.get(pk=num)
    return render_to_response('a.html',{'a':a})

def dailyhomepage(request,page='1'):
    CURRENT_URL = request.path
    PREVIOUS_URL = CURRENT_URL.replace(page,str(int(page)-1))
    NEXT_URL = CURRENT_URL.replace(page,str(int(page)+1))
    page = int(page)
    DAILY_LIST=[]
    ARTICLE_LIST=[[],[],[],[]]
    for d_num in range(page * 4 - 3, page * 4 + 1):
        if not page==1:
            index = (d_num) % (page * 4 - 3)
        if page==1:
            index = d_num - 1
        try:
            DAILY_LIST.append(Daily.objects.get(pk=d_num))
        except:
            break
        ARTICLE_LIST[index] = Article.objects.filter(daily=Daily.objects.get(pk=d_num))
        #for a_num in ARTICLE_NUM_LIST[index]:
        #    ARTICLE_LIST[index].append(Article.objects.get(pk=a_num))

    return render_to_response('dhome.html',{'d_num':d_num,'PREVIOUS_URL':PREVIOUS_URL, 'NEXT_URL':NEXT_URL, 'page':page, 'DAILY_LIST':DAILY_LIST, 'ARTICLE_LIST':ARTICLE_LIST})

def daily(request,num='1'):
    d = Daily.objects.get(pk=num)
    #ARTICLE_NUM_LIST = [d.article_num1,d.article_num2,d.article_num3,d.article_num4,d.article_num5]
    ARTICLE_LIST = Article.objects.filter(daily=d)
    return render_to_response('d.html',{'d':d, 'ARTICLE_LIST':ARTICLE_LIST})

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = DailySerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
