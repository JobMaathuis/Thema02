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
    global GUANINE, ADENINE, CYTOSINE, URACIL_ONE, ADENINE_TWO

    GUANINE = pdb.PDBMolecule('{}/pdb/GMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    ADENINE = pdb.PDBMolecule('{}/pdb/AMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    CYTOSINE = pdb.PDBMolecule('{}/pdb/CMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    URACIL_ONE = pdb.PDBMolecule('{}/pdb/UMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    ADENINE_TWO = pdb.PDBMolecule('{}/pdb/AMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])


def create_first_part(step_in_frame, two_fifth_of_animation):

    ADENINE.rotate([1, 0, 0], pi + pi / 3)
    ADENINE_TWO.rotate([1, 0, 0], pi + pi / 3)
    GUANINE.rotate([0, 1, 1], [0, pi / 2 + pi / 3, pi / 2])


    URACIL_ONE.move_to([-5, -20, 0])
    ADENINE.move_to([0, -10, 0])
    ADENINE_TWO.move_to([-4.5, -6, 5])
    GUANINE.move_to([-10, 4, 10])
    CYTOSINE.move_to([-15, 20, 0])


def frame(step):
    """ """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    # obtain molecules from function
    create_molecules()

    # Creation of RNA molecule
    step_in_frame = step
    two_fifth_of_animation = n_frames // 5 * 2

    if step in range(0, two_fifth_of_animation):
        create_first_part(step_in_frame, two_fifth_of_animation)


    # Return the Scene object for rendering
    return Scene(Camera('location', [0, 0, -50], 'look_at', [0, 0, 0]),
                 objects=[models.default_light] + URACIL_ONE.povray_molecule + ADENINE.povray_molecule
                 + ADENINE_TWO.povray_molecule + GUANINE.povray_molecule + CYTOSINE.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame, range(39, 40))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
