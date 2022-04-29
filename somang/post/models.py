from django.db import models
from datetime import datetime


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(
        "account.Team", related_name="team", on_delete=models.CASCADE, db_column="team_id")
    img_url = models.TextField(null=False)
    content = models.TextField(null=True)
    uploaded_at = models.DateTimeField(default=datetime.now(), blank=True)
