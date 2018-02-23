from django.contrib import admin
from blog.models import vacancy

# Register your models here.

#class BlogAdmin(admin.ModelAdmin):
    
 #   prepopulated_fields = {'slug': ('title',)}

admin.site.register(vacancy) #, BlogAdmin)
