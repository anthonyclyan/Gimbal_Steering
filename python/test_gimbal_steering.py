import unittest
from GimbalSteering import GimbalSteering

class TestGimbalSteering (unittest.TestCase):

    def test_GimbalSteering_case_01 (self):
        camera_location = [0, 0]
        camera_fov = 80
        list_of_boats = [
                            # Prompt input locations
                            [+3, +2],
                            [+4, -1],
                            [-1, +4],
                            [-1, +2],
                            [-4, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [56.3, 284.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_02 (self):
        camera_location = [0, 0]
        camera_fov = 80
        list_of_boats = [
                            # More location with same angle
                            [+3, +2],
                            [+6, +4],
                            [+4, -1],
                            [+8, -2],
                            [-1, +4],
                            [-1, +2],
                            [-4, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [56.3, 284.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_03 (self):
        camera_location = [0, 0]
        camera_fov = 360    # Changed camera FOV
        list_of_boats = [
                            [+3, +2],
                            [+6, +4],
                            [+4, -1],
                            [+8, -2],
                            [-1, +4],
                            [-1, +2],
                            [-4, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [0.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_04 (self):
        camera_location = [0, 0]
        camera_fov = 80
        list_of_boats = [
                            # Check same angle
                            [1, 1],
                            [2, 2],
                            [3, 3],
                            [4, 4]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [45.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_05 (self):
        camera_location = [0, 0]
        camera_fov = 80
        list_of_boats = [
                            # Prompt input locations
                            [+0, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [0.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_06 (self):
        camera_location = [0, 0]
        camera_fov = 80
        list_of_boats = [
                            [0, 1],     # 0
                            [1, 1],     # 45
                            [1, 0],     # 90
                            [1, -1],    # 135
                            [0, -1],    # 180
                            [-1, -1],   # 225
                            [-1, 0],    # 270
                            [-1, 1]     # 315
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [0.0, 90.0, 180.0, 270.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_07 (self):
        camera_location = [0, 0]
        camera_fov = 0      # Camera FOV become 1 if input == 0
        list_of_boats = [
                            [+0, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [0.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_08 (self):
        camera_location = [0, 2]    # Changed camera_location
        camera_fov = 80
        list_of_boats = [
                            [+0, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [180.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_09 (self):
        camera_location = [1, 0]
        camera_fov = 80
        list_of_boats = [
                            [+0, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [315.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_10 (self):
        # Ommit certain input
        list_of_boats = [
                            [+0, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats)
        result = my_gimbal.get_capture_angles()
        expected = [0.0]
        self.assertEqual(result, expected)

    def test_GimbalSteering_case_11 (self):
        camera_location = [0, 0]
        camera_fov = 1
        list_of_boats = [
                            [+3, +2],
                            [+6, +4],
                            [+4, -1],
                            [-1, +4],
                            [-1, +2],
                            [-4, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [56.3, 104.0, 284.0, 333.4, 346.0]
        self.assertEqual(result, expected)
    
    def test_GimbalSteering_case_11 (self):
        camera_location = [0, 0]
        camera_fov = 80
        list_of_boats = [
                            [-0.5, +1],
                            [+0.5, +1]
                        ]
        my_gimbal = GimbalSteering(list_of_boats, camera_location, camera_fov)
        result = my_gimbal.get_capture_angles()
        expected = [333.4]
        self.assertEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main()