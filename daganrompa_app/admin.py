from django.contrib import admin
from .models import UsersModel, HeroListModel, GameModel


admin.site.register(UsersModel)
admin.site.register(HeroListModel)
admin.site.register(GameModel)

@admin.register(UsersModel)
class UsersModelAdmin(admin.ModelAdmin):
    pass

@admin.register(HeroListModel)
class HeroListModelAdmin(admin.ModelAdmin):
    pass

@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    pass