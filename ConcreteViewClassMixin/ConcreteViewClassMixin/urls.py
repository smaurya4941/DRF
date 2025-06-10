from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentListView.as_view()),
    # path('studentapi/', views.StudentCreateview.as_view()),
    # path('studentapi/<pk>/', views.StudentRetrieveView.as_view()),
    # path('studentapi/', views.StudentListCreateView.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveUpdateView.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroyView.as_view())

]
