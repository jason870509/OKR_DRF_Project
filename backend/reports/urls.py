from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('<int:pk>/', views.report_detail_view),
    path('list_create/', views.report_list_create_view),
    path('list_personal/', views.report_personal_view),
    path('<int:pk>/update/', views.report_update_view),
    path('<int:pk>/delete/', views.report_destroy_view),

    path('category/list_create/', views.category_list_create_view)
]