from django.shortcuts import render
from django.http import HttpResponse
from .models import groupe
# Create your views here.
def index(request):
    groupes = groupe.objects.all()
    # return HttpResponse("Bienvenue dans la page d'acceuil DJANGO")
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{groupes[0].name}</li>
            <li>{groupes[1].name}</li>
        </ul>
""")