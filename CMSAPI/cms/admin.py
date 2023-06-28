from django.contrib import admin
from .models import Post,Like
# Register your models here.

@admin.register((Post))
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description','content','creation_date','owner']

@admin.register((Like))
class LikeModelAdmin(admin.ModelAdmin):
    list_display=['id','post','user']