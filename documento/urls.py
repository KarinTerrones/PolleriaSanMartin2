from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('', views.home,name="home"),
   path('registro/',views.Registro_doc,name="registro"),
   path('historial/',views.Historial_doc,name="historial"),
   path('perfil/,',views.Confi_Perfil,name="perfil")

]