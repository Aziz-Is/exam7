"""pythonexam7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from webapp.views import PollListView, DetailView, AddView, UpdateView, DeleteView, AddChoiceView, DeleteChoiceView, UpdateChoiceView, PollView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',PollListView.as_view(), name='home'),
    path('home/<int:pk>', DetailView.as_view(), name='detail'),
    path('add/', AddView.as_view()),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteView.as_view()),
    path('add_choices/', AddChoiceView.as_view(), name='add-choices'),
    path('delete_choices/<int:pk>', DeleteChoiceView.as_view(), name='delete-choices'),
    path('update_choices/<int:pk>', UpdateChoiceView.as_view(), name='update-choices'),
    path('poll/<int:pk>',PollView.as_view())
]
