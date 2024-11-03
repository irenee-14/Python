'''
2024.11.3
5340 - Secret Location
'''

lat = []
lon = []

for i in range(3):
    lat.append(str(len(str(input().rstrip()))))
for i in range(3):
    lon.append(str(len(str(input().rstrip()))))
print("Latitude", ":".join(lat))
print("Longitude", ":".join(lon))
