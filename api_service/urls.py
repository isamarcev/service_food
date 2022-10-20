from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('order/', views.CreateOrderView.as_view())
]

router = routers.DefaultRouter()
router.register(r'checks', views.ChecksViewSet, basename="api")
# router.register(r'order', views.CreateOrderView, basename="order")

urlpatterns += router.urls
