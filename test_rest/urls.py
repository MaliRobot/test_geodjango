"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^users$', views.user_plot, name='users'),
	url(r'^countries$', views.countries, name='data'),
	url(r'^regions$', views.regions, name='data'),
	url(r'^districts$', views.districts, name='data'),
	url(r'^territory/(?P<reg_id>[0-9]+)$', views.territory, name='territory'),
	url(r'', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

