
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token


# Create a router and register our viewset with it.
router=DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',obtain_auth_token),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
