class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidean_to_origin(p: List[int]) -> float:
            return math.sqrt((p[0] ** 2)+ (p[1] ** 2)) # sqrt (x^2 + y^2)

        distances = [euclidean_to_origin(point) for point in points] # O(N)
        # Brute force
        # Sort distances and points based on distances
        # Sort both lists based on distances
        sorted_pairs = sorted(zip(distances, points))  # Sorts by the first element (distance)

        # Unzip back to separate lists
        sorted_distances, sorted_points = zip(*sorted_pairs)
        return list(sorted_points[:k])
        

        

