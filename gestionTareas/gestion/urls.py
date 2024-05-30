from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Tasks/', views.TaskListView.as_view(), name='Tasks'),
    path('Task/<uuid:pk>', views.TaskDetailView.as_view(), name='Task-detail'),
]

# Add URLConf to create, update, and delete Tasks
urlpatterns += [
    path('Task/create/', views.TaskCreate.as_view(), name='Task-create'),
    path('Task/<uuid:pk>/update/', views.TaskUpdate.as_view(), name='Task-update'),
    path('Task/<uuid:pk>/delete/', views.TaskDelete.as_view(), name='Task-delete'),
]
