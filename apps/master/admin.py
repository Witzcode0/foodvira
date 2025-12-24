from django.contrib import admin
from apps.master.models import Contact, BlogCategory, Blog, TeamMember
# Register your models here.


admin.site.register(Contact)
admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(TeamMember)