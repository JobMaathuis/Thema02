#!/usr/bin/env python3

"""
Makes an animation in which a camera moves around objects using Povray
usage: python3 assignment4.py
"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from math import sin, cos, pi
from pypovray import pypovray, SETTINGS, models, logger
from vapory import Sphere, Scene, Cylinder, LightSource, Camera
from assignment2a import legend


def make_objects():
    global SPHERE, CYLINDER, LEGEND

    SPHERE = Sphere([6, 2, -2], 3, models.default_sphere_model)
    CYLINDER = Cylinder([-6, -1, 4], [-6, 7, 4], 3, models.default_sphere_model)
    LEGEND = legend([-15, 0, 0], 5)


def frame(step):
    """ Returns a scene at a step number while camera is moving """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    # Calculates coordinates for the camera position
    radius = 25
    degrees = pi / (n_frames / 2) * (step + 1)
    x_coord = radius * sin(degrees)
    z_coord = radius * cos(degrees)

    # Returns the objects of the scene using the default camera settings
    return Scene(Camera('location', [x_coord, 8, z_coord], 'look_at', [0, 0, 0]),
                 objects=[LightSource([2, 8, -20], 2),
                          models.checkered_ground] + SPHERE + CYLINDER + LEGEND)


def main(args):
    """ Main function of this program """
    make_objects()
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
