from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ml', views.ApprovalsView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('form/', views.cxcontact, name='cxform'),
]
