
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# Create a router and register our viewset with it.
router=DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken'), 
]
