from django.shortcuts import render

from wisdom_talent_solutions import settings


def index(request):
    context = {}
    context['STATIC_URL']: settings.STATIC_URL

    return render(request, "wisdom/index.html", context)