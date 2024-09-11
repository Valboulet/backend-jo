from django.urls import path
from . import views

app_name = "backoffice"

urlpatterns = [
    path("api/", views.EventListView.as_view(), name="events")
]
