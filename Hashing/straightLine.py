def maxPoints(self, A, B):
        """Pick a point and check the relative slope of all other points to this point. If the two different points have the same slope they are in the same line. Check the maximum number of points a line can have by having this particular point on it's one end.
            Note:
            1. We don't need to check of intercept as we kept one end fixed.This way there is no possiblity of paralled lines.
            2. Overlapping points should be taken care off.
            3. Lines which are parallel to Y will give a infinite slope. So, keep a tracker for the points which fall in this vertical line.
            """
        if len(A) < 2:
            return len(A)
        global_max = 0
        for i in range(len(A)):
            # Keeping track of slopes for a given fixed point
            local_slope_dict = {}
            # Each point by itself is a vertical line.
            vertical = 1
            # overlapping points are added in the end in additional to local max.
            overlap = 0
            
            for j in range(i+1, len(A)):
               
                if A[i] == A[j] and B[i]==B[j]:
                    overlap += 1
                elif A[i] == A[j]:
                    vertical += 1
                else:
                    # In python 2 make sure to use float for high precision
                    # and to avoid to rounding down.
                    slope = (B[i]-B[j])/float(A[i]-A[j])
                    if slope in local_slope_dict:
                        local_slope_dict[slope] = local_slope_dict[slope] + 1
                    else:
                        local_slope_dict[slope] = 2
            
            local_max = 0
            
            for x in local_slope_dict.values():
                local_max = max(local_max,x)
            
            local_max = max(local_max,vertical)
            # Add any overlapping points
            local_max = local_max + overlap
            
            global_max = max(local_max,global_max)
            
        return global_max

print(maxPoints(None, [1,1], [2,2]))