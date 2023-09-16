"""
URL configuration for potumerakapro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from potumerakaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage,name='mainpage'),
    path('adddata',views.adddata, name='adddata'),
    path('see_sub',views.see_sub, name='see_sub'),
    path('update/<id>',views.update , name= 'update' ),
    path('update_data/<id>',views.update_data, name= 'update_data'),
    path('delete/<id>',views.delete, name= 'delete'),
    path('expenditure',views.expenditure, name= 'expenditure'),
    path('update_exp/<id>',views.update_exp, name='update_exp'),
    path('updated_exp/<id>',views.updated_exp, name='updated_exp'),
    path('delete_exp/<id>',views.delete_exp, name='delete_exp'),
    path('total_amount',views.total_amount,name='total_amount'),
    path('help',views.help,name='help')
]
