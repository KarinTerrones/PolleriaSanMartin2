from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo")
        if not username:
            raise ValueError("El ususario debe tener un Username")

        my_user = self.model(
            email=self.normalize_email(email),
            username=username)

        my_user.set_password(password)
        my_user.save(using=self._db)
        return my_user

    def create_superuser(self, email, username, password):
        my_user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username
                )
        my_user.is_admin = True
        my_user.is_staff = True
        my_user.is_superuser = True
        my_user.save(using=self._db)
        return my_user

class Account(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(verbose_name="email", max_length=60, unique=True)
    username=models.CharField(max_length=30, unique=True)
    date_joined=models.DateTimeField(verbose_name='data joined', auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    
    objects= MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True

class EncargadoArea(models.Model):
    email = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True, max_length=30)
    nombre =models.CharField(null=True,max_length=30)
    apellido_pater= models.CharField(null=True,max_length=30)
    apellido_mater= models.CharField(null=True,max_length=30)
    celular = models.CharField(null=True,max_length=9)
    foto_perfil=models.ImageField(null=True,blank=True)
    data_created=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre+""+self.apellido_pater

class Area(models.Model):
       nombre = models.CharField(null=True,max_length=20)
       encargado = models.OneToOneField(EncargadoArea,on_delete=models.CASCADE,null=True)

class Administrador(models.Model):
    email = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True, max_length=30)
    nombre =models.CharField(null=True,max_length=30)
    apellido_pater= models.CharField(null=True,max_length=30)
    apellido_mater= models.CharField(null=True,max_length=30)
    celular = models.CharField(null=True,max_length=9)
    foto_perfil=models.ImageField(null=True,blank=True)
    data_created=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.nombre+""+self.apellido_pater

class Categoria(models.Model):
    categoria = models.CharField(null=True,max_length=30)
    def __str__(self):
        return self.categoria

class Proveedor(models.Model):
    razon_social = models.CharField(null=True,max_length=30)
    contacto = models.CharField(null=True,max_length=9)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    foto_perfil=models.ImageField(null=True,blank=True)
    data_created=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.razon_social

class Documento(models.Model):
    opciones = (('opcion1','opcion1'),
                ('opcion2','opcion2'),
                ('opcion3','opcion3'),
                ('opcion4','opcion4'))

    estado = (('Evaluando','Evaluando'),
                ('Aprobado','Aprobado'),
                ('Rechazado','Rechazado'),
                ('Observado','Observado'))
    nombre = models.CharField(null=True,max_length=30)
    tipo = models.CharField(choices=opciones, null=True,max_length=20)
    estado = models.CharField(default="Evaluando",choices=estado, null=True,max_length=20)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True)
    encargado = models.ForeignKey(EncargadoArea,on_delete=models.CASCADE,null=True)
    pedido = models.CharField(null=True,max_length=300)
    data_created=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.estado