from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('', views.home,name="home"),
   path('registro/',views.Registro_doc,name="registro"),
   path('historial/',views.Historial_doc,name="historial"),
   path('perfil/,',views.Confi_Perfil,name="perfil"),
   path('usuario/',views.userpage, name='user-page'),
   path('login/',views.Pagina_Login, name="login"),
   path('registrar/',views.Registro_Encargado,name="registrar"),
   path('logout',views.logoutPage,name='logout'),
   path('solicitudes/',views.solicitudes_admin,name='solicitudes'),
   path('empleados/',views.info_encargado_are,name="empleados"),
   path('generar_pedido',views.generar_pdf,name="generar_pedido"),
]