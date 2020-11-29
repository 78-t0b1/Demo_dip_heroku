"""demo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include,re_path
from first_app import views as fv
from second_app import views as sv




urlpatterns = [
	path('',fv.index,name='new'),
	path('2nd/',sv.hi,name='scnd'),
	path('1st/',include('first_app.urls')),
    path('admin/', admin.site.urls),
    re_path(r'help/$',fv.help_func), 					#Becouse of this if url contains help at the end. it will redirect page to help.
]
