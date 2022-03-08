# redirect: 작업이 끝나는 시점에 특정 url로 돌아갈 수 있도록 함
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm


def home(request):
  # 블로그 글을 모두 출력하는 작업
  # posts = Blog.objects.all()  # Blog객체에 입력된 개체를 DB로 부터 모두 출력
  posts = Blog.objects.filter().order_by('-date')  # 날짜를 기준으로 정렬해서 개체 출력(내림차순)
  return render(request, 'index.html', {'posts': posts})

# 블로그 글 작성: html을 보여주는 함수
def new(request):
    return render(request, 'new.html')


# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == "POST"):
        post = Blog()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.date = timezone.now()
        post.save()     # model.save()를 통해 모델 객체를 데이터베이스에 저장할 수 있다.
    return redirect('home')

# django form을 이용해서 입력값을 받는 함수
# GET 요청  (= 입력값을 받을 수 있는 html을 가져다 줌)
# POST 요청 (= 입력한 내용을 DB에 저장. form에서 입력된 내용을 처리)
# 둘 다 처리가 가능한 함수(그러면 html form은 안되는가?)


def formcreate(request):
    # Django는 하나의 url에서 GET요청과 POST요청을 모두 처리할 수 있다
    if(request.method == 'POST'):
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        # 입력값의 유효성 검사를 위해 .is_valid() 메서드를 사용
        if form.is_valid():
          post = Blog()
          # form으로 입력된 값 중 검증된 깨끗한 값 의미
          post.title = form.cleaned_data['title']
          post.content = form.cleaned_data['content']
          post.save()
          return redirect('home')
    else:
      # 입력을 받을 수 있는 html을 가져다 줌
      form = BlogForm()  # 객체를 가져옴
    # 세 번째 인자에서는 views.py 내의 데이터를 html에 넘겨줄 수 있도록한다. 단,  Dictionary 자료형으로 넘겨줘야 한다.
    # form이라는 이름으로 html에 넘겨줄 수 있는데 form은 BlogForm의 객체를 가져온 변수 form이다.
    return render(request, 'formcreate.html', {'form': form})


def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          return redirect('home')
    else:
      form = BlogModelForm()
    return render(request, 'formcreate.html', {'form': form})

def detail(request, blog_id):
  # get_objecct_or_404()를 사용해서 pk값을 이용해 특정 모델 객체 하나만 가지고 올 수 있다.
  # blog_id 번째 블로그 글을 DB로부터 가지고 와서
  blog_detail = get_object_or_404(Blog, pk=blog_id)
  
  comment_form = CommentForm()

  # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
  return render(request, 'detail.html', {'blog_detail': blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
  filled_form = CommentForm(request.POST)

  if filled_form.is_valid():
    finished_form = filled_form.save(commit=False) # 저장하지않고 대기
    finished_form.post = get_object_or_404(Blog, pk=blog_id)
    finished_form.save()
  
  return redirect('detail', blog_id) # blog_id가 동일한 detail로 복귀