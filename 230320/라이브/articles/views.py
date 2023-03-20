from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB에 새로운 Article저장
    # Article.objects.create(title=title, content=content)

    # 이 방법을 많이 쓴다(유효성 검사 때문에)
    article=Article(title=title, content=content)
    article.save()

    return redirect('articles:index')