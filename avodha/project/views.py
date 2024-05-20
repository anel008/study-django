from django.shortcuts import render,redirect
from .models import Product
from .form import Modeform

def hello(request):
    return render(request,"home.html")


def products(request):
    detail = Product.objects.all()
    return render(request,'product.html',{'details':detail})

def add(request):
    if request.method == 'POST' :
        name = request.POST['name']
        price = request.POST['price']
        disc = request.POST['disc']
        img = request.FILES['img']

        product = Product.objects.create(name = name , price = price, disc = disc,img = img)
        product.save()
        return redirect("/")
    else:
        return render(request,"product.html")
    
def pdetails(request,p_id):
    details = Product.objects.get(id=p_id)
    return render(request,'pdetails.html',{'pdetails':details})


def update(request,pdetails_id):
    obj = Product.objects.get(id=pdetails_id)
    form = Modeform(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return render(request,'home.html')
    return render(request,'update.html',{'form':form,'obj':obj})

def delete(request,pdetails_id):
    if request.method == 'POST':
        print("******  POST  *********")
        obj = Product.objects.get(id=pdetails_id)
        obj.delete()
        return redirect('/')
    print("*******  NOT EXICUTED **********")
    return render(request,'delete.html')


