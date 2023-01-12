from django.db import models

# Create your models here.

from django.db import models
class Post(models.Model):
# 데이터베이스의 필드(컬럼): 최대 길이가 30
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)    

# author는 추후 작성

    def __str__(self):
        return f'[{self.pk}]_{self.title}' #[번호] 제목

    # pk: 기본키로 레코드에 대한 고유한 값(중복 허용 안됨) 
    # 포스트의 번호를 primary key로 지정
