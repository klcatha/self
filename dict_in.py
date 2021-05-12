songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live",
         "6": "eden"
         }

n = input("please number")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("not exist")
