from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.views.generic import View

from cars.models import Make,Cars
from cars.forms import CarsForm,MakeForm
# Create your views here.

class MainView(View):
    def get(self, request):
        make_list = Make.objects.all().count()
        car_list = Cars.objects.all()

        context = {'ml':make_list,'cl':car_list}
        return render(request,'cars/car_list.html',context)

class MakeListView(ListView):
    model = Make
    context_object_name = 'make_list'
    template_name = 'cars/make_list.html'

class MakeCreateView(CreateView):
    model = Make
    fields ='__all__'
    success_url = reverse_lazy('make_list')

class MakeUpdateView(UpdateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy('make_list')

class MakeDeleteView(DeleteView):
    model = Make
    success_url = reverse_lazy('make_list')


class CarsUpdateView(UpdateView):
    model = Cars
    fields = '__all__'
    success_url = reverse_lazy('index')

class CarsCreateView(CreateView):
    model = Cars
    fields = '__all__'
    success_url = reverse_lazy('index')

class CarsDeleteView(DeleteView):
    model = Cars
    success_url = reverse_lazy('index')
