from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user_id = models.BigIntegerField(null=False)

    class Meta:
        managed = False
        db_table = 'user_profile'