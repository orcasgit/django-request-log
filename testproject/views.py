from django.http import HttpResponse


def create_requestlog(request):
    return HttpResponse('OK')
