from ckeditor.fields import RichTextField
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from ordered_model.models import OrderedModel


class Category(OrderedModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")
    summary = RichTextField()
    description_col_1 = RichTextField()
    description_col_2 = RichTextField(null=True, blank=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return f"{self.name}"

