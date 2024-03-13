from django.urls import path
from . import views

urlpatterns = [
  path("",views.home, name="home"),
  path("about/",views.about, name="about"),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('hyejin/', views.HyejinView.as_view(), name='Hyejin_view'),
  path('extra/', views.ExtraView.as_view(), name='Extra_view'),
]
