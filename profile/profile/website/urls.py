from django.urls import path
from .views import IndexView, ServiceView, CareerView, RecentView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('service/', ServiceView.as_view(), name='service'),
    path('career/', CareerView.as_view(), name='career'),
    path('contact/', RecentView.as_view(), name='recent'),
]