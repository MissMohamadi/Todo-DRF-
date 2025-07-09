from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todo ),
    path('<int:todo_id>', views.todo_detail_view),
    path('cbv/', views.TodoListApiView.as_view()),
    path('mixins/', views.TodoListMixinsApiview.as_view()),
    path('cbv/<int:todo_id>', views.TodoDetailView.as_view()),
    path('mixins/<int:pk>', views.TodoDetailMixinsApiView.as_view()),
]