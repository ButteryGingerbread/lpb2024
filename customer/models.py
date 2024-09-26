from django.db import models

class Customer(models.Model):
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    condition = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'