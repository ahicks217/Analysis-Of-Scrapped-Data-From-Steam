from django.db import models

class SteamGame(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    dlc = models.TextField(default="N/A")  # <--- add default
    has_drm = models.BooleanField(null=True, blank=True, default=None) 
    platform_windows = models.BooleanField(default=False)
    platform_mac = models.BooleanField(default=False)
    platform_linux = models.BooleanField(default=False)
    release_date = models.TextField(default="N/A")
    coming_soon = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    required_age = models.IntegerField(default=0)
    controller_support = models.TextField(default="N/A")
    demos = models.TextField(default="N/A")
    metacritic_score = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    

# Related Tables (for lists)
class Developer(models.Model):
    name = models.TextField()
    game = models.ForeignKey(SteamGame, on_delete=models.CASCADE, related_name='developers')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.TextField()
    game = models.ForeignKey(SteamGame, on_delete=models.CASCADE, related_name='publishers')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField()
    game = models.ForeignKey(SteamGame, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField()
    game = models.ForeignKey(SteamGame, on_delete=models.CASCADE, related_name='genres')

    def __str__(self):
        return self.name


class SupportedLanguage(models.Model):
    name = models.TextField()
    game = models.ForeignKey(SteamGame, on_delete=models.CASCADE, related_name='supported_languages')

    def __str__(self):
        return self.name


# Pricing table
class Pricing(models.Model):
    game = models.ForeignKey(SteamGame, on_delete=models.CASCADE, related_name='pricing')
    currency = models.TextField()
    discount = models.IntegerField()
    initial_price = models.TextField()
    final_price = models.TextField()

    def price_display(self):
        try:
            return f"{float(self.final_price) / 100:.2f}"
        except:
            return None

    def __str__(self):
        return f"{self.game.name} - {self.currency} {self.final_price}"