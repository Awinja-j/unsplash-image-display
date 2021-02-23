from django.urls import path
from . import views

urlpatterns = [
    path('get_photos', views.get_photos),
    path('tag_photo/<pk>', views.tag_photo, name='tag'),
    path('',views.index, name='index'),

]