from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request.GET.get('msg1'))
    msg1 = request.GET.get('msg1')
    msg2 = request.GET.get('msg2')
    context = {
        'msg1' : msg1,
        'msg2' : msg2,
    }
    return render(request, 'articles/catch.html', context)