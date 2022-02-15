
from django.urls import path

from . import views, apps

app_name = 'dailyphoto'


urlpatterns = [

    path('', views.index, name = "index"),
    path('detail/<int:id>/', views.detail, name="detail"), # <int:post_id>/   <- 상세보기 주소
    path('upload/', views.post_create, name="post_create"),
    path('profile/<str:username>/', views.profile, name="profile"),

    path('modify/', views.modify_profile, name="modify_profile"),
    path('<int:user_id>/follow/', views.follow, name = 'follow'),
    path('like/',views.like, name='like'),
    path('unlike/',views.unlike, name='unlike'),
    path('show_like/<int:post_id>',views.show_like,name='show_like'),
  
  # COMMENT
    
    path('<int:post_id>/comment_create' , views.comment_create, name="comment_create"),
    


]
