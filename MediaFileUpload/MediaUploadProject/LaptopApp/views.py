from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from .models import Laptop
from django.views import View




class AddLaptopView(View):
    def get(self,request):
        form = LaptopModelForm()
        template_name = 'LaptopApp/addlaptop.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form = LaptopModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
        template_name = 'LaptopApp/addlaptop.html'
        context = {'form': form}
        return render(request,template_name,context)

class ShowLaptop(View):
    def get(self,request):
        laptop_list = Laptop.objects.all()
        template_name = 'LaptopApp/showlaptop.html'
        context = {'laptop_list': laptop_list}
        return render(request, template_name, context)

class LaptopUpdate(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(instance=laptop)
        template_name = 'LaptopApp/addlaptop.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request,i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
        template_name = 'LaptopApp/addlaptop.html'
        context = {'form': form}
        return render(request, template_name, context)

class LaptopDelete(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        template_name = 'LaptopApp/confirm_delete.html'
        context = {'laptop': laptop }
        return render(request, template_name, context)
    def post(self,request,i):
        laptop = Laptop.objects.get(id=i)
        laptop.delete()
        return redirect("show_laptop")

class LaptopDetails(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        template_name = 'LaptopApp/laptop_detail.html'
        context = {'laptop': laptop}
        return render(request, template_name, context)