#!/usr/bin/env python3

"""
Makes an animation of a sphere making a seesaw wave using Povray.
usage: python3 assignment3.py
"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from pypovray import pypovray, SETTINGS, models, logger
from vapory import Sphere, Scene


def frame(step):
    """ Returns a scene at a step number in which a sphere is visualised. """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    # Calculate the frames per wave
    repeats = 5
    n_frames_wave = n_frames / repeats  # amount of frames per wave

    # Calculates starting coordinates of the sphere
    increase = 4  # amount of increase per wave
    x_start = -10
    x_end = x_start + increase
    y_start = -4
    y_end = 4

    # Calculates total distance and distance per frame
    x_distance = x_end - x_start
    y_distance = y_end - y_start
    x_distance_per_frame = (x_distance / (n_frames_wave / 2))
    y_distance_per_frame = (y_distance / (n_frames_wave / 2))

    # Determine in which wave this step is
    if step // n_frames_wave == 0:
        wave = 0
    else:
        wave = step // n_frames_wave

    # Step has to reset for every wave, so subtract frames of previous wave(s)
    frame_in_wave = step - (wave * n_frames_wave)

    # If it is in the first part of the wave
    if frame_in_wave <= (n_frames_wave / 2):
        x_coord = x_start + (wave * increase) + frame_in_wave * x_distance_per_frame  # Increases linear
        y_coord = y_start + frame_in_wave * y_distance_per_frame  # Increases linear
    # Second part of the wave
    else:
        x_coord = x_end + (wave * increase)  # Stays constant and increases 4 for every wave
        y_coord = y_end - (frame_in_wave - (n_frames_wave / 2)) * y_distance_per_frame  # Decreases linear

    # Makes a sphere at given x- and Y-coordinates with the default style
    sphere = Sphere([x_coord, y_coord, 0], 0.5, models.default_sphere_model)

    # Returns the objects of the scene using the default camera settings
    return Scene(models.default_camera,
                 objects=[sphere, models.default_ground, models.default_light])


def main(args):
    """ Main function to preform this render. """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
