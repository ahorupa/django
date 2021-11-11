"""isano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path
# from isano.views import allpost
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from posting.views import*


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('menu/', menu, name='menu'),
    # path('post/', post, name='post'),
    path('details/<int:id>', allpost, name='detail'),
    path('new_users/', include('django.contrib.auth.urls')),
    path('new_users/', include('new_users.urls')),
    path('create-article', createArticleView, name='create_article')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
