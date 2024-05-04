from django.contrib import admin
from .models import Contents ,Category , Comment, MsgFromAdmin, SayToMe, UserProfile, MusicOfDay
from django.utils import timezone
from datetime import timedelta
# Register your models here.


@admin.register(MusicOfDay)
class MusicOfDayAdmin(admin.ModelAdmin):
    list_display = ('slug', 'image',)
@admin.register(Contents)
class SeeContents(admin.ModelAdmin):
    list_display = ['user','slug','title','uploaded_at','updated_at','likes','dislikes','views','descript','picture','slug',]
    # fields='__all__'
# Register the model with the custom admin class

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('content', 'commenter_name', 'commenter_photo', 'comment',)

admin.site.register(UserProfile)


@admin.register(SayToMe)
class UserSayToMe(admin.ModelAdmin):
    list_display = ('name_is', 'saying', )


admin.site.register(MsgFromAdmin)

