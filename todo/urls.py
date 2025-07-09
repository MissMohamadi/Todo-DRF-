from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodoViewSetsApiView)

urlpatterns = [
    path('', views.all_todo ),
    path('<int:todo_id>', views.todo_detail_view),
    path('cbv/', views.TodoListApiView.as_view()),
    path('mixins/', views.TodoListMixinsApiview.as_view()),
    path('generics/', views.TodoListGenericApiView.as_view()),
    path('viewsets/', include(router.urls) ),
    path('cbv/<int:todo_id>', views.TodoDetailView.as_view()),
    path('mixins/<int:pk>', views.TodoDetailMixinsApiView.as_view()),
    path('generics/<int:pk>', views.TodoDetailGenericApiView.as_view()),
]