from django.db import models


class UsersModel(models.Model):
    BAN = (
        ('T', 'True'),
        ('F', 'False')
    )
    VIP = (
        ('T', 'True'),
        ('F', 'False')
    )
    name = models.CharField(max_length=16)
    email = models.EmailField(null=True)
    discord = models.CharField(max_length=30)
    steam = models.URLField()
    total_game = models.IntegerField()
    history_game = models.IntegerField()
    # main_hero
    ban = models.CharField(max_length=1, choices=BAN)
    vip = models.CharField(max_length=1, choices=VIP)


class HeroListModel(models.Model):
    pass


class GameModel(models.Model):
    pass