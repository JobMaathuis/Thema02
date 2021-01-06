#!/usr/bin/env python3
"""

    usage:
        python3 assignment3.py
"""

__author__ = "Joukje Kloosterman"

import sys
from math import sin
from pypovray import pypovray, SETTINGS, models, logger
from vapory import Sphere, Scene


def frame(step):
    """ Returns the scene at step number (1 step per frame) """
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Getting the total number of frames, see the configuration file
    nframes = eval(SETTINGS.NumberFrames)

    x_start = -10
    x_end = 10

    distance_x = x_end - x_start

    distance_per_frame_x = (distance_x / nframes) * 2

    x_coord = x_start + step * distance_per_frame_x
    y_coord = sin(x_coord)

    sphere = (Sphere([x_coord, y_coord, 0], 3, models.default_sphere_model))
    return Scene(models.default_camera,
                 objects=[sphere, models.default_ground, models.default_light])


def main(args):
    """ Main function performing the rendering """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))

    pypovray.render_scene_to_mp4(frame)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
