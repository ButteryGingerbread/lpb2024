from django.db import models

# Create your models here.

class Menu(models.Model):
    menu_name = models.CharField(max_length=256, blank=True, null=True)
    menu_ingredients = models.TextField(blank=True, null=True)
    menu_instructions = models.TextField(blank=True, null=True)
    menu_category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'

    def serialize(self):
        return {
            "menu_name": self.menu_name,
            "menu_ingredients": self.menu_ingredients,
            "menu_instructions": self.menu_instructions,
            "menu_category": self.menu_category
        }