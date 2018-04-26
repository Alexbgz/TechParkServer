"""TestServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from TestAPI import views
from rest_framework.authtoken.views import obtain_auth_token

#Раздача картинок
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api-token-auth/', obtain_auth_token),

                  url(r'^user/create$', views.UserCreate.as_view()),
                  url(r'^user/(?P<username>[0-9a-zA-Z_-]+)$', views.UserDetail.as_view(), name='user-detail'),
                  url(r'^user/(?P<username>[0-9a-zA-Z_-]+)/update$', views.UserUpdate.as_view(), name='user-detail'),

                  url(r'^test$', views.TestList.as_view()),
                  url(r'^test/create$', views.TestCreate.as_view()),
                  url(r'^test/(?P<id>\d+)$', views.TestDetail.as_view(), name='test-detail'),
                  #url(r'^test/(?P<id>\d+)/update$', views.TestUpdate.as_view(), name='test-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
