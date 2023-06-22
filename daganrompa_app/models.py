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

    def save(self, *args, **kwargs):
        super(UsersModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} | Discord: {self.discord} | GAMES: {self.total_game}'

class HeroListModel(models.Model):
    HEROES = ()
    hero = models.CharField(max_length=10, choices=HEROES)


class GameModel(models.Model):
    game_name = models.CharField(max_length=30)
    game_time = models.DateTimeField()
    game_master = models.CharField(max_length=30)
    game_admin = models.CharField(max_length=30)
    streamer = models.CharField(max_length=30)
    game_tag = models.CharField(max_length=100)
    ban_hero = models.CharField(max_length=100)
    game_map = models.CharField(max_length=30)
    comments = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super(GameModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.game_name} | TIME: {self.game_time} | MAP: {self.game_map}'
