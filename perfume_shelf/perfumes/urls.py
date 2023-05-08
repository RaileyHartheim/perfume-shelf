from django.urls import path

from . import views

app_name = 'perfumes'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.perfume_create, name='perfume_create'),
    path('perfume/<slug:slug>/comment/add/', views.comment_add,
         name='comment_add'),
    path('perfume/<slug:slug>/comment/<int:comment_id>/delete/',
         views.comment_delete, name='comment_delete'),
    path('perfume/<slug:slug>/edit',
         views.perfume_edit, name='perfume_edit'),
    path('perfume/<slug:slug>/delete/',
         views.perfume_delete, name='perfume_delete'),
    path('perfume/<slug:slug>/',
         views.perfume_detail, name='perfume_detail'),

]
