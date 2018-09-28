from django.shortcuts import render, HttpResponse


def base(request):
    return render(request, 'sitepages/index.html')


def wedding(request):
    return render(request, 'sitepages/wedding.html')


def corporate(request):
    return render(request, 'sitepages/corporate.html')


def couple(request):
    return render(request, 'sitepages/couple.html')


def baby(request):
    return render(request, 'sitepages/baby.html')


def fashion(request):
    return render(request, 'sitepages/fashion.html')


def party(request):
    return render(request, 'sitepages/party.html')
