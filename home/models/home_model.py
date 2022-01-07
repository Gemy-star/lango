from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _
from imagekit.processors import ResizeToFill


class HomePage(SingletonModel):
    introduction = RichTextField()
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    facts = RichTextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(
        max_length=256, null=True, blank=True, verbose_name=_("City")
    )
    country = models.CharField(
        max_length=256, null=True, blank=True, verbose_name=_("Country")
    )
    street = models.CharField(
        max_length=256, null=True, blank=True, verbose_name=_("Street")
    )
    hero_video = models.FileField(null=True, blank=True)
    apply = RichTextField()
    image = models.ImageField(upload_to="home/backgrounds")
    image_webp = ImageSpecField(source="image", format="WEBP", options={"quality": 100})
    image_thumb = ImageSpecField(
        source="image",
        options={"quality": 90},
    )
    image_thumb_png = ImageSpecField(
        source="image",
        processors=[ResizeToFill(380, 380)],
        format="PNG",
        options={"quality": 90},
    )
    image_thumb_webp = ImageSpecField(
        source="image",
        processors=[ResizeToFill(380, 380)],
        format="WEBP",
        options={"quality": 90},
    )
    apply_button_text = models.CharField(
        max_length=250,
        help_text="Apply Button Text",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("-last_modified", "-created_at")

    @property
    def Address(self):
        return f"{self.street} - {self.city} - {self.country}"

    @property
    def CategoriesHome(self):
        from courses.models.category_model import Category
        return Category.objects.all()

    @property
    def CoursesHome(self):
        from courses.models.course_model import Course
        return Course.objects.all()[:5]
