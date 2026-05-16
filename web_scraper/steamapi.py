import os
import django
import pandas as pd
import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup as bs    
import re

#Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

#django models
from steam_app.models import SteamGame, Developer, Publisher, Category, Genre, SupportedLanguage, Pricing

def get_data(data, appid):
    if appid in data and data[appid]["success"]:
        app_data = data[appid]["data"]

        # Basic game info
        id = app_data["steam_appid"]
        name = app_data.get("name", "N/A")

        # dev/pub = array
        developer = app_data.get("developers", ["N/A"])
        publisher = app_data.get("publishers", ["N/A"])
        
        # DLC = integer
        dlc = len(app_data["dlc"]) if app_data.get("dlc") else "N/A"
        
        # Platforms
        platforms = app_data.get("platforms", {})
        platform_windows = platforms.get("windows", False)
        platform_mac = platforms.get("mac", False)
        platform_linux = platforms.get("linux", False)

        # Release data
        release_date_info = app_data.get("release_date", {})
        release_date = release_date_info.get("date", "N/A")
        coming_soon = release_date_info.get("coming_soon", False)

        # Other metadata
        is_free = app_data.get("is_free", False)
        required_age = app_data.get("required_age", 0)
        controller_support = app_data.get("controller_support", "N/A")
        demos = len(app_data["demos"]) if app_data.get("demos") else "N/A"

        # Price overview
        p_overview = app_data.get("price_overview", {})
        currency = p_overview.get("currency", "N/A")
        discount = p_overview.get("discount_percent", 0)
        initial = p_overview.get("initial", "N/A")
        final = p_overview.get("final", "N/A")
        metacritic_score = app_data.get("metacritic", {}).get("score")

        # Categories and genres
        categories = [c.get("description", "N/A") for c in app_data.get("categories", [])]
        genres = [c.get("description", "N/A") for c in app_data.get("genres", [])]

        # Supported languages
        supported_languages = app_data.get("supported_languages", "")
        soup = bs(supported_languages, "html.parser")
        text = soup.get_text(separator=" ")
        text = re.sub(r"^.*supported_languages:\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"languages with.*", "", text, flags=re.IGNORECASE)
        text = text.replace("*", "")
        items = [lang.strip() for lang in text.split(",") if lang.strip()]

        return {
            "id": id,
            "name": name,
            "developer": developer,
            "publisher": publisher,
            "dlc": dlc,
            "platform_windows": platform_windows,
            "platform_mac": platform_mac,
            "platform_linux": platform_linux,
            "release_date": release_date,
            "coming_soon": coming_soon,
            "is_free": is_free,
            "required_age": required_age,
            "controller_support": controller_support,
            "demos": demos,
            "currency": currency,
            "discount": discount,
            "initial": initial,
            "final": final,
            "metacritic_score": metacritic_score,
            "categories": categories,
            "genres": genres,
            "supported_languages": items
        }
    else:
        print(f"No data found for appid {appid}")
        return None

# Save data to Django database
def to_db(data):
    # Save main game record
    game, created = SteamGame.objects.update_or_create(
        id=data["id"],
        defaults={
            "name": data["name"],
            "dlc": data["dlc"],
            "platform_windows": data["platform_windows"],
            "platform_mac": data["platform_mac"],
            "platform_linux": data["platform_linux"],
            "release_date": data["release_date"],
            "coming_soon": data["coming_soon"],
            "is_free": data["is_free"],
            "required_age": data["required_age"],
            "controller_support": data["controller_support"],
            "demos": data["demos"],
            "metacritic_score": data["metacritic_score"]
        }
    )

    # Related models
    for dev in data.get("developer", []):
        Developer.objects.get_or_create(game=game, name=dev)
    for pub in data.get("publisher", []):
        Publisher.objects.get_or_create(game=game, name=pub)
    for cat in data.get("categories", []):
        Category.objects.get_or_create(game=game, name=cat)
    for genre in data.get("genres", []):
        Genre.objects.get_or_create(game=game, name=genre)
    for lang in data.get("supported_languages", []):
        SupportedLanguage.objects.get_or_create(game=game, name=lang)

    # Pricing info
    Pricing.objects.update_or_create(
        game=game,
        defaults={
            "currency": data.get("currency", "N/A"),
            "discount": data.get("discount", 0),
            "initial_price": data.get("initial", "N/A"),
            "final_price": data.get("final", "N/A")
        }
    )


# Main scraping loop
if __name__ == "__main__":
    id_pool = "steam_ids.csv"  # CSV with Steam App IDs
    df = pd.read_csv(id_pool)
    values = [v for col in df.to_dict().values() for v in col.values()]

    for i in values:
        appid = str(i)
        url = requests.get(f"https://store.steampowered.com/api/appdetails?l=english&appids={appid}")
        print(f"Fetching {appid} - Status Code: {url.status_code}")
        data = url.json()
        game_data = get_data(data, appid)
        if game_data:
            to_db(game_data)
        time.sleep(1.5)

    print("All Steam data saved to Django database.")