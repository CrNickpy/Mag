from django.shortcuts import render,get_object_or_404, HttpResponse,redirect
from .models import Stech,Otzyv,Client
from .forms import OtzyvForm,ClientForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


menu=[ {'title': "О нас", 'url_name': 'about'},
       {'title': "Оставить отзыв", 'url_name': 'otzyv'},
       {'title': "Отзывы", 'url_name': 'otzyvy'},
       {'title': "Обратный звонок", 'url_name': 'contact'},
]

def index(request):
    ec = Stech.objects.all()
    return render(request, 'main/index.html', {'menu': menu, 'ec':ec})


def about(request):
    return render(request, 'main/about.html',{'menu': menu})


def post_contact(request):
        if request.method == 'POST':
            con = ClientForm(request.POST)
            if con.is_valid():
                con.save()
                return redirect('postcont')
        else:

            con = ClientForm()
        return render(request, 'main/post_contact.html',{'menu':menu, 'con':con})


def otzyvy(request):
    otz = Otzyv.objects.all()
    return render(request, 'main/otzyvy.html', {'menu': menu, 'otz':otz})
    return render(request, 'main/contact.html',{'menu': menu})



def get_otz(request):
    if request.method == 'POST':
        pos = OtzyvForm(request.POST)
        if pos.is_valid():
            pos.save()
            return redirect('home')
    else:

        pos = OtzyvForm()
    return render(request, 'main/get_otz.html',{'menu':menu, 'pos':pos})


class Otzyvy(ListView):
    model = Otzyv
    template_name = 'main/otzyvy.html'
    context_object_name = 'otz'
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        return context
    

class AvtHome(ListView):
    model = Stech
    template_name = 'main/avt.html'
    context_object_name = 'ec'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        return context


class ExcHome(ListView):
    model = Stech
    template_name = 'main/exc.html'
    context_object_name = 'ec'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class SsvHome(ListView):
    model = Stech
    template_name = 'main/ssv.html'
    context_object_name = 'ec'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        return context
    

class PrHome(ListView):
    model = Stech
    template_name = 'main/pr.html'
    context_object_name = 'ec'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        return context
    

class ShowNumer(DetailView):
    model = Stech
    template_name = 'main/numer.html'
    pk_url_kwarg = 'numer_id'
    context_object_name = 'numer'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context['title']= context['numer']
        return context
    

def p_phone(request):
    return render(request,'main/p_phone.html',{'menu': menu})
    