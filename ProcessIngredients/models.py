from django.db import models

class Customer(models.Model):
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    condition = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'

class Menu(models.Model):
    menu_name = models.CharField(max_length=256, blank=True, null=True)
    menu_ingredients = models.TextField(blank=True, null=True)
    menu_instructions = models.TextField(blank=True, null=True)
    menu_category = models.TextField(blank=True, null=True)
    menu_image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'menu'

    def serialize(self):
        return {
            "id": self.id,
            "menu_name": self.menu_name,
            "menu_ingredients": self.menu_ingredients,
            "menu_instructions": self.menu_instructions,
            "menu_category": self.menu_category,
            "menu_image": self.menu_image
        }
