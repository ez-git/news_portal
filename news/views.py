from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.order_by('-created_at')
    context = {'news': news,
               'title': 'News list'}


    return render(request, 'news/index.html', context)
    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    # return HttpResponse(res)

def test(request):
    # print(dir(request))
    return HttpResponse('<H1>Test page</H1>')