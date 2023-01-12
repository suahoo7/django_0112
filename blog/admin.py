from django.contrib import admin

from .models import Post #admin.py와 같은 폴더에 models.py가 존재하므로 .models 사용

# Register your models here.

admin.site.register(Post)