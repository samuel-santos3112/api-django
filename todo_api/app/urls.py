from app.views import TodoListAndCreate, TodoDetailChangeAndDelete

from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:id>/', TodoDetailChangeAndDelete.as_view())
]