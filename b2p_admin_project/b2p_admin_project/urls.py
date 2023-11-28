"""b2p_admin_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from main import views as main_views
from users import views as users_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_views.home, name="main-home"),
    path("login/", users_views.login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name='users/logout.htm'), name="logout"),
    path("project_lists/", main_views.project_lists, name="main-project_lists"),
    path("project_lists_add/", main_views.project_lists_add, name="main-project_lists_add")
    
]
