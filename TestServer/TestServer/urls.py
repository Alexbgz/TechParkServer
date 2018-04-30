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
from django.conf.urls import url
from TestAPI import views
from rest_framework.authtoken.views import obtain_auth_token

# Раздача картинок
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api-token-auth/', obtain_auth_token),

                  url(r'^user/create$', views.UserCreate.as_view()),
                  url(r'^user/(?P<username>[0-9a-zA-Z_-]+)$', views.UserDetail.as_view()),
                  url(r'^user/(?P<username>[0-9a-zA-Z_-]+)/update$', views.UserUpdate.as_view()),

                  url(r'^test$', views.TestListCreate.as_view()),
                  url(r'^test/(?P<id>\d+)$', views.TestDetailUpdateDelete.as_view()),


                  url(r'^question/create$', views.QuestionCreate.as_view()),
                  url(r'^question/(?P<test>[0-9a-zA-Z_-]+)$', views.QuestionList.as_view()),
                  url(r'^question/(?P<id>[0-9a-zA-Z_-]+)/update$', views.QuestionUpdate.as_view()),

                  url(r'^answer/create$', views.AnswerCreate.as_view()),
                  url(r'^answer/(?P<question>[0-9a-zA-Z_-]+)$', views.AnswerList.as_view()),
                  url(r'^answer/(?P<id>[0-9a-zA-Z_-]+)/update$', views.AnswerUpdate.as_view()),

                  url(r'^usertest/create$', views.UserTestCreate.as_view()),
                  url(r'^usertest/(?P<username>[0-9a-zA-Z_-]+)$', views.UserTestList.as_view()),
                  url(r'^usertest/(?P<id>[0-9a-zA-Z_-]+)/update$', views.UserTestUpdate.as_view()),

                  url(r'^useranswer/create$', views.UserAnswerCreate.as_view()),
                  url(r'^useranswer/(?P<username>[0-9a-zA-Z_-]+)$', views.UserAnswerList.as_view()),
                  url(r'^useranswer/(?P<id>[0-9a-zA-Z_-]+)/update$', views.UserAnswerUpdate.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
