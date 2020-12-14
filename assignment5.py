# !/usr/bin/env python3

"""
Makes an animation in which the nucleotide guanine is split into ribose-phosphate and
the guanine base. In the second half of the animation the two molecules rotate one full
circle around its axis.
usage: python3 assignment5.py
"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from math import pi
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene


def create_molecules():
    """ Creates the molecules """
    global GTP, GUANINE

    GTP = pdb.PDBMolecule('{}/pdb/gtp.pdb'.format(SETTINGS.AppLocation), center=True)
    GTP.rotate([1, 1, 1], [pi * 1.5, pi, pi / 2])
    GTP.divide([11, 12, 13, 14, 15, 16, 17, 18], 'phosphate',
               offset=[0, 0, 0])  # removes two phosphate groups to create guanine nucleotide
    GUANINE = GTP.divide([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 34, 35], 'guanine',
                         offset=[4, 0, 0])  # splits into ribose-phosphate and the guanine base


def frame(step):
    """ Renders an animation in which the molecules are split
    and rotate one full circle around its axis """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    # Calculates distance per frame for the two molecules
    x_start = 0
    x_end = 8
    x_distance = x_end - x_start
    x_distance_per_frame = (x_distance / (n_frames / 2))

    # Variables used for rotating of molecules
    full_circle = 2 * pi  # One full circle equals exactly 2 times pi
    rotation_per_frame = full_circle / (n_frames/2)

    # obtain molecules from function
    create_molecules()

    # In the 1st half of animation: split the guanine nucleotide into guanine and ribose-phosphate
    if step in range(0, n_frames//2):
        GTP.move_to([-step * x_distance_per_frame, 0, 0])
        GUANINE.move_to([step * x_distance_per_frame, 0, 0])

    # In the 2nd half of animation: rotate both molecules one full circle
    if step in range(n_frames//2, n_frames):
        GTP.rotate([0, 1, 0], rotation_per_frame * (step - (n_frames/2)))
        GUANINE.rotate([1, 0, 0], rotation_per_frame * (step - (n_frames/2)))
        GTP.move_to([-n_frames//2 * x_distance_per_frame, 0, 0])
        GUANINE.move_to([n_frames//2 * x_distance_per_frame, 0, 0])

    # Return the Scene object for rendering
    return Scene(models.floor_camera,
                 objects=[models.default_light] + GTP.povray_molecule + GUANINE.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
