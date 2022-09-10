import django_filters
from django import forms
from .models import *


class Filtro_Status(django_filters.FilterSet):
    status = django_filters.ModelMultipleChoiceFilter(queryset=Documento.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Documento
        fields = ["estado"]