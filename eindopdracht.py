# !/usr/bin/env python3

"""

"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from math import pi
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene


def create_molecules():
    """ Creates the molecules """
    global GUANINE

    GUANINE = pdb.PDBMolecule('{}/pdb/gtp.pdb'.format(SETTINGS.AppLocation), center=True)
    GUANINE.rotate([1, 1, 1], [pi * 1.5, pi, pi / 2])
    GUANINE.divide([11, 12, 13, 14, 15, 16, 17, 18], 'phosphate',
                         offset=[0, 0, 0])  # removes two phosphate groups to create guanine nucleotide


def frame(step):
    """ Renders an animation in which the molecules are split
    and rotate one full circle around its axis """

    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    full_circle = 2 * pi  # One full circle equals exactly 2 times pi

    # obtain molecules from function
    create_molecules()

    # Creation of RNA molecule
    if step in range(0, n_frames // 5 * 2):

    # Sphere covering the RNA molecule
    if step in range(n_frames // 5 * 2, n_frames // 5 * 3):

    # RNA division
    if step in range(n_frames // 5 * 3, n_frames // 5 * 4):

    # Sphere division
    if step in range(n_frames // 5 * 4, n_frames):

    # Return the Scene object for rendering
    return Scene(models.floor_camera,
                 objects=[models.default_light] + GUANINE.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
