class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        l = 0
        total = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                total += min(neededTime[l], neededTime[r])
                if neededTime[r] > neededTime[l]:
                    l = r         
            else:
                l = r            
        return total