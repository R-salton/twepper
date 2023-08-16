from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister user

admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile
# extends USer MOdel

# Combine User and Profile
class UserAdmin(admin.ModelAdmin):
    model = User
    # Display USer Fields
    fields = ["username"]
    inlines = [ProfileInline]

# unregister user Initial User
admin.site.unregister(User)
# Register user and pr eofile

admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
