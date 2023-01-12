from django.urls import path
from . import views
urlpatterns = [
    path('<int:value>/', views.single_post_page),
    
    #– <int:value>:	정수값을 받으면, 해당 값을 value 변수에 저장해서 views.single_post_page()로 전송

    path('',views.index) #URL이 ‘blog/’로 끝나면, views.py의 index() 함수 실행
]