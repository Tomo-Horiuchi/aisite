"""
satomimodels
"""
from datetime import timezone
from django.db import models

IMG_DIR = 'satomi'

# Create your models here.
class SatomiImg(models.Model):
    """
    画像情報
    """
    image = models.ImageField(upload_to=IMG_DIR, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        画像取得時刻取得
        """
        self.published_date = timezone.now()
        self.save()
