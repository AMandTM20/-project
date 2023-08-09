from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('index/', views.index, name='index'),
     path('pasta/', views.pasta, name='pasta'),
     path('omlet/', views.omlet, name='omlet'),
     path('buter/', views.buter, name='buter'),
]



