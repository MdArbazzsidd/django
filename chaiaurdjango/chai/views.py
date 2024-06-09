from django.shortcuts import render, get_object_or_404
from .models import chaiverity,store
from .forms import chaiverityForm

def all_chai(request):
    return render(request, 'chai/all_chai.html')

def order(request):
    chais = chaiverity.objects.all()
    return render(request, 'chai/order.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiverity, pk=chai_id)
    return render(request, 'chai/details.html', {'chai': chai})

def chai_store_view(request):
    stores=None
    if request.method == 'POST':
        form=chaiverityForm(request.POST)
        if form.is_valid():
            chai_varity=form.cleaned_data['chai_varity']
            stores=store.objects.filter(chai_varaities=chai_varity)
    else:
        form=chaiverityForm()

    return render(request,'chai/chai_store.html',{'store':stores , 'form':form})
