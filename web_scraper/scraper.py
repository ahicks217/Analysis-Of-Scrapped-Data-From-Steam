import requests
import sqlite3
import pandas as pd

def to_db(db_path, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS data(id, name, developer, publisher, description)")
    cursor.execute("INSERT OR REPLACE INTO data(id, name, developer, publisher, description) VALUES (?, ?, ?, ?, ?)", (
                   data[appid]["data"]["steam_appid"],
                   data[appid]["data"]["name"],
                   ", ".join(data[appid]["data"]["developers"]),
                   ", ".join(data[appid]["data"]["publishers"]),
                   data[appid]["data"]["short_description"]
    ))

    conn.commit()
    conn.close()
    
def save_csv(data, file, appid):    
    df = pd.DataFrame([{
        "id": data[appid]["data"]["steam_appid"],
        "name": data[appid]["data"]["name"],
        "developer": ", ".join(data[appid]["data"]["developers"]),
        "publisher": ", ".join(data[appid]["data"]["publishers"]),
        "description": data[appid]["data"]["short_description"]
    }])

    df.to_csv(file, index=False)

if __name__=="__main__":
    db_path = "data.db"
    csv_path = "data.csv"

    appid = input("Enter steam app ID: ")

    url = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appid}")
    print("application found")
    data = url.json()
    
if not data.get(appid) or not data[appid].get("data"):
    print("No valid data found for this app ID.")
    
    choice = input("Select the type of format the data will be saved in. (1=database, 2=csv): ")
    if choice == "1":
        to_db(db_path, data)
        print(f"data saved successfully to {db_path}")

    elif choice == "2":
        save_csv(data, csv_path, appid)
        print(f"data saved successfully to {csv_path}")




