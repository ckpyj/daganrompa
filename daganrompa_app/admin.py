from django.contrib import admin
from .models import UsersModel, HeroListModel, GameModel


admin.site.register(UsersModel)
admin.site.register(HeroListModel)
admin.site.register(GameModel)


class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class HeroListModelAdmin(admin.ModelAdmin):
    pass


class GameModelAdmin(admin.ModelAdmin):
    pass