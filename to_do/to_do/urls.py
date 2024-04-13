"""
URL configuration for to_do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",user_views.index,name='index'),
    path("register/",user_views.register,name="register"),
    path('login/', user_views.custom_login_view, name='login'),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("profile/",user_views.profile,name="profile"),
    path("update/",user_views.profile_update,name="profile_update"),
    path('verify_email/<str:token>/', user_views.verify_email, name='verify_email'),
    path("resend_verification_email/",user_views.resend_verification_email,name="resend_verification_email"),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name="password_reset"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="users/reset.html"), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"), name="password_reset_complete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

