from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def hello(request, name, age):
    print(name)
    # context = {
    #     'name': name,
    #     'age' : age
    # }
    person = {
        'name':name,
        'age':age
    }
    context = {
        'person' :person
    }
    return render(request, 'articles/hello.html', context)