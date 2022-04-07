import numpy as np

class Boat():
    
    def __init__(self, boat_location):
        self.boat_location = boat_location

    def get_angle(self):
        dx = self.boat_location[0]
        dy = self.boat_location[1]
        angle = [np.arctan2(dx,dy), round( np.degrees( np.arctan2(dx,dy) ) % 360, 1) ]
        return angle
    
    def display_boat_angle(self):
        dx = self.boat_location[0]
        dy = self.boat_location[1]
        angle = [np.arctan2(dx,dy), np.degrees( np.arctan2(dx,dy) ) % 360]
        print("Location: ", end = "")
        print(self.boat_location)
        print("     Radian: ",end="")
        print(angle[0])
        print("     Degree: ",end="")
        print(angle[1])