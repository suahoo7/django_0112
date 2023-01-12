from django.shortcuts import render
#import 해야함
from .models import Post

# Create your views here.

def index(request):

    posts= Post.objects.all().order_by('-pk') 
    #클래스 Post => models.py에서 정의했었음
    #-pk: 내림차순 (없으면 오름차순)

    return render(request,'blog/index.html',
    {'posts':posts}
    ) 
    #아직 blog에는 index.html이 없음
    #'blog/index.html'를 화면에 보여줌


    #Post 내의 객체: title, content, update_at
    #쿼리 요청 방법
# – 모델명.objects.all()
# Ø 모든 데이터를 가져옴
# – 모델명.objects.filter(조건)
# Ø 특정 데이터를 필터링해서 가져옴
# – 모델명.objects.exclude(조건)
# Ø 조건에 해당되지 않는 데이터


def single_post_page(request, value):
    post= Post.objects.get(pk=value)

    return render(
        request,
        'blog/single_post_page.html',
        {'post': post,}
    )