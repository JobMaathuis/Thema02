#!/usr/bin/env python3

"""
Renders a left-handed 3D-coordinate system, als known as a legend
"""

__author__ = "Job Maathuis"

from pypovray import pypovray, models
from vapory import Cylinder, Cone, Texture, Pigment, Finish, LightSource, Scene, Camera


def frame(step):
    """ Creates the objects and places this in a scene """
    # Creates the lines in each directions
    x_cylinder = Cylinder([-15, 0, 0], [-10, 0, 0], 0.1, Texture(Pigment('color', [1, 0, 0]), Finish('reflection', 1)))
    y_cylinder = Cylinder([-15, 0, 0], [-15, 5, 0], 0.1, Texture(Pigment('color', [0, 0, 1]), Finish('reflection', 1)))
    z_cylinder = Cylinder([-15, 0, 0], [-15, 0, 5], 0.1, Texture(Pigment('color', [0, 1, 0]), Finish('reflection', 1)))
    # Creates the arrows of each directions
    x_cone = Cone([-10, 0, 0], 0.3, [-9, 0, 0], 0, Texture(Pigment('color', [1, 0, 0]), Finish('reflection', 1)))
    y_cone = Cone([-15, 5, 0], 0.3, [-15, 6, 0], 0, Texture(Pigment('color', [0, 0, 1]), Finish('reflection', 1)))
    z_cone = Cone([-15, 0, 5], 0.3, [-15, 0, 6], 0, Texture(Pigment('color', [0, 1, 0]), Finish('reflection', 1)))
    # Return the Scene object for rendering
    return Scene(models.default_camera,
                 objects=[LightSource([2, 8, -20], 2), x_cylinder, y_cylinder, z_cylinder, x_cone, y_cone, z_cone])


if __name__ == '__main__':
    # Render as an image
    pypovray.render_scene_to_png(frame)
