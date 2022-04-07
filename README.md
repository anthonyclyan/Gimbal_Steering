# Gimbal Steering

## Problem statement

Let's take photos, efficiently! <br />
Imagine you're on a boat and there are other boats around you that you are interested in capturing an image of. The goal is to capture each boat at least once with the least number of images. <br />
So... <br />
Given you own location - camera location, the camera field of view, and the other boats location represented in [x, y] coordinate, output the **least** number of captures and their **respective angle** with respect to you.

### Example
Given:
- Camera location: `[0, 0]`
- Camera FOV: `80` degree
- 5 boats location: `[ [3, 2], [4, -1], [-1, 4], [-1, 2], [-4, 1] ]`

The inefficient way is to take 5 phots, one per each boat and we don't want that.
An efficient way is to only take 2 photos, 
1. `[ [3, 2], [4, -1] ]` with capture angle `56.3` degree
2. `[ [-1, 4], [-1, 2], [-4, 1] ]` with capture angle `284` degree


## My approach

### Design 

1. What are the objects?
2. What are their attributes?
3. What are their behaviors?
4. What are their collections? Or how are they grouped?
5. How do they interact?
6. What is the deveoplment schedule?

### Objects

1. Boats
2. SteeringAngles

### Attributes

1. of a boat
    - location: x, y

2. of a steering angles
    - has at least the same number of boats

### Behaviors

1. Boats
    - calculate location: angle [rad]
    - do not include if angle already covered

2. SteeringAngles
    - group boats according to location angle
    - return angles with least number of captures

### How are they grouped?

- Group boats if the angle difference between the two locations <= camera FOV

### How do they interact?

- Gimbal Steering ensure there are no "duplicate" boats lying in the same angle
