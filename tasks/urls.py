from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"), 
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("tasks/complete/<int:pk>/", views.mark_complete, name="mark_complete"),
    path("tasks/toggle/<int:pk>/", views.toggle_complete_ajax, name="toggle_complete_ajax"),
]



