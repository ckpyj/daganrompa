from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    total_game = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    history_game = models.IntegerField()
    # main_hero
    ban = models.CharField(max_length=1, choices=BAN, default="F")
    vip = models.CharField(max_length=1, choices=VIP, default="F")

    def save(self, *args, **kwargs):
        super(UsersModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} | Discord: {self.discord} | GAMES: {self.total_game}'


class HeroListModel(models.Model):
    HEROES = (
        ('Макото Наэги', 'Макото Наэги'),
        ('Кёко Киригири', 'Кёко Киригири'),
        ('Киётака Ишимару', 'Киётака Ишимару'),
        ('Саяка Майзоно', 'Саяка Майзоно'),
        ('Ясухиро Хагакурэ', 'Ясухиро Хагакурэ'),
        ('Чихиро Фуджисаки', 'Чихиро Фуджисаки'),
        ('Хифуми Ямада', 'Хифуми Ямада'),
        ('Бьякуя Тогами', 'Бьякуя Тогами'),
        ('Мондо Овада', 'Мондо Овада'),
        ('Селестия Люденберг', 'Селестия Люденберг'),
        ('Аой Асахина', 'Аой Асахина'),
        ('Леон Кувата', 'Леон Кувата'),
        ('Сакура Огами', 'Сакура Огами'),
        ('Токо Фукава', 'Токо Фукава'),
        ('Убийца Сё (Геноцид Джек)', 'Убийца Сё (Геноцид Джек)'),
        ('Джунко Эношима', 'Джунко Эношима'),
        ('Хаджимэ Хината', 'Хаджимэ Хината'),
        ('Пеко Пекояма', 'Пеко Пекояма'),
        ('Нагито Комаэда', 'Нагито Комаэда'),
        ('Ибуки Миода', 'Ибуки Миода'),
        ('Махиру Коизуми', 'Махиру Коизуми'),
        ('Чиаки Нанами', 'Чиаки Нанами'),
        ('Фуюхико Кузурю', 'Фуюхико Кузурю'),
        ('Микан Цумики', 'Микан Цумики'),
        ('Гандам Танака', 'Гандам Танака'),
        ('Сония Невермайнд', 'Сония Невермайнд'),
        ('Казуичи Сода', 'Казуичи Сода'),
        ('Нэкомару Нидай', 'Нэкомару Нидай'),
        ('Хиёко Сайонджи', 'Хиёко Сайонджи'),
        ('Аканэ Овари', 'Аканэ Овари'),
        ('Бьякуя Тогами', 'Бьякуя Тогами'),
        ('Тэрутэру Ханамура', 'Тэрутэру Ханамура'),
        ('Каэде Акамацу', 'Каэде Акамацу'),
        ('Кируми Тоджо', 'Кируми Тоджо'),
        ('Кайто Момота', 'Кайто Момота'),
        ('Цумуги Широганэ', 'Цумуги Широганэ'),
        ('Корекиё Шингуджи', 'Корекиё Шингуджи'),
        ('Кокичи Ома', 'Кокичи Ома'),
        ('Шуичи Сайхара', 'Шуичи Сайхара'),
        ('Миу Ирума', 'Миу Ирума'),
        ('Маки Харукава', 'Маки Харукава'),
        ('Гонта Гокухара', 'Гонта Гокухара'),
        ('Анджи Ёнага', 'Анджи Ёнага'),
        ('Химико Юмено', 'Химико Юмено'),
        ('Тенко Чабашира', 'Тенко Чабашира'),
        ('К1-B0 (Кибо)', 'К1-B0 (Кибо)'),
        ('Рёма Хоши', 'Рёма Хоши'),
        ('Рантаро Амами', 'Рантаро Амами'),
        ('Комару Наэги', 'Комару Наэги'),
        ('Масару Даймон', 'Масару Даймон'),
        ('Джатаро Кемури', 'Джатаро Кемури'),
        ('Нагиса Шингецу', 'Нагиса Шингецу'),
        ('Котоко Уцуги', 'Котоко Уцуги'),
        ('Монака Това', 'Монака Това'),
        ('Рёко Отонаши', 'Рёко Отонаши'),
        ('Оки Ноксо', 'Оки Ноксо'),

    )
    hero = models.CharField(max_length=24, choices=HEROES)

    def save(self, *args, **kwargs):
        super(HeroListModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.HEROES}'


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
