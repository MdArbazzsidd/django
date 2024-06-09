# your_app_name/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('order/', views.order, name='order'),
    path('order/<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_store/', views.chai_store_view, name='chai_stores'),
]
