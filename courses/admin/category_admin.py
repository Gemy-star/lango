from django.contrib import admin
from ..models import Category, Course


class CourseInline(admin.StackedInline):
    model = Course
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (CourseInline,)
    pass


admin.site.register(Category, CategoryAdmin)
# from ordered_model.admin import OrderedModelAdmin
#
# from ..models import Category, Course
#
#
# class CoursesInline(admin.StackedInline):
#     model = Course
#     extra = 1
#
#
# @admin.register(Category)
# class CategoryAdmin(OrderedModelAdmin):
#     list_display = (
#         "name",
#         "summary",
#     )
#     search_fields = ("name",)
#     fields = ['name', 'summary', 'description_col_1', 'description_col_2']
