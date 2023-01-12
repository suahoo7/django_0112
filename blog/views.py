from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'blog/index.html') #아직 blog에는 index.html이 없음
    #'blog/index.html'를 화면에 보여줌
