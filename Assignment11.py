import pandas as pd

video_games_raw = pd.read_csv("video_games_raw.csv")

print("VIDEO GAME CATALOG MANAGER\n")

#user selects row
while True:
    try:
        selected_row = int(input("Please select a row to inspect: ").strip())
        if 0 <= selected_row < len(video_games_raw):
            break
        print(f"Enter a row number from 0 to {len(video_games_raw) - 1}.")
    except ValueError:
        print("Please enter a whole number.")
        
#grab data
game_row = video_games_raw.iloc[selected_row]

#display data
print(f"\nTitle: {game_row['Title']}")
print(f"Platform: {game_row['Platform']}")
print(f"Genre: {game_row['Genre']}")
print(f"Rating: {game_row['Rating']}")
print(f"Status: {game_row['Status']}\n")

#change data
new_status = input("Please enter updated status:\n")
video_games_raw.at[selected_row, "Status"] = new_status

#add recommended category
video_games_raw["Recommended"] = "No"
video_games_raw.loc[
    (video_games_raw["Rating"] >= 8) & (video_games_raw["Price"] <= 40), 
    "Recommended"
] = "Yes"

#display recommended games
recommended_games = video_games_raw.query('Recommended == "Yes"')[["Title", "Platform", "Price", "Rating"]].sample(3)
print("\nRecommended for You:")
print(recommended_games)

#save to new file
video_games_raw.to_csv("video_games_cleaned.csv", index = False)
print("\nThe catalog is updated.\n" \
"Saved as video_games_cleaned.csv")