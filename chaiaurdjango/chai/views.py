from django.shortcuts import render, get_object_or_404
from .models import chaiverity

def all_chai(request):
    return render(request, 'chai/all_chai.html')

def order(request):
    chais = chaiverity.objects.all()
    return render(request, 'chai/order.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiverity, pk=chai_id)
    return render(request, 'chai/details.html', {'chai': chai})
