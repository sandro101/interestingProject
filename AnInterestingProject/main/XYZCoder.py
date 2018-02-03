class XYZCoder:
    def countWays(self, room, size):
        if room == 1: return 1
        if size == 1: return room   
        #how many non-repeating rooms can be generated 
        #and then for them how many variations are there of that room (facotrial(room))      
        2x2[1,2], [1,3],               [2,1], [3,1]
        2x3[1,2], [1,3], [1,4],        [2,1], [3,1], [4,1]
        2x4[1,2], [1,3], [1,4], [1,5], [2,1], [3,1], [4,1], [5,1]
        
        3x2[1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5]#first room has 1, second room 
        3x3[1,2,3], [1,2,4], [1,2,5], [1,4,7]#first room has 1, second room 
        #Max last room can have is: room * size - size + 1
        #min last room can have is: max - room + 1
        #combinations = max - min + 1 = room
        #Max second to last room can have is: max1 - size
        #Min second to last room can have is: max2 - size
        #combinations size - 1
        
        #room1 size 3
        #1 (1)
        
        #room 2 size 3
        #1, 4
        #1, 3
        #1, 2 (3)
        
        #room 3 size 1                 
        #1, 2, 3 (1)
        
        #room 3 size 2
        #1, 3, 5
        #1, 3, 4(2)
        #1, 2, 5
        #1, 2, 4
        #1, 2, 3(3) 
        
        #0, 2, 3
        
        #room 3 size 3
        #1, 4, 7
        #1, 4, 6
        #1, 4, 5 (3)
        #1, 3, 7
        #1, 3, 6
        #1, 3, 5
        #1, 3, 4 (4)
        #1, 2, 7
        #1, 2, 6
        #1, 2, 5
        #1, 2, 4
        #1, 2, 3 (5) 
        
        #starts with a 3 because it is size 3, has 5 because 7 - 2 = 5
        
        #3: 1
        #4: 2
        #5: 3
        #6: 3
        #7: 3
        
        #0, 3, 5
        
        #room 4 size 3  
        #1, 4, 7, 10
        #1, 4, 7, 9  
        #1, 4, 7, 8  (3)
        #1, 4, 6, 10 
        #1, 4, 6, 9
        #1, 4, 6, 8 
        #1, 4, 6, 7  (4) 
        #1, 4, 5, 10 
        #1, 4, 5, 9
        #1, 4, 5, 8 
        #1, 4, 5, 7   
        #1, 4, 5, 6  (5)                   
        #1, 3, 7, 10 
        #1, 3, 7, 9
        #1, 3, 7, 8  (3)
        
        
        
        #
        
           
        
        
        #each time size increases add on an extra number

        return -1    
    
print(XYZCoder().countWays(1, 2) == 1);    
print(XYZCoder().countWays(2, 1) == 2);
print(XYZCoder().countWays(2, 2) == 4);
print(XYZCoder().countWays(2, 3) == 4);
