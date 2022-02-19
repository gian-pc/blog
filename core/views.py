from django.http import Http404
from django.shortcuts import render
from .models import Persona, Skills, Post
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    template_name = 'index.html'
    # Este objeto almacenará toda la información de la persona
    persona = Persona.objects.get(id=1)
    # Este objeto almacenará sus SKILLS o HABILIDADES
    # 100 objetos
    skills = Skills.objects.all()
    # Dividimos los objetos de 3 en 3
    paginator = Paginator(skills,3)
    # Devolver el número de página en el que me encuentro
    page_number = request.GET.get('page')
    # Y devolver los objetos de esa página
    skills = paginator.get_page(page_number)
    context = {
        'per': persona, 'ski': skills
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'about.html'
    # Este objeto almacenará toda la información de la persona
    persona = Persona.objects.get(id=1)
    context = {
        'per': persona
    }
    return render(request, template_name, context)


def post(request):
    template_name = 'post.html'
    persona = Persona.objects.get(id=1)
    post = Post.objects.all()
    context = {
        'per': persona, 'pos': post
    }
    return render(request, template_name, context)


def skill_detail(request, cod):
    template_name = 'skill_detail.html'
    persona = Persona.objects.get(id=1)
    try:
        skilldetail = Skills.objects.get(codigo=cod)
    except Skills.DoesNotExist:
        raise Http404("Skill No Existe")
    context = {
        'per': persona, 'ski': skilldetail
    }
    return render(request, template_name, context)


def skill_search(request):
    template_name = 'index.html'
    q = request.GET["q"]
    # Cuando deseamos mostrar varias coincidencias de busqueda usamos FILTER
    skills = Skills.objects.filter(estado=True, skill__icontains=q)
    # select * from skills where skill like '%q%'
    persona = Persona.objects.get(id=1)

    context = {
        'per': persona, 'ski': skills
    }
    return render(request, template_name, context)


def test(request):
    template_name = 'test.html'
    return render(request, template_name)
