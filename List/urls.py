from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.task_view),
    path('task/<int:id>/', views.task_view_id),
]
