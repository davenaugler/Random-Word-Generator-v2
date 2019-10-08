from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'word' not in request.session:
        request.session['count'] = 0
        # random = RandomWords()
    return render(request, 'rw_app/index.html')

def random_word(request):
    request.session['count'] += 1
    print(request.session['count'])
    request.session['word'] = get_random_string(length=14)
    print(request.session['word'])
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')


