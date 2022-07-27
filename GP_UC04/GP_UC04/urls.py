"""GP_UC04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('inicio/', views.index, name = "inicio"),
    path('saludo/', views.saludo, name = "saludo"),
    path('crear-estudiante/<str:codigo>/<str:dni>/<str:nombre>/<str:apepat>/<str:apemat>/<str:direccion>/<str:estado>/',views.crear_estudiante,name="crear_estudiante"),
    path('buscar-estudiante', views.buscar_estudiante, name="buscar_estudiante"),
    path('listar-estudiantes/',views.listar_estudiantes,name="listar_estudiantes"),
    path('eliminar-estudiante/<int:id>',views.eliminar_estudiante, name='eliminar_estudiante'),
    path('save-estudiante/',views.save_estudiante, name='save_estudiante'),
    path('create-estudiante/',views.create_estudiante, name='create_estudiante'),

]