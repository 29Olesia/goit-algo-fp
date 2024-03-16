import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, src, dest, weight):
        self.vertices[src][dest] = weight

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]  

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex == start and current_distance > 0:
                continue

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

cities = ['a', 'b', 'c', 'd', 'e', 'f']
distances = {
    ('a', 'b'): 25,
    ('a', 'c'): 32,
    ('a', 'd'): 47,
    ('a', 'e'): 81,
    ('a', 'f'): 27,
}

g = Graph()
for city in cities:
    g.add_vertex(city)
for (city1, city2), distance in distances.items():
    g.add_edge(city1, city2, distance)

start_city = 'a'
shortest_paths = g.dijkstra(start_city)

print(f"Найкоротші відстані від міста {start_city}:")
for city, distance in shortest_paths.items():
    print(f"Від {start_city} до {city}: {distance} km")
