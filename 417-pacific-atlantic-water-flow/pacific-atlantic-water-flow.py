class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        
        # pacific_reachable[r][c] = True if water can flow from (r,c) to Pacific Ocean
        pacific_reachable = [[False for _ in range(n)] for _ in range(m)]
        # atlantic_reachable[r][c] = True if water can flow from (r,c) to Atlantic Ocean
        atlantic_reachable = [[False for _ in range(n)] for _ in range(m)]

        # Queues for BFS for Pacific and Atlantic oceans
        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()

        # Initialize queues and mark border cells as reachable from their respective oceans
        # Pacific Ocean: Top row (r=0) and Left column (c=0)
        # Atlantic Ocean: Bottom row (r=m-1) and Right column (c=n-1)
        for r in range(m):
            # Leftmost column for Pacific
            pacific_queue.append((r, 0))
            pacific_reachable[r][0] = True
            
            # Rightmost column for Atlantic
            atlantic_queue.append((r, n - 1))
            atlantic_reachable[r][n - 1] = True
        
        for c in range(n):
            # Topmost row for Pacific
            pacific_queue.append((0, c))
            pacific_reachable[0][c] = True
            
            # Bottommost row for Atlantic
            atlantic_queue.append((m - 1, c))
            atlantic_reachable[m - 1][c] = True
        
        # Possible directions to move (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # BFS helper function to find all cells reachable from the starting queue
        # based on the "uphill" flow condition
        def bfs(queue, reachable_matrix):
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if neighbor is within bounds
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    
                    # Check if neighbor has not been visited for this ocean yet
                    if reachable_matrix[nr][nc]:
                        continue
                    
                    # Check "uphill" flow condition: 
                    # water from neighbor (nr, nc) can flow to current cell (r, c)
                    # if neighbor's height is greater than or equal to current cell's height.
                    # This means (nr, nc) can also reach the ocean that (r, c) reaches.
                    if heights[nr][nc] >= heights[r][c]:
                        reachable_matrix[nr][nc] = True
                        queue.append((nr, nc))

        # Run BFS from Pacific and Atlantic borders
        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)

        # Collect cells that can reach both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])
                    
        return result