from django.urls import path

from tempracatao.healthcheck.views import HealthCheckView

urlpatterns = [
    path("", HealthCheckView.as_view(), name="healthcheck"),
]
