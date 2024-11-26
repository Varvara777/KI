from django.shortcuts import render

from kisite.models import Tovar


def index(request):
    tovar_do3 = Tovar.objects.filter(type__exact='DO3').order_by('?')[:6]
    tovar_do7 = Tovar.objects.filter(type__exact='GRLboy3_6').order_by('?')[:6]
    tovar_do13 = Tovar.objects.filter(type__exact='GRLboy7_13').order_by('?')[:6]
    context = {'tovar_do3': tovar_do3, 'tovar_do7': tovar_do7, 'tovar_do13': tovar_do13}
    return render(
        request,
        'index.html',
        context=context
    )
