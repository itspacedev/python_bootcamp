from songs_helper import top_songs_by_date

date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ").strip()
songs = top_songs_by_date(date)

for song_idx, song in enumerate(songs):
    print(f"{song_idx+1}. {song['artist']} - {song['title']}")
