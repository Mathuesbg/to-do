from django.urls import path
from core import views

app_name = "todo"

urlpatterns = [
    path('create/', views.create_task, name="create"),
    path('status/<int:id>', views.change_status, name="status"),
    path('delete/<int:id>', views.delete_task, name="delete"),
    path('detail/<int:id>', views.detail_task, name="detail"),
    path('update/<int:id>', views.update_task, name="update"),
    path('', views.list_task, name="list"),
]