from django.shortcuts import render, redirect
from .forms import ServiceForm, CarByuForm


def register(request):
    error = ''
    if request.method == 'POST':
        form = CarByuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = CarByuForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'homepage/testdrive.html', data)


def action(request):
    error = ''
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = ServiceForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'homepage/action.html', data)


def reg(request):
    error = ''
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = ServiceForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'homepage/reg.html', data)


def buy_porsche(request):
    error = ''
    if request.method == 'POST':
        form = CarByuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = CarByuForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'homepage/buy_porsche.html', data)