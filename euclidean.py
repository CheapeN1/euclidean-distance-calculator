import math

# Öklid Mesafesi Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktalar (2D uzayındaki demetler)
points = [(1, 2), (4, 6), (5, 9), (3, 8)]

# Mesafelerin saklanacağı liste
distances = []

# Noktalar arası mesafeleri hesapla ve mesafeler listesine ekle
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"{points[i]} ile {points[j]} arasındaki mesafe: {distance:.2f}")

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print(f"\nEn kısa mesafe: {min_distance:.2f}")
