"""django_project2 URL Configuration

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
from django.urls import path, include #blog 폴더의 url과 연결

urlpatterns = [
    path("admin/", admin.site.urls), #admin으로 접속
    path('blog/', include('blog.urls')) #blog 폴더의 url과 연결
] 
#• 웹 사이트 방문자가 여러 정보에 접근할 수 있도록 이정표의 역할을 수행
# • “127.0.0.1/admin/” 접속하면 관리자 페이지로 이동
# – urls.py에 정의되어 있음







