class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [0] * n  # Initialize the answer array. 0 will act as a placeholder for dry days.

        # Maps lake ID to the index of the day it last rained and became full.
        # This helps identify which lakes are currently full.
        lake_to_last_rain_day = {}

        # Stores indices of available dry days (where rains[i] == 0).
        # We use a SortedList to efficiently find and remove the earliest available dry day
        # that occurs after a specific previous rain day.
        dry_day_indices = SortedList() 

        for i in range(n):
            lake_id = rains[i]

            if lake_id > 0:
                # If it rains on a specific lake
                ans[i] = -1  # As per problem, mark rain days with -1.
                
                # Check if this lake (lake_id) has already rained before and is currently full.
                if lake_id in lake_to_last_rain_day:
                    prev_rain_day = lake_to_last_rain_day[lake_id]
                    
                    # A flood is imminent for lake_id. We need to find a dry day
                    # that occurs *after* prev_rain_day but *before* the current day 'i'.
                    # We search for the smallest dry day index 'j' such that j > prev_rain_day.
                    # bisect_right finds the insertion point for prev_rain_day,
                    # which corresponds to the index of the first element strictly greater than prev_rain_day.
                    idx_in_dry_days_list = dry_day_indices.bisect_right(prev_rain_day)
                    
                    if idx_in_dry_days_list == len(dry_day_indices):
                        # No suitable dry day found. A flood cannot be avoided.
                        return []
                    
                    # This is the earliest dry day after the previous rain for this lake.
                    day_to_dry = dry_day_indices[idx_in_dry_days_list]
                    
                    # Assign this dry day to dry the flooding lake.
                    ans[day_to_dry] = lake_id
                    
                    # Remove this dry day from the available dry days list as it's now used.
                    dry_day_indices.pop(idx_in_dry_days_list)
                
                # Update the last rain day for this lake. It is now full from this rain.
                lake_to_last_rain_day[lake_id] = i
            
            else: # rains[i] == 0, it's a dry day
                # Add the current day's index to the list of available dry days.
                dry_day_indices.add(i)
                # ans[i] remains 0 for now. It will be assigned a specific lake ID later
                # if this dry day is used to prevent a flood.

        # After processing all days, iterate through ans again.
        # Any `ans[i]` that is still 0 means it was a dry day that was not
        # explicitly used to prevent a specific flood. For these days, we can
        # choose to dry any arbitrary lake (e.g., lake 1). Drying an empty lake
        # has no effect, so this is a valid assignment.
        for i in range(n):
            if ans[i] == 0:
                ans[i] = 1 

        return ans
