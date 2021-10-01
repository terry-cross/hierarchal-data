from django.db import models
from django.db.models.fields.related import RelatedField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Hierarchy(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by= ['name']

