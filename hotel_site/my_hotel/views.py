from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegistrationForm, UserLoginForm, ContactForm, EmailSupport
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from django.core.mail import send_mail


def preview(request):
    return render(request, 'my_hotel/index.html')


def show_hotels(request):
    rows = Hotels.objects.all()
    country = Country.objects.all()
    city = City.objects.all()
    tags = Tag.objects.all()
    name = Hotels.tags.through.objects.all()
    x = {
        'rows': rows,
        'countries': country,
        'cities': city,
        'tags': tags,
        'name': name}
    return render(request, 'my_hotel/test_filter.html', x)


def show_post(request, id):
    rows = Hotels.objects.filter(id=id)
    galery = Galery.objects.filter(hotel_id_id=id)
    tags = Hotels.tags.through.objects.filter(hotels_id=id)
    one_photo = (galery[0].photo)
    two_photo = (galery[1].photo)
    three_photo = (galery[2].photo)
    four_photo = (galery[3].photo)
    context = {
        'title': rows,
        'price_econom': rows,
        'price_standart': rows,
        'price_business': rows,
        'content': rows,
        'free_places': rows,
        'id_hotels': rows,
        'tags': tags,
        'photo': rows,
        'one_photo' : one_photo,
        'two_photo': two_photo,
        'three_photo': three_photo,
        'four_photo' : four_photo}
    return render(request, 'my_hotel/show_post.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            login(request, new_user)
            Users.objects.create(name_user=new_user.username,
                                 email_user=new_user.email)

            return render(request, 'my_hotel/index.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'my_hotel/auth/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(data=request.POST)
        if user_form.is_valid():
            new_user = user_form.get_user()
            login(request, new_user)
            return redirect('Home')

    else:
        user_form = UserLoginForm()
    return render(request, 'my_hotel/auth/login.html', {'user_form': user_form})


def bookinghotels(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            rows = Hotels.objects.filter(id=id)
            form = ContactForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                tickets = Ticket.objects.all
                data = {
                    'title': rows,
                    'price_econom': rows,
                    'price_standart': rows,
                    'price_business': rows,
                    'content': rows,
                    'photo': rows,
                    'free_places': rows,
                    'id_hotels': rows,
                    'form': form,
                    'name_user_ticket': tickets,
                    'id': tickets,
                }
                return render(request, 'my_hotel/baseblockpay.html', data)
        else:
            form = ContactForm(request.POST)
        return render(request, 'my_hotel/testforma.html', {'form': form})
    else:
        return redirect('Login')


def last(request, id1, id2):
    rows = Hotels.objects.filter(id=id1)
    forms = Ticket.objects.filter(id=id2)
    country = Country.objects.all()
    city = City.objects.all()
    context = {'title': rows,
               'price_econom': rows,
               'price_standart': rows,
               'price_business': rows,
               'content': rows,
               'photo': rows,
               'free_places': rows,
               'id_hotels': rows,
               'name_user_ticket': forms,
               'email_user_ticket': forms,
               'time_go': forms,
               'time_back': forms,
               'choose': forms,
               }
    return render(request, 'my_hotel/last.html', context)


def pdf(request, id1, id2):
    rows = Hotels.objects.filter(id=id1)
    forms = Ticket.objects.filter(id=id2)
    ticket = Ticket.objects.filter(id=id2)
    country = Country.objects.all()
    city = City.objects.all()
    template_path = 'my_hotel/ticket.html'
    context = {
        'title': rows,
        'id': ticket,
        'name_user_ticket': forms,
        'email_user_ticket': forms,
        'time_go': forms,
        'time_back': forms,
        'choose': forms,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="ticket.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def download(request, id1, id2):
    rows = Hotels.objects.filter(id=id1)
    forms = Ticket.objects.filter(id=id2)
    ticket = Ticket.objects.filter(id=id2)
    country = Country.objects.all()
    city = City.objects.all()
    template_path = 'my_hotel/ticket.html'
    context = {
        'title': rows,
        'id': ticket,
        'name_user_ticket': forms,
        'email_user_ticket': forms,
        'time_go': forms,
        'time_back': forms,
        'choose': forms,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def support(request, id1, id2):
    rows = Hotels.objects.filter(id=id1)
    forms = Ticket.objects.filter(id=id2)
    get_mail = []
    for row in forms:
        print(get_mail)
        print(row.email_user_ticket)
        get_mail.append(row.email_user_ticket)
        print(get_mail)
    if request.method == 'POST':
        form = EmailSupport(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject']+' (??????????????????????: '+get_mail[0]+')', form.cleaned_data['content'], 'companyvira@yandex.by', ['nikita.carasevitch@yandex.by'], fail_silently=False)
            if mail:
                messages.success(request, '???????????? ????????????????????!')
                return redirect('support.'+str(id1)+'.'+str(id2))
            else:
                messages.error(request, '???????????? ??????????????????????')
        else:
            messages.error(request, '???????????? ??????????????????????')
    else:
        form = EmailSupport()
    return render(request, 'my_hotel/support.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("Login")


def get_obejct_or_404(Hotels, pk):
    pass
