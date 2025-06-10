from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()), # List all students
    # path('studentapi/', views.StudentCreate.as_view()), # Create a new student
    # path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()), # Retrieve a single student by primary key
    # path('studentapi/<int:pk>/', views.StudentPUT.as_view()), # Update a student by primary key
    # path('studentapi/<int:pk>/', views.StudentDelete.as_view()), # Delete a student by primary key






    ###FOr List and Create in one class
    path('studentapi/', views.StudentListandCreate.as_view()),

    ###For Retrieve, Update and Delete in one class
    path('studentapi/<int:pk>/', views.StudentRetrieveDestroyUpdate.as_view()),
    

]
