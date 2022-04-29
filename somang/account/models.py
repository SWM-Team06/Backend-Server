from django.db import models


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.TextField(null=False)
    project_name = models.TextField(null=False)
    description = models.TextField(null=True)
    account_id = models.TextField(null=False)
    account_pw = models.TextField(null=False)
    profile_url = models.TextField(null=True)
