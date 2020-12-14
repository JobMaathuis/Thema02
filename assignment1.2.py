# !/usr/bin/env python3

from pypovray import pypovray, models
from vapory import Sphere, Box, Cone, Scene, Pigment


def frame(step):
    ''' Creates a sphere, boxes and cones and places it all in a scene '''
    colour_purple = Pigment('color', [1, 0, 1, ])
    colour_aquamarine = Pigment('color', [0, 1, 1], )
    sphere = Sphere([0, 0, 0], 4, colour_purple)
    side_box_1 = Box([4, -7, -4], [5.5, 7, 4], colour_aquamarine, )
    side_box_2 = Box([-4, -7, -4], [-5.5, 7, 4], colour_aquamarine, )
    side_box_3 = Box([5.5, 5.5, -4], [-5.5, 7, 4], colour_aquamarine, )
    side_box_4 = Box([5.5, -5.5, -4], [-5.5, -7, 4], colour_aquamarine, )
    cone_1 = Cone([0, 7, 0], 3.5, [0, 11, 0], 0, colour_purple)
    cone_2 = Cone([0, -7, 0], 3.5, [0, -11, 0], 0, colour_purple)
    cone_3 = Cone([5.5, 0, ], 3.5, [9.5, 0, ], 0, colour_purple)
    cone_4 = Cone([-5.5, 0, 0], 3.5, [-9.5, 0, 0], 0, colour_purple)
    # Return the Scene object for rendering
    return Scene(models.default_camera,
                 objects=[models.default_light, side_box_1, side_box_2, side_box_3, side_box_4,
                          cone_1, cone_2, cone_3, cone_4, sphere])


if __name__ == '__main__':
    # Render as an image
    pypovray.render_scene_to_png(frame)
