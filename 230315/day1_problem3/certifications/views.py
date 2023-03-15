from django.shortcuts import render

# Create your views here.
def certifications1(request):
    age = range(25, 31)
    grade = ['a', 'b', 'c', 's']
    name = 'kim happy'

    context = {
        'name' : name,
        'age' : age,
        'grade' : grade,
    }


    return render(request, 'certifications/certifications1.html', context)

def certifications2(request):
    age = range(25, 31)
    grade = ['a', 'b', 'c', 's']
    name = 'park happy'

    context = {
        'name' : name,
        'age' : age,
        'grade' : grade,
    }

    return render(request, 'certifications/certifications2.html', context)

def certifications3(request):
    age = range(25, 31)
    grade = ['a', 'b', 'c', 's']
    name = 'lee happy'

    context = {
        'name' : name,
        'age' : age,
        'grade' : grade,
    }

    return render(request, 'certifications/certifications3.html', context)