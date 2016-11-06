from django.shortcuts import render_to_response
from principal2.models import usuario

# Create your views here.

def lista_usuarios(request):
	usuarios = usuario.objects.all()
	return render_to_response('lista_usuarios.html',{'lista':usuarios})
