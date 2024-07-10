from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user_id = models.BigIntegerField(null=False)
    birth_date = models.DateField(max_length="100")
    gender = models.CharField(max_length=6)
    condition = models.CharField(max_length=11)
    class Meta:
        db_table = 'user_profile'