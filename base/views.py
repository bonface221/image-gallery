from unicodedata import category
from django.shortcuts import render
from . models import Location,Category,Images
from django.db.models import Q

# Create your views here.

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    images = Images.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)|
        Q(location__name__icontains=q)
        )

    categories=Category.objects.all()
    locations=Location.objects.all()
    # images = Images.get_all_images()
    context=dict(images=images,categories=categories,locations=locations)
    return render (request ,'base/home.html',context)

def categories(request,pk):
    images= Images.objects.filter(category__id=pk)
    category= Category.objects.get(id=pk)
    categories=Category.objects.all()
    locations=Location.objects.all()
    context=dict(images=images ,category=category,categories=categories,locations=locations)

    return render(request,'base/category.html',context)


def locations(request,pk):
    images= Images.objects.filter(location__id=pk)
    location=Location.objects.get(id=pk)
    locations=Location.objects.all()
    categories=Category.objects.all()
    context=dict(images=images,location=location,locations=locations,categories=categories)

    return render(request,'base/location.html' ,context)

def single(request,pk):
    image=Images.objects.get(id=pk)
    locations=Location.objects.all()
    categories=Category.objects.all()
    context=dict(image=image,locations=locations,categories=categories)

    return render(request,'base/img_details.html' ,context)
