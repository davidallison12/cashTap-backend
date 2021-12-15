from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Bill, Profile
# Register your models here.

admin.site.register(Bill)
admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define new User Admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)




# Reregister Admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)