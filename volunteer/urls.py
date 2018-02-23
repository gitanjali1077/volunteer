"""volunteer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include, static
from django.contrib import admin
from register.views import signup,activate,index,login,admin_login
from blog.views import indexs ,detail ,add_post,post_update,post_delete
from django.conf.urls import include ,url
from django.conf import settings 
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', signup, name='signup'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin_login/$', admin_login, name='admin_login'),
    url(r'^application/$',indexs,name='indexs'),
    url(r'^application/(?P<oid>[0-9]+)/$',detail,name='detail'),
    url(r'^post_update/(?P<oid>[0-9]+)/$',post_update,name='post_update'),
    url(r'^post_delete/(?P<oid>[0-9]+)/$',post_delete,name='post_delete'),
   
    url(r'^add_post/$',add_post,name='add_post'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
        # for the inbuilt login view
      #url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
 url(r'^(?P<string>[\w\-]+)/$',index,name='index1'),
  
]
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
