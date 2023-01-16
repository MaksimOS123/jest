from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.
def get_start_context():
    menu = [
        {'link': '/evolution', 'text': 'НАЧАЛО РАЗВИТИЯ'},
        {'link': '/cosmonauts', 'text': 'КОСМОНАВТЫ'},
        {'link': '/grades', 'text': 'ДОСТИЖЕНИЯ'},
        {'link': '/v', 'text': 'ПРОВЕРЬ СЕБЯ'},
    ]
    return {
        'menu': menu,
    }


def index_page(request):
    context = get_start_context()
    return render(request, 'index.html', context)


def planets(request):
    context = get_start_context()
    context['current'] = 'ПЛАНЕТЫ'
    return render(request, 'content.html', context)


def galactics(request):
    context = get_start_context()
    return render(request, 'galactics.html', context)


def stars(request):
    context = get_start_context()
    return render(request, 'grades.html', context)


def v(request):
    context = get_start_context()
    if request.method == "POST":
        first = request.POST.get("first")
        second = request.POST.get("second")
        third = request.POST.get("third")
        fourth = request.POST.get("fourth")
        fiveth = request.POST.get("fiveth")
        k = 0
        if first == '2':
            k+=1
        if second == '4':
            k+=1
        if third == '2':
            k+=1
        if fourth == '3':
            k+=1
        if fiveth == '2':
            k+=1

        context['answered'] = True
        context['res'] = str(k)+'/5'
        return render(request, "v.html", context)
    else:
        context['form'] = UserForm()
        context['answered'] = False
        return render(request, "v.html", context)