from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.hello,name='home'),
    path('products',views.products,name='products'),
    path('add',views.add, name= 'add'),
    path('pdetails/<int:p_id>/',views.pdetails, name='pdetails'),
    path('update/<int:pdetails_id>/',views.update, name= 'update'),
    path('delete/<int:pdetails_id>/',views.delete, name= 'delete')
]
