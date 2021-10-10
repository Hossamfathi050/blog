  
from django.urls import path
from . import views
from blog.views import post_add

from django.conf.urls import url



app_name = 'blog'

urlpatterns = [
    path('' , views.PostList.as_view(),name='post_list'),
    path('ict' , views.post_add,name='ict'),

    path('<slug:slug>' ,views.PostDetail.as_view(),name='post_detail' ),

]