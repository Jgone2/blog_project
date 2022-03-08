from tkinter import CASCADE
from django.db import models

# Create your models here.
class Blog(models.Model):
  # Primary_Key를 따로 지정하지 않으면 django에서 자동으로 Id값ㅇ르 생성한다.
  title = models.CharField(max_length=200)
  content = models.TextField()
  photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # 공란이나 Null값 가능, 업로드 시 MEDIA_ROOT경로 하위의 blog_photo라는 폴더 생성 후 저장
  date = models.DateTimeField(auto_now_add=True)


  def __str__(self):
   return self.title

class Comment(models.Model):
  comment = models.CharField(max_length=200)
  date = models.DateField(auto_now_add=True)
  # 댓글이 어떤 게시물에 달려있는지 알 수 있는 참조데이터가 필요
  post = models.ForeignKey(Blog, on_delete=models.CASCADE) # Blog라는 객체를 참조하는 참조키이며, Blog에 종속적이다
  # 댓글이 참조하고 있는 글이 삭제될 시, 종속되어 있는 Comment도 삭제된다.

  def __str__(self):
    return self.comment