from re import template
from unicodedata import name
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('os', views.osPage, name='os'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('courses_windows', views.coursesWindowsPage, name='courses_windows'),
    path('courses_mac', views.coursesMacOsPage, name='courses_mac'),
    path('forum_mac', views.forumMacPage, name='forum_mac'),
    path('forum_windows', views.forumWindowsPage, name='forum_windows'),
    path('quiz_windows', views.quizWindowsPage, name='quiz_windows'),
    path('quiz_mac', views.quizMacPage, name='quiz_mac'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
]
