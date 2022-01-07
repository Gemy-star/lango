from ckeditor.fields import RichTextField
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ordered_model.models import OrderedModel
from .category_model import Category


class Course(OrderedModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")
    image = models.ImageField(upload_to="courses_image")
    image_webp = ImageSpecField(source="image", format="WEBP", options={"quality": 100})
    summary = RichTextField()
    description_col_1 = RichTextField()
    description_col_2 = RichTextField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        "courses.Category", null=True, blank=True, on_delete=models.DO_NOTHING
    )
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

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return f"{self.name}"

    def image_url(self):
        return self.image.url if self.image else static("images/courses/course.png")

    def image_webp_url(self):
        return (
            self.image_webp.url
            if self.image
            else static("images/courses/course.png")
        )

    def image_thumb_webp_url(self):
        return (
            self.image_thumb_webp.url
            if self.image
            else static("images/courses/course.png")
        )

    def image_thumb_png_url(self):
        return (
            self.image_thumb_png.url
            if self.image
            else static("images/courses/course.png")
        )

    def image_thumbnail_url(self):
        return (
            self.image_thumb.url
            if self.image
            else static("images/courses/course.png")
        )
