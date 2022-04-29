from . import views
from django.urls import path

urlpatterns = [
    path("feed", views.feed_GET, name="feed_get"),
]
