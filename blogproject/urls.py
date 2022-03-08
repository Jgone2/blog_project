from django.contrib import admin
from django.urls import path, include
import blogapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='home'),

    # html form을 이용해 블로그 객체 만들기
    path('new/', blogapp.views.new, name='new'),
    path('create/', blogapp.views.create, name='create'),

    # django form을 이용해 블로그 객체 만들기
    path('formcreate/', blogapp.views.formcreate, name='formcreate'),

    # django form을 이용해 블로그 객체 만들기
    path('modelformcreate/', blogapp.views.modelformcreate, name='modelformcreate'),

    # 127.0.0.1:8000/detail/1
    # 127.0.0.1:8000/detail/2
    # 127.0.0.1:8000/detail/3
    # detail/<자료형: 전송할 인자 값>
    path('detail/<int:blog_id>', blogapp.views.detail, name='detail'),

    path('create_comment/<int:blog_id>', blogapp.views.create_comment, name='create_comment'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     # 방법1
# media 파일에 접근할 수 있는 url도 추가해주어야 함
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # 방법2

