from GimbalSteering import GimbalSteering 

def main(list_of_boats, camera_location, camera_fov):
    my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
    return my_gimbal.get_capture_angles()

if __name__ == "__main__":
    camera_location = [0, 0]
    camera_fov = 80
    list_of_boats = [
                        # Prompt input locations
                        [+3, +2],
                        [+6, +4],
                        [+4, -1],
                        [+8, -2],
                        [-1, +4],
                        [-1, +2],
                        [-4, +1]

                        # [-0.5, +1],
                        # [+0.5, +1]

                        # [0, 1],
                        # [1, 1],
                        # [1, 0],
                        # [1, -1],
                        # [0, -1],
                        # [-1, -1],
                        # [-1, 0],
                        # [-1, 1]
                    ]

    capture_angles = main(list_of_boats, camera_location, camera_fov)
    print( "There are", len(capture_angles), "captured angles:", capture_angles )