songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])

print(songs[1:3])

songs[2] = "Safari Disco Club"
print(songs)

songs.append("Completement Fou")
songs.extend(["Moteur Action"])
songs.insert(0, "Que Veux Tu")
print(songs)

del songs[2]
print(songs)

animals = ["Cat", "Dog", "Bird"]
animals.append("Fish")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)