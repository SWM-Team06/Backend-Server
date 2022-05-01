from . import views
from django.urls import path

urlpatterns = [
    path("feed", views.feed_GET, name="feed_get"),
    path('detail/<int:id>', views.post_details, name="post_details")

]
