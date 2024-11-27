from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from kisite.forms import ContactForm
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
def about(request):
    return render(
        request,
        'about.html'
    )
def contacts(request):
    context={}
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form=ContactForm()
    context['form']=form
    return render(
        request,
        'contacts.html',
        context=context
    )
def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['ala-zaa@yandex.ru'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()