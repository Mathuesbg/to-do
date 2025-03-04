from django.urls import path
from core import views

app_name = "todo"

urlpatterns = [
    path('create/', views.create_task, name="create"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('status/<int:id>', views.change_status, name="status"),
    path('delete/<int:id>', views.delete_task, name="delete"),
    path('detail/<int:id>', views.detail_task, name="detail"),
    path('update/<int:id>', views.update_task, name="update"),
    path('', views.list_task, name="list"),
]