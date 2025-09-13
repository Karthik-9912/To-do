from django.urls import path
from . import views

urlpatterns=[
    path('',views.create,name='create'),
    path('display',views.display,name='display'),
    path('single/<int:pk>',views.single,name='single'),
    path('edit/<int:vk>',views.edit,name='update'),
    path('delete/<int:dl>',views.delete,name='delete'),
]