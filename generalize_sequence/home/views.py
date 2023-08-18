from django.shortcuts import render

def index(request):
    a = 5
    b = 10
    c = a + b
    context = {
        'a': a,
        'b': b,
        'c': c,
        'list': [1, 2, 3, 4, 5],
    }
    return render(request, 'index.html', context)
