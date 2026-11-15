"""
URL configuration for evaluacion3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from mascotas.views import listar_responsables

"""
URL configuration for u2_proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from mascotas.views import crear_mascota,modificar_mascota,eliminar_mascota,listar_mascota,listar_mascotas,listar_responsable,listar_responsables,eliminar_responsable,modificar_responsable,crear_responsable

urlpatterns = [
    #Responsables
    path('admin/', admin.site.urls),
    path('responsable/crear', crear_responsable),
    path('responsable/modificar/<int:id>', modificar_responsable),
    path('responsable/eliminar/<int:id>', eliminar_responsable),
    path('responsables', listar_responsables),
    path('responsable/<int:id>', listar_responsable),

    #Mascotas
    path('mascota/crear', crear_mascota),
    path('mascota/modificar/<int:id>', modificar_mascota),
    path('mascota/eliminar/<int:id>', eliminar_mascota),
    path('mascotas', listar_mascotas),
    path('mascota/<int:id>', listar_mascota)
]
