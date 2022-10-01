import io
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from requests import RequestException
from documento.models import *
from documento.forms import *
from django.contrib import messages
from .filters import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allow_users,admin_only
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



@login_required(login_url='login')
def home(request):
	context = {}
	return render(request,'documentos/dashboard.html',context)
@login_required(login_url='login')
def userpage(request):
	context = {}
	return render (request,'documentos/user.html',context)

@login_required(login_url='login')
def Registro_Encargado(request):
	r_form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			messages.success(request,'Cuenta creada exitosamente: ' + email)
			return redirect ('home')

	context= {'r_form':r_form}
	return render(request,'documentos/registrar.html',context)

def Pagina_Login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email= email, password= password)

		if user is not None:
			login(request, user)
			return redirect ('home')
		else:
			messages.info(request, "Correo o contraseña invalida")
	context={}
	return render (request, 'documentos/login.html', context)


def logoutPage(request):
	logout(request)
	return redirect ('login')

@login_required(login_url='login')
@allow_users(allowed_roles=['a_encargado'])
def Registro_doc(request):
	doc_form = DocumentoForm
	if request.method == 'POST':
		doc_form = DocumentoForm(request.POST)
		if doc_form.is_valid():
			doc_form.save()
			messages.success(request,'El pedido fue grabado exitosamente')
			return redirect ('home')
	context = {'doc_form':doc_form}
	return render(request,'documentos/registro.html',context)

@login_required(login_url='login')
@allow_users(allowed_roles=['a_encargado'])
def Historial_doc(request):
	documentos=Documento.objects.all()
	stat_filtro= Filtro_Status(request.GET,queryset=documentos)
	documentos=stat_filtro.qs
	context = {'documentos':documentos,'filtro':stat_filtro}
	return render (request,'documentos/historial.html',context)

@login_required(login_url='login')
@allow_users(allowed_roles=['a_encargado'])
def Confi_Perfil(request):
	encargado = request.user.encargadoarea
	perfil_form = PerfilEncargado(instance=encargado)
	if request.method == 'POST':
		perfil_form = PerfilEncargado(request.POST, request.FILES, instance=encargado)
		if perfil_form.is_valid():
			perfil_form.save()
	context = {'perfil_form':perfil_form}
	return render (request, 'documentos/perfil.html',context)	

def solicitudes_admin(request):
	solic = Documento.objects.all()
	fech_filtro = Fecha_tipo(request.GET, queryset=solic)
	solic = fech_filtro.qs 
	context = {'solic': solic,'filtro':fech_filtro}
	return render (request, 'documentos/solicitudes.html',context)

def info_encargado_are(request):
	area = Area.objects.all()
	context = {'area':area}
	return render ( request, 'documentos/empleados.html',context)

def generar_pdf(request):
		buf = io.BytesIO()
		c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
		textob = c.beginText()
		textob.setTextOrigin(inch, inch)
		textob.setFont('Helvetica',14)

		documentos = Documento.objects.all()
		lines = []
		

		for documento in documentos:
			lines.append(documento.nombre)
			lines.append(documento.tipo)
			lines.append(documento.estado)
			lines.append(documento.proveedor.razon_social)
			lines.append(documento.encargado.nombre)
			lines.append(documento.pedido)
			lines.append("")

		for line in lines:
			textob.textLine(line)

		c.drawText(textob)
		c.showPage()
		c.save()
		buf.seek(0)
		return FileResponse(buf, as_attachment=True,filename="Pedido.pdf")