import pandas as pd
import pdb

# I should mention here that Ed Sheeran is not exactly my favorite artist.
# But he makes a fine default.
music = pd.read_csv('/home/diogenes/python-cert/Wi2018-Classroom/students/jim/Lesson12/featuresdf.csv')

def generate_sheeran(artist_name):
    for i in range(len(music)):
        if artist_name in music.artists[i]:
            yield music.name[i]


def get_songs(criterion, threshold=0.5):
    tracks = []
    for i in range(len(music)):
        if music.iloc[i][criterion] >= threshold:
            track = (music.iloc[i]['artists'],
                     music.iloc[i]['name'],
                     music.iloc[i][criterion])
            tracks.append(track)
    return tracks


eds_tracks = generate_sheeran("Sheeran")

print("These are the tracks by Ed Sheeran:")

for track in music.artists:
    try:
        print(next(eds_tracks))
    except StopIteration:
        break

print("And these are the songs with energy >= 0.8:")

for song in get_songs('energy', 0.8):
    print(song)
