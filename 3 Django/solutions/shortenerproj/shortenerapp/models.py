from django.db import models
import re

class ShortURL(models.Model):
    code = models.CharField(max_length=10)
    url = models.URLField()
    clicks = models.IntegerField(default=0)

    def get_long_url_domain(self):
        pattern = r'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)'
        domain = re.search(pattern, self.url, re.IGNORECASE)
        return domain.group(1)
    
    def __str__(self):
        return self.code + ' - ' + self.url
