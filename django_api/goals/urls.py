from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.goal_list_create, name='goal-list-create'),
    path('goals/<int:goal_id>/', views.goal_detail, name='goal-detail'),
]