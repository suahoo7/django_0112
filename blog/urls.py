from django.urls import path
from . import views
urlpatterns = [
    path('',views.index) #URL이 ‘blog/’로 끝나면, views.py의 index() 함수 실행
]