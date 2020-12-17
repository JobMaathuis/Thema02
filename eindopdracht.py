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
    global GUANINE, ADENINE, CYTOSINE, URACIL_ONE, URACIL_TWO

    GUANINE = pdb.PDBMolecule('{}/pdb/GMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    ADENINE = pdb.PDBMolecule('{}/pdb/AMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    CYTOSINE = pdb.PDBMolecule('{}/pdb/CMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    URACIL_ONE = pdb.PDBMolecule('{}/pdb/UMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    URACIL_TWO = pdb.PDBMolecule('{}/pdb/UMP.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])


def create_first_part(step_in_frame, two_fifth_of_animation):
    """ """
    one_sixth_of_scene = two_fifth_of_animation // 6
    two_sixth_of_scene = one_sixth_of_scene * 2
    three_sixth_of_scene = one_sixth_of_scene * 3
    four_sixth_of_scene = one_sixth_of_scene * 4
    five_sixth_of_scene = one_sixth_of_scene * 5
    six_sixth_of_scene = two_fifth_of_animation

    start = 30
    end = 0

    distance = start - end
    distance_per_frame = distance / one_sixth_of_scene

    if step_in_frame in range(0, one_sixth_of_scene):
        uracil_x_location = step_in_frame * distance_per_frame - start
        URACIL_ONE.move_to([uracil_x_location, -20, 0])

    if step_in_frame in range(one_sixth_of_scene, two_sixth_of_scene):
        step_in_scene = step_in_frame - one_sixth_of_scene
        adenine_x_location = step_in_scene * distance_per_frame - start
        URACIL_ONE.move_to([end, -20, 0])
        ADENINE.move_to([adenine_x_location, -10, 0])

    if step_in_frame in range(two_sixth_of_scene, three_sixth_of_scene):
        step_in_scene = step_in_frame - two_sixth_of_scene
        uracil_x_location = step_in_scene * distance_per_frame - start
        URACIL_ONE.move_to([end, -20, 0])
        ADENINE.move_to([end, -10, 0])
        URACIL_TWO.move_to([uracil_x_location, 0, 0])

    if step_in_frame in range(three_sixth_of_scene, four_sixth_of_scene):
        step_in_scene = step_in_frame - three_sixth_of_scene
        guanine_x_location = step_in_scene * distance_per_frame - start
        URACIL_ONE.move_to([end, -20, 0])
        ADENINE.move_to([end, -10, 0])
        URACIL_TWO.move_to([end, 0, 0])
        GUANINE.move_to([guanine_x_location, 10, 0])

    if step_in_frame in range(four_sixth_of_scene, five_sixth_of_scene):
        step_in_scene = step_in_frame - four_sixth_of_scene
        cytosine_x_location = step_in_scene * distance_per_frame - start
        URACIL_ONE.move_to([end, -20, 0])
        ADENINE.move_to([end, -10, 0])
        URACIL_TWO.move_to([end, 0, 0])
        GUANINE.move_to([end, 10, 0])
        CYTOSINE.move_to([cytosine_x_location, 20, 0])



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

    # Creation of RNA molecule
    step_in_frame = step
    two_fifth_of_animation = n_frames // 5 * 2

    if step in range(0, two_fifth_of_animation):
        create_first_part(step_in_frame, two_fifth_of_animation)
        # ADENINE.move_to([-10, 0, 0])



    # # Sphere covering the RNA molecule
    # if step in range(n_frames // 5 * 2, n_frames // 5 * 3):
    #
    # # RNA division
    # if step in range(n_frames // 5 * 3, n_frames // 5 * 4):
    #
    # # Sphere division
    # if step in range(n_frames // 5 * 4, n_frames):

    # Return the Scene object for rendering
    return Scene(Camera('location', [0, 8, -50], 'look_at', [0, 2, -5]),
                 objects=[models.default_light] + URACIL_ONE.povray_molecule + ADENINE.povray_molecule
                 + URACIL_TWO.povray_molecule + GUANINE.povray_molecule + CYTOSINE.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame, range(0, 40))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
