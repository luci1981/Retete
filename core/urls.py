from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.topics, name='topics'),
    path('<int:pk>/new/', views.new_topic, name='new'),
    path('<int:pk>/titluri/<int:topic_pk>/', views.postari, name='discutii'),
    path('<int:pk>/titluri/<int:topic_pk>/new', views.new_post, name='comment'),
]
