from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.view_all_tasks, name='task_list'),
    path('task/<int:pk>/update_status/', views.update_task_status, name='update_task_status'),
    path('task/<int:pk>/', views.view_details, name='task_detail'),
    path('task/new/', views.create_task, name='task_create'),
    path('task/<int:pk>/edit/', views.update_task, name='task_update'),
    path('task/<int:pk>/delete/',views.delete_task, name='task_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)