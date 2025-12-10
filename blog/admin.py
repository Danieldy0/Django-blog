# blog/admin.py
from django.contrib import admin
from .models import Post, PostImage 

# 1. Define an Inline class for the images
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    max_num = 5

# 2. Update the PostAdmin class to include the inline
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('title', 'author', 'created_on', 'status')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content')

# 3. Register the model using your custom PostAdmin class.
# *** COMMENT OUT OR DELETE THIS LINE IF YOU SEE IT: ***
# admin.site.unregister(Post) 

# *** Ensure only the final registration line is present: ***
admin.site.register(Post, PostAdmin)
