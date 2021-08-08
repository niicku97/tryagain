
from django.contrib import admin
from django.urls import path

from myApp.views import AnimeViewSet,UserViewSet
from rest_framework import routers
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
#filtered by user logged in with token
router.register(r'animes', AnimeViewSet)
router.register(r'user', UserViewSet)


api_urlpatterns = [

    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('myapi/v1/', include(api_urlpatterns)),
]

