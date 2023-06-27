from django.contrib import admin
from .models import UsersModel, HeroListModel, GameModel


admin.site.register(UsersModel)
admin.site.register(HeroListModel)
admin.site.register(GameModel)


class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 25


class HeroListModelAdmin(admin.ModelAdmin):
    list_display = ['HEROES']
    list_per_page = 15


class GameModelAdmin(admin.ModelAdmin):
    list_display = ['game_name', 'game_time']
    list_per_page = 10
