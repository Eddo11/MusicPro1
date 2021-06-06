from django.shortcuts import redirect, render
from .models import Producto, Marca
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets
from .serializers import MarcaSerializer, ProductoSerializer 

# Create your views here.

class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre =self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        return productos

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos' : productos


    }

    return render(request, 'app/producto/listar.html', data)