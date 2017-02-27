from django.shortcuts import redirect, render


def index(request):
    return render(request, 'common/index.html')
