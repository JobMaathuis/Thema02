# !/usr/bin/env python3

"""

"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from math import pi
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene, Camera


def create_molecules():
    """ Creates the molecules """
    global GUANINE, ADENINE

    GUANINE = pdb.PDBMolecule('{}/pdb/GMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    ADENINE = pdb.PDBMolecule('{}/pdb/AMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])


def frame(step):
    """ """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    full_circle = 2 * pi  # One full circle equals exactly 2 times pi

    # obtain molecules from function
    create_molecules()
    new_molecule = pdb(pdb=None, atoms= GUANINE , ADENINE)
    print(new_molecule)

    # Creation of RNA molecule
    step_in_frame = step
    two_fifth_of_animation = n_frames // 5 * 2

    # if step in range(0, two_fifth_of_animation):

    # return Scene(Camera('location', [0, 8, -50], 'look_at', [0, 2, -5]),
    #              objects=[models.default_light] + ADENINE.povray_molecule + GUANINE.povray_molecule

def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame, range(39, 40))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
