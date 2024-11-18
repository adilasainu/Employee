from django.shortcuts import render
from app1.models import Emp1
# Create your views here.
def home(request):
    return render(request,'home.html')

def addemployee(request):
    if(request.method=="POST"):
        i=request.POST['i']
        n=request.POST['n']
        a=request.POST['a']
        p=request.POST['p']
        e=request.POST['e']
        z=request.FILES['z']
        f=request.FILES['f']
        e=Emp1.objects.create(id=i,name=n,age=a,place=p,email=e,profile=z,pdf=f)
        e.save()
        return home(request)
    return render(request,'addemployee.html')

def viewemployee(request):
    k=Emp1.objects.all()
    context={'emp':k}
    return render(request,'viewemployee.html',context)

def detail(request,p):
    k=Emp1.objects.get(id=p)
    return render(request,'detail.html',{'emp':k})


def edit(request,p):
    k=Emp1.objects.get(id=p)
    if(request.method=="POST"):
      k.id=request.POST['i']
      k.name=request.POST['n']
      k.age=request.POST['a']
      k.place=request.POST['p']
      k.email=request.POST['e']

      if(request.FILES.get('z')==None):
          k.save()
      else:
          k.profile=request.FILES['z']

    if (request.FILES.get('f')==None):
        k.save()
    else:
        k.pdf=request.FILES['f']
        k.save()

    return viewemployee(request)

    return render(request,'edit.html',{'emp':k})

def delete(request,p):
    k=Emp1.objects.get(id=p)
    k.delete()
    return viewemployee(request)


