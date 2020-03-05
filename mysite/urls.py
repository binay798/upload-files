from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('',views.index,name='index'),
    path('photos/',views.files,name='files'),
]