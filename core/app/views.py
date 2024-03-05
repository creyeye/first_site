from django.shortcuts import HttpResponse
from .models import Shishka

def shishka_list(request):
    shishki = Shishka.objects.all()
    return HttpResponse(shishki)

def shishka_detail(request, id):
    shishki = Shishka.objects.get(id=id)

    content = {
        'title': shishki.title,
        'description': shishki.description,
        'price': shishki.price,
        'strength': shishki.strength,
        'sort': shishki.sort,
    }
    return HttpResponse(content.items())