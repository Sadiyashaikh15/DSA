class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        
        # If the grid is too small to trap water (e.g., all cells are on perimeter)
        if m < 3 or n < 3:
            return 0

        min_heap = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        total_trapped_water = 0
        
        
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        
        # Directions for neighbors: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while min_heap:
            current_boundary_height, r, c = heapq.heappop(min_heap)
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if already visited
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                
                    
                    if heightMap[nr][nc] < current_boundary_height:
                        total_trapped_water += (current_boundary_height - heightMap[nr][nc])
                    
                    
                    new_boundary_height = max(current_boundary_height, heightMap[nr][nc])
                    heapq.heappush(min_heap, (new_boundary_height, nr, nc))
                    
        return total_trapped_water