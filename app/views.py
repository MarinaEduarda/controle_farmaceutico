from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class ProdutosView(View):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        return render(request, 'produtos.html', {'produtos': produtos})

class EstoquesView(View):
    def get (self, request, *args, **kwargs):
        estoques = Estoque.objects.all()
        return render(request, 'estoque.html', {'estoques': estoques})

class AnimaisView(View):
    def get (self, request, *args, **kwargs):
        animais = Animal.objects.all()
        return render(request, 'animal.html', {'animais': animais})

class SetoresView(View):
    def get (self, request, *args, **kwargs):
        setores = Setor.objects.all()
        return render(request, 'setor.html', {'setores': setores})

class UsuariosView(View):
    def get (self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios})
    
class SaidasView(View):
    def get (self, request, *args, **kwargs):
        saidas = Saida.objects.all()
        return render(request, 'saidas.html', {'saidas': saidas})

class DetalhesView(View):
    def get (self, request, *args, **kwargs):
        detalhes = Detalhes.objects.all()
        return render(request, 'detalhes.html', {'detalhes': detalhes})
