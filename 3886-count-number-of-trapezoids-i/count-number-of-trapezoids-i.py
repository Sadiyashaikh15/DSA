class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
       
        from collections import Counter
        y_count = Counter(y for _, y in points)
        
        
        choose2 = []
        for c in y_count.values():
            if c >= 2:
                choose2.append(c * (c - 1) // 2)
        
     
        if len(choose2) < 2:
            return 0

      
        total_sum = sum(choose2) % MOD
        square_sum = sum((x * x) % MOD for x in choose2) % MOD
        
      
        ans = (total_sum * total_sum - square_sum) % MOD
        ans = ans * pow(2, MOD-2, MOD)  
        
        return ans % MOD