class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_cost_per_stair = [None] * (len(cost) + 1)

        min_cost_per_stair[0], min_cost_per_stair[1] = 0, 0
       
        for i in range(2, len(cost) + 1):
            min_cost_per_stair[i] = min(min_cost_per_stair[i-1] + cost[i-1], min_cost_per_stair[i-2] + cost[i-2])
        
        return min_cost_per_stair[len(cost)]