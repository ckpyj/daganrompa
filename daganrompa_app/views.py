from django.shortcuts import render, redirect


def test(request):
    return render(request, 'daganrompa/test.html')


def list_game(request):
    return render(request, 'daganrompa/test.html')


def wiki(request):
    return redirect("https://docs.google.com/document/d/1HKJUJCgOofZynKb-y5Yq-g8YD5d3z2uN0Rw58kz4EEU/edit")


def forms(request):
    return render(request, 'daganrompa/test.html')
