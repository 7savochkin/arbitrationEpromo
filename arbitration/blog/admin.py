from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post ModelAdmin for crud in admin panel"""
    list_display = ('view_preview_image', 'title', 'is_publish', 'updated_at', 'created_at')
    list_display_links = ('view_preview_image', 'title')
    list_filter = ('is_publish',)
    fields = ('title', 'slug',
              'view_preview_image', 'preview', 'view_banner_image', 'banner', 'content',
              'is_publish', 'updated_at', 'created_at')
    search_fields = ('title__startswith',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('view_preview_image', 'view_banner_image', 'updated_at', 'created_at')

    def view_preview_image(self, obj): # noqa
        """View preview image in admin panel"""
        return mark_safe('<img src="{}" width="64" height="64" />'.format(obj.preview.url))

    def view_banner_image(self, obj): # noqa
        """View banner image in admin panel"""
        return mark_safe('<img src="{}" width="128" height="128" />'.format(obj.banner.url))

    view_preview_image.short_description = 'Preview Image'
    view_banner_image.short_description = 'Banner Image'
