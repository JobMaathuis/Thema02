#!/usr/bin/env python3

"""
Makes an animation of a sphere making a seesaw wave using Povray.
usage: python3 assignment3.py
"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from pypovray import pypovray, SETTINGS, models, logger
from vapory import Sphere, Scene, Cone


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
    arrow = Cone(x_coord, 0.3, y_coord, 0, models.default_sphere_model)

    # Returns the objects of the scene using the default camera settings
    return Scene(models.default_camera,
                 objects=[arrow, models.default_ground, models.default_light])


def main(args):
    """ Main function to preform this render. """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

# !/usr/bin/env python3

"""

"""

__author__ = "Job Maathuis"

import sys
from math import pi
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene


def create_molecules():
    """ Creates molecules and contains other constants """
    global ETHANOL

    ETHANOL = pdb.PDBMolecule('{}/pdb/ethanol.pdb'.format(SETTINGS.AppLocation), center=True)


def frame(step):
    """ Renders an ATP molecule centered in the scene """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    # Calculates distance per frame for the to be splitted molecule parts
    x_start = 0
    x_end = 8
    x_distance = x_end - x_start
    x_distance_per_frame = (x_distance / (n_frames / 2))

    # Variables used for rotating of molecules
    full_circle = 2 * pi  # One full circle equals exactly 2 times pi
    rotation_per_frame = full_circle / (n_frames/2)

    # creating the nucleotide
    gtp = pdb.PDBMolecule('{}/pdb/gtp.pdb'.format(SETTINGS.AppLocation), center=True)
    gtp.rotate([1, 1, 1], [pi * 1.5, pi, pi/2])

    gtp.divide([11, 12, 13, 14, 15, 16, 17, 18],
               'phosphate', offset=[0, 0, 0])  # removes two phosphate groups to create guanine nucleotide
    guanine = gtp.divide([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 34, 35],
                         'base', offset=[4, 0, 0])  # splits into ribose-phosphate and the gaunine base

    # In the first half of the animation: split the guanine nucleotide into guanine and ribose-phosphate
    if step in range(0, n_frames//2):
        gtp.move_to([-step * x_distance_per_frame, 0, 0])
        guanine.move_to([step * x_distance_per_frame, 0, 0])

    # In the second half of the animation: rotate both molecules one full circle
    if step in range(n_frames//2, n_frames):
        gtp.rotate([0, 1, 0], rotation_per_frame * (step - (n_frames/2)))
        guanine.rotate([1, 0, 0], rotation_per_frame * (step - (n_frames/2)))
        gtp.move_to([-n_frames//2 * x_distance_per_frame, 0, 0])
        guanine.move_to([n_frames//2 * x_distance_per_frame, 0, 0])

    # Return the Scene object for rendering
    return Scene(models.floor_camera,
                 objects=[models.default_light] + gtp.povray_molecule + guanine.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
