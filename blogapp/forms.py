from dataclasses import field
from django import forms
from .models import Blog, Comment  # models Form을 사용할 때만 사용

# Django Form


class BlogForm(forms.Form):
    # 입력받고자 하는 값들
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)

# Model Form


class BlogModelForm(forms.ModelForm):
    class Meta:
        # 어떤 모델을 기반으로 Form을 생성할지 지정
        model = Blog
        # 어떤 필드를 입력받을지 지정
        fields = '__all__'    # 모두 지정
        # fields = ['title', 'content']  # 특정 필드 지정. list형태로 저장


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']