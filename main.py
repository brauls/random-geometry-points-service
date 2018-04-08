from random_geometry_points import circle2d

circle = circle2d.Circle2D(1.0, 2.5, 10)
points = circle.create_random_points(5)

print(points)