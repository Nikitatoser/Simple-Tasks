from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from notes import views
from users import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("notes/", include("notes.urls")),
    path('users/', include('users.urls')),
    path(
        'users/login/',
        auth_views.LoginView.as_view(template_name='users/registration/login.html'),  # Шлях до шаблону
        name='login'
    ),
    path('users/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/signup/', views.register_view, name='signup'),
    path('', views.home, name="home")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)