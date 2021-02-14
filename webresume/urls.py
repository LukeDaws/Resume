"""WebResume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import (home_view,  
    resume_view,
    project_view,
    contact_view,
    pdf_view
) 

urlpatterns = [
    path('', home_view, name='home'),
    path('resume/', resume_view, name='resume'),
    path('project/', project_view, name='project'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),
    path('pdfs/', pdf_view, name='pdfs')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)