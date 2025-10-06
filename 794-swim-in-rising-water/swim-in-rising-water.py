class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        dist = [[float('inf')] * n for _ in range(n)]
        min_heap = []
        dist[0][0] = grid[0][0]
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        
        # Define the four possible directions (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Dijkstra's algorithm variant
        while min_heap:
            current_max_elevation, r, c = heapq.heappop(min_heap)
            
            if r == n - 1 and c == n - 1:
                return current_max_elevation
           
            if current_max_elevation > dist[r][c]:
                continue
            
            # Explore all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
               
                if 0 <= nr < n and 0 <= nc < n:
                   
                    new_max_elevation = max(current_max_elevation, grid[nr][nc])
                    if new_max_elevation < dist[nr][nc]:
                        dist[nr][nc] = new_max_elevation
                        heapq.heappush(min_heap, (new_max_elevation, nr, nc))
                        
        return dist[n-1][n-1]
