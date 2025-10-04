class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            
            current_height = min(height[left], height[right])
            
            # Calculate the width of the current container
            current_width = right - left
            
            # Calculate the current area and update max_area if it's larger
            current_area = current_height * current_width
            max_area = max(max_area, current_area)
            
            # Move the pointer of the shorter line inwards
            # This is because moving the shorter line has the potential to find a taller line
            # which might increase the container's height. Moving the taller line would
            # only decrease the width, without any guarantee of increased height.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area





