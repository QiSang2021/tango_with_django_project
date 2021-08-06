from django.contrib import admin
from rango.models import Category, Page, Article, Comment


# customize the admin interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brandname',)}

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('clothname',)}
    #list_display = ('category', 'clothname', 'url')

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'comtime', 'author')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment, CommentAdmin)