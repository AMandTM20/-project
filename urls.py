from django.contrib import admin
from django.urls import path
from calculator.views import dish_view

urlpatterns = [
     path('admin/', admin.site.urls),
     path('<dish>/', dish_view, name='dish')
]



