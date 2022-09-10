from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from documento.models import *

class AccAdmin(UserAdmin):
    list_display = ('id','email','username','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class EncargadoAreaAdmin(admin.ModelAdmin):
    list_display =('email','nombre','apellido_pater','celular')

class AreaAdmin(admin.ModelAdmin):
    list_display =('nombre','encargado')    

class AdministradorAdmin(admin.ModelAdmin):
    list_display =('email','nombre','apellido_pater','celular')

class ProveedorAdmin(admin.ModelAdmin):
    list_display =('razon_social','contacto','categoria')

class DocumentoAdmin(admin.ModelAdmin):
    list_display =('id','nombre','tipo','estado','proveedor','encargado')

admin.site.register(EncargadoArea,EncargadoAreaAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Administrador,AdministradorAdmin)
admin.site.register(Categoria)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Documento,DocumentoAdmin)
admin.site.register(Account,AccAdmin)