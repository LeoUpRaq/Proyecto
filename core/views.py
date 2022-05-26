from django.views.generic import View
from django.shortcuts import render

from blog.models import Eventos

class HomeView(View):
    def get(self,request,*args, **kwargs):
        event = Eventos.objects.all()
        context={
                'event':event
        }
        return render(request,'index.html',context)