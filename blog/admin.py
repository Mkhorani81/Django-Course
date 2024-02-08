from django.contrib import admin
from .models import Article, Categoty

# Admin header change
admin.site.site_header = "وبلاگ جنگویی من"


# Register your models here.

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message = "منتشر شد."
    else:
        message = "منتشر شدند."

    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message))


make_published.short_description = "انتشار مقالات انتخاب شده"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message = "پیش نویس شد."
    else:
        message = "پیش نویس شدند."

    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message))


make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"


def make_active(modeladmin, request, queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1:
        message = "فعال شد."
    else:
        message = "فعال شدند."
    modeladmin.message_user(request, "{} دسته بندی {}".format(rows_updated, message))


make_active.short_description = "فعال کردن دسته بندی های انتخاب شده."


def make_disactive(modeladmin, request, queryset):
    rows_updated = queryset.update(status=False)
    if rows_updated == 1:
        message = "غیرفعال شد."
    else:
        message = "غیرفعال شدند."
    modeladmin.message_user(request, "{} دسته بندی {}".format(rows_updated, message))


make_disactive.short_description = "غیرفعال کردن دسته بندی های انتخاب شده."


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_active, make_disactive]


admin.site.register(Categoty, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'author', 'jpublish','is_special' , 'status', 'category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']
    actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)
