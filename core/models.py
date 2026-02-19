from django.db import models

class GitHubStat(models.Model):
    """ Model to store GitHub stats fetched from the API in JSON format """
    stats = models.JSONField(default=dict)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'GitHub Stats - Updated {self.last_updated}'
