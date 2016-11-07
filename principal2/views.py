from django.http import HttpResponse 
from django.template import loader, Context
from principal2.models import usuario

# Create your views here.

def lista_usuarios(request):
	usuarios = usuario.objects.all()
	mi_template = loader.get_template("lista_usuarios.html")
	mi_contexto = Context({"usuarios":usuarios})
	return HttpResponse(mi_template(mi_contexto))

	#return render_to_response('lista_usuarios.html',{'lista':usuario})
