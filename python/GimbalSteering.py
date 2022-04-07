from Boat import Boat
import numpy as np

class GimbalSteering():

    def __init__(self, boat_location, camera_location = [0,0], camera_fov = 80):
        self.boat_location = boat_location
        self.camera_location = camera_location
        self.camera_fov = camera_fov
        
        if camera_location != [0,0]:
            self.boat_location = []
            for i in boat_location:
                x_temp = i[0] - self.camera_location[0]
                y_temp = i[1] - self.camera_location[1]
                self.boat_location.append([x_temp, y_temp])
        
        if camera_fov < 0:
            self.camera_fov = abs(self.camera_fov)
        elif camera_fov > 360:
            self.camera_fov = 360
        elif camera_fov == 0:
            self.camera_fov = 1

    def get_angle_between_two_vectors(self, a, b):
        angle = round (np.degrees( np.arccos( np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)) )), 1)
        return angle

        
    def get_capture_angles(self):

        if len(self.boat_location) == 0:
            return []
        elif self.camera_fov >= 360:
            return [0.0]

        unique_location = []
        for location in self.boat_location:
            temp = Boat(location).get_angle()[1]
            if temp not in unique_location:
                unique_location.append( temp )
        unique_location.sort()

        capture_angle = unique_location

        for i, val in enumerate(unique_location):
            new_list = [val]
            pivot = val
            if i > 0:
                for j in range(i+1, len(unique_location)):
                    if abs(unique_location[j] - pivot) >= self.camera_fov:
                        new_list.append(unique_location[j])
                        pivot = unique_location[j]
                for j in range(0, i):
                    if abs(pivot - unique_location[j]) > 180:
                        if abs(360 - pivot + unique_location[j]) >= self.camera_fov:
                        # if abs(unique_location[j] - pivot) >= self.camera_fov:
                            new_list.append(unique_location[j])
                            pivot = unique_location[j]
                    else:
                        new_list.append(unique_location[j])
                        pivot = unique_location[j]
            else:
                for j in range (i+1, len(unique_location)):
                    if abs(unique_location[j] - pivot) >= self.camera_fov:
                        new_list.append(unique_location[j])
                        pivot = unique_location[j]
        
            if len(new_list) < len(capture_angle):
                capture_angle = new_list
        return capture_angle
