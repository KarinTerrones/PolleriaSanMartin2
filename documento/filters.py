import django_filters
from django import forms
from .models import *
from django_filters import  DateFilter


class Filtro_Status(django_filters.FilterSet):
    status = django_filters.ModelMultipleChoiceFilter(queryset=Documento.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Documento
        fields = ["estado"]

class Fecha_tipo(django_filters.FilterSet):
    start_date = DateFilter(field_name="data_created",lookup_expr='gte',label="Fecha Inicio")
    end_date = DateFilter(field_name="data_created",lookup_expr='lte',label="Fecha Fin")

    class Meta:
        model = Documento
        fields = ['id',"tipo"]