from django.shortcuts import render, get_object_or_404, redirect
from .models import Kist
import datetime
# Create your views here.
def index(request):    
    arr = Kist.objects
    return render(request, 'index.html', {'arr':arr})

def new(request):
    return render(request, 'new.html')

def create(request):
    #빈 오브젝트 생성 -> 오브젝트 값 채움 -> 오브젝트 저장
    ob = Kist()   
    ob.title = request.GET['title']   
    ob.product = request.GET['product']  
    ob.category = request.GET['category']  
    ob.save()
    return redirect('/')

def detail(request, id):
    ob = get_object_or_404(Kist, pk=id)
    return render(request, 'detail.html', {'x':ob})    

def update(request, id):
    ob = get_object_or_404(Kist, pk=id)
    return render(request, 'update.html', {'x':ob})

def updat(request, id):
    ob = get_object_or_404(Kist, pk=id)
    ob.title = request.GET['title']    
    ob.product = request.GET['product']
    ob.category = request.GET['category']    
    ob.date = datetime.datetime.now()
    ob.save()
    return redirect('/'+str(id))

def delete(request, id):
    ob = get_object_or_404(Kist, pk=id)
    ob.delete()
    return redirect('/')