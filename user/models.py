from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# デフォルトのユーザーテーブルにwebsiteとpictureの項目を追加した
# OneToOneフィールドで紐づける
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='user/', blank=True)

    def __str__(self):
        return self.user.username
