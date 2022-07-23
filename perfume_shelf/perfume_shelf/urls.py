from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'auth/login',
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'auth/logout',
        views.LogoutView.as_view(next_page='/'),
        name='logout'
    ),
    path('', include('perfumes.urls', namespace='perfumes')),
]
