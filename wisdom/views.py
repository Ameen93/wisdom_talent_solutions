from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>You made it to Wisdom</h1>")