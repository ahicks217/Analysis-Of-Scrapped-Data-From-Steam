import os 
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from steam_app.models import SteamGame

scraped_games = [
    # Example scraped data  
]


for game_data in scraped_games:
    SteamGame.objects.update_or_create(
        id=game_data['id'],  # fixed here
        defaults=game_data
    )


print(f"Inserted/updated {len(scraped_games)} games into the database.")
