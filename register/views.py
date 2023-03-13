from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = RegisterForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'homepage/testdrive.html', data)


def action(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = RegisterForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'homepage/action.html', data)


def reg(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = RegisterForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'homepage/reg.html', data)


def buy_porsche(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = RegisterForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'homepage/buy_porsche.html', data)