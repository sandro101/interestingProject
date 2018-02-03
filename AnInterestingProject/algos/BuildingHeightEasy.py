class BuildingHeightsEasy:
    def minimum(self, numberOfBuildings, heights):
        if numberOfBuildings == 1: return 0 
        cost = {}; 
        heights = sorted(heights)
        j=numberOfBuildings;
        possible_heights = heights[numberOfBuildings - 1:]      
        for possible_height in possible_heights:           
            cost[possible_height] = numberOfBuildings * possible_height - sum(heights[:j][j-numberOfBuildings:])
            j = j + 1
        return sorted(cost.values())[0]      
#print(BuildingHeightsEasy().minimum(1, [3,1,2]) == 0);
#print(BuildingHeightsEasy().minimum(2, [3,1,2]) == 1);
#print(BuildingHeightsEasy().minimum(3, [3,1,2]) == 3);
#print(BuildingHeightsEasy().minimum(7, {3,1,2,7,4,5,8}) == 26);
#print(BuildingHeightsEasy().minimum(2, [1, 2, 1, 4, 3]) == 0);
#print(BuildingHeightsEasy().minimum(39, [33, 3, 36, 7, 17, 31, 6, 24, 35, 20, 15, 17, 15, 5, 22, 34, 36, 37, 9, 3, 50, 13, 46, 43, 34, 12, 45, 40, 24, 36, 45, 9, 41, 30, 15, 9, 10, 23, 32, 46, 44, 48]) == 795)
#print(BuildingHeightsEasy().minimum(12, [25, 18, 38, 1, 42, 41, 14, 16, 19, 46, 42, 39, 38, 31, 43, 37, 26, 41, 33, 37, 45, 27, 19, 24, 33, 11, 22, 20, 36, 4, 4]) == 47);
#print(BuildingHeightsEasy().minimum(3, {19, 23, 9, 12}) == 15);