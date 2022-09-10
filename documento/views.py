from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from documento.models import *
from documento.forms import *
from django.contrib import messages
from .filters import *


def home(request):
	context = {}
	return render(request,'documentos/dashboard.html',context)


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


def Historial_doc(request):
	documentos=Documento.objects.all()
	stat_filtro= Filtro_Status(request.GET,queryset=documentos)
	documentos=stat_filtro.qs
	context = {'documentos':documentos,'filtro':stat_filtro}
	return render (request,'documentos/historial.html',context)


def Confi_Perfil(request):
	perfil = EncargadoArea.objects.all()
	perfil_form = PerfilEncargado()
	if request.method == 'POST':
		perfil_form = PerfilEncargado(request.POST, request.FILES, instance=perfil)
		if perfil_form.is_valid():
			perfil_form.save()
	context = {'perfil_form':perfil_form}
	return render (request, 'documentos/perfil.html',context)	
