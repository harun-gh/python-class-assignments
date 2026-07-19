everyone_lives = []
prefectures = []

with open("hometown.csv", "r", encoding="shift_jis") as data:
    for line in data:
        everyone_lives.append(line.strip())

with open("Prefectures.txt", "r", encoding="utf-8") as data:
    for line in data:
        prefectures.append(line.strip())

print(everyone_lives)
print(prefectures)

common = [ prefecture for prefecture in prefectures if not any(prefecture in live for live in everyone_lives) ]

print(common)