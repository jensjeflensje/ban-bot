from django.db import models


class Ban(models.Model):
    reason = models.TextField()
    user_name = models.TextField()
    user_id = models.TextField()
    server_name = models.TextField()
    server_id = models.TextField()