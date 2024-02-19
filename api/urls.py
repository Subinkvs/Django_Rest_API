from django.urls import path, include
from home.views import *
from home.views import PersonViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', PersonViewSets, basename='users')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name='index'),
    path('person/', person, name='person'),
    path('personview/', PersonView.as_view(), name='personview'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login' )
]