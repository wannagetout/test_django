from django.urls import path
from task import views

urlpatterns = [
    path('', views.get_all_tasks),
    path('create/', views.create_task),
    path('edit/<int:id>/', views.update_task),
    path('delete/<int:id>/', views.delete_task),
]
