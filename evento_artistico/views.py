
from django.shortcuts import render
from django.db.models import Q
from evento_artistico.models import Productores, Musicos, Tecnicos
from evento_artistico.forms import productoresform, musicosform, tecnicosform


def index(request):
    return render(request, "evento_artistico/index.html")

def productores(request):
    productores = Productores.objects.all()

    context_dict = {
        'productores': productores
    }

    return render(
        request=request,
        context=context_dict,
        template_name="evento_artistico/productores.html"
    )
def productor_form(request):
    if request.method == 'POST':
        productor_form = productoresform(request.POST)
        if productor_form.is_valid():
            data = productor_form.cleaned_data
            productor = Productores(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email'],
                cuil=data['cuil'],
            )
            productor.save()

            productor = Productores.objects.all()
            context_dict = {
                'productores': productores
            }
            return render(
                request=request,
                context=context_dict,
                template_name="evento_artistico/productores.html"
            )
    productor_form = productoresform(request.POST)
    context_dict = { 'productor_form': productor_form}
    return render(request=request, context=context_dict, template_name='evento_artistico/productoresform.html')   
   

def musicos(request):
    musicos = Musicos.objects.all()

    context_dict = {
        'musicos': musicos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="evento_artistico/musicos.html"
    )


def musicos_form(request):
    if request.method == 'POST':
        musico_form = musicosform(request.POST)
        if musico_form.is_valid():
            data = musico_form.cleaned_data
            musico = Musicos(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email'],
                instrumento=data['instrumento'],
                cuil=data['cuil'],
            )
            musico.save()

            musico = Musicos.objects.all()
            context_dict = {
                'musicos': musicos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="evento_artistico/musicos.html"
            )
    musico_form = musicosform(request.POST)
    context_dict = { 'musico_form': musico_form}
    return render(request=request, context=context_dict, template_name='evento_artistico/musicosform.html')    

def tecnicos(request):
    tecnicos = Tecnicos.objects.all()

    context_dict = {
        'tecnicos': tecnicos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="evento_artistico/tecnicos.html"
    )


def tecnicos_form(request):
    if request.method == 'POST':
        tecnico_form = tecnicosform(request.POST)
        if tecnico_form.is_valid():
            data = tecnico_form.cleaned_data
            tecnico = Tecnicos(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email'],
                cuil=data['cuil'],
            )
            tecnico.save()

            tecnico = Tecnicos.objects.all()
            context_dict = {
                'tecnico': tecnico
            }
            return render(
                request=request,
                context=context_dict,
                template_name="evento_artistico/tecnicos.html"
            )
    tecnico_form = tecnicosform(request.POST)
    context_dict = { 'tecnico_form': tecnico_form}
    return render(request=request, context=context_dict, template_name='evento_artistico/tecnicosform.html')

def search(request):
    context_dict = dict()
    if request.GET.get('nombre'):
        search_param = request.GET.get('nombre')
        musicos = Musicos.objects.filter(nombre__contains=search_param)
        context_dict = {
            'musicos': musicos
        }
    elif request.GET.get('cuil'):
        search_param = request.GET.get('cuil')
        musicos = Musicos.objects.filter(cuil__contains=search_param)
        context_dict = {
            'musicos': musicos
        }
    elif request.GET.get('all_search'):
        search_param = request.GET.get('all_search')
        query = Q(nombre__contains=search_param)
        query.add(Q(cuil__contains=search_param), Q.OR)
        musicos = Musicos.objects.filter(query)
        context_dict = {
            'musicos': musicos
        }

    return render(
        request=request,
        context=context_dict,
        template_name="evento_artistico/search.html",
    )