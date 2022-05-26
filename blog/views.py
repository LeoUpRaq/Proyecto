from django.shortcuts import render,get_object_or_404
from django.views.generic import View

from blog.models import Hotel,Eventos

# Create your views here.

class BlogListView(View):
    def get(self,request,*args, **kwargs):
        posts = Hotel.objects.all()

        context={
            'posts':posts
        }
        return render (request, 'blog_list.html' ,context)


class HomeI(View):
    def get(self,request,*args, **kwargs):
        context={

        }
        return render (request, 'index.html',context)

class BlogDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Hotel, pk=pk)
        context={
            'post':post
        }
        return render(request, 'blog_detail.html', context)


class BlogListViewEven(View):
    def get(self,request,*args, **kwargs):
        posts = Eventos.objects.all()

        context={
            'posts':posts
        }
        return render (request, 'index.html' ,context)
