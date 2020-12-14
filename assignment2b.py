#!/usr/bin/env python3

"""
Renders a shape which consists out of a sphere and multiple boxes and cones.
It also renders the legend, which is imported from a different program.
"""

__author__ = "Joukje Kloosterman, Job Maathuis"

from pypovray import pypovray
from vapory import Sphere, Box, Cone, Texture, Pigment, Finish, LightSource, Scene, Camera
from assignment2a import legend


def make_sphere(x1, y1, z1, x2, y2, z2):
    """ Creates a pink sphere with a radius of 3"""
    sphere = Sphere([x1, y1, z1], 3, Texture(Pigment('color', [x2, y2, z2]), Finish('reflection', 0.4)))
    return sphere


def make_box(x1, y1, z1, x2, y2, z2):
    """ Creates a blue box or rectangle"""
    rectangle = Box([x1, y1, z1], [x2, y2, z2], Texture(Pigment('color', [0, 1, 1]), Finish('reflection', 0.4)))
    return rectangle


def make_cone(x1, y1, z1, x2, y2, z2):
    """ Creates a pink cone with a base-radius of 3"""
    cone = Cone([x1, y1, z1], 3, [x2, y2, z2], 0, Texture(Pigment('color', [1, 0, 1]), Finish('reflection', 0.4)))
    return cone


def frame(step):
    """ Creates the objects and places this in a scene """
    # Creates a sphere
    sphere = make_sphere(0, 0, 0, 1, 0, 1)
    # Creates the rectangles
    rectangle_right = make_box(3, -6, -4, 5, 6, 2)
    rectangle_top = make_box(3, 6, -4, -3, 4, 2)
    rectangle_left = make_box(-3, -6, -4, -5, 6, 2)
    rectangle_bottom = make_box(-3, -4, -4, 3, -6, 2)
    # Creates the cones
    cone_top = make_cone(0, 6, 0, 0, 10, 0)
    cone_left = make_cone(-5, 0, 0, -9, 0, 0)
    cone_right = make_cone(5, 0, 0, 9, 0, 0)
    cone_bottom = make_cone(0, -6, 0, 0, -10, 0)
    # Return the Scene object for rendering
    xyz_legend = legend([-15, 0, 0], 5)
    return Scene(Camera('location', [0, 10, -35], 'look_at', [0, 2, -2]),
                 objects=[LightSource([2, 8, -20], 2), sphere, rectangle_right, rectangle_top, rectangle_left,
                          rectangle_bottom, cone_top, cone_left, cone_right, cone_bottom] + xyz_legend)


if __name__ == '__main__':
    # Render as an image
    pypovray.render_scene_to_png(frame)
