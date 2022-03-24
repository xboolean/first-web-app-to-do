from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.TaskTableView.as_view(), name='index'),
    path('detail/<pk>', views.TaskDetailView.as_view(), name='detail_view'),
    path('empty_response/', views.response, name='response')
    
]

htmx_urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path('task/edit/<int:pk>/', views.EditTaskView.as_view(), name='edit_task'),
    path('task/complete/<int:pk>/', views.TaskCompleteView.as_view(), name='complete_task'),
    path('task/delete/<pk>', views.TaskDeleteView.as_view(), name='delete_task'),
]

urlpatterns += htmx_urlpatterns
