from Profileapp import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib.auth  import views as auth_views
from main.views import *
from main.views import  CreateBlog 
urlpatterns=[
    #home
    path('createblog/<int:pk>',CreateBlog,name='CreateBlog'),
    path("register/",RegisterView.as_view(),name="register"),
    path('',HomePageView.as_view(),name='home'),
    path('accounts',include('django.contrib.auth.urls')),
    path('accounts/login',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('accounts/logout',auth_views.LogoutView.as_view(),name='logout'),
    path('accounts/password_change',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),name='password_change'),
    path('updateprofile/<int:pk>',ProfileUpdateView.as_view(),name='editprofile'),
    path('updateBlog/<int:pk>',BlogUpdateView.as_view(),name='editblog'),
    path('DeleteBlog/<int:pk>',DeleteBlogView.as_view(),name='deleteblog'),
    path('myblogs/<int:pk>',Myblogs,name='Myblogs'),
    path('comment/<int:pk>',comment,name='comment'),
    path('reply/<int:pk>',reply,name='reply')
 

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)