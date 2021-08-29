from django.contrib import admin
from .models import Hobby, UserExtendedInfo  # CommunityMember



# Register your models here.

# admin.site.register(CommunityMember)
admin.site.register(Hobby)
admin.site.register(UserExtendedInfo)


