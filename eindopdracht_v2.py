# !/usr/bin/env python3

"""

"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from assignment2a import legend
from math import pi
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene, Camera

NUCL_1 = NUCL_2 = NUCL_3 = NUCL_4 = NUCL_5 = NUCL_6 = NUCL_7 = None


def create_molecules():
    """ Creates the molecules """
    global NUCL_1, NUCL_2, NUCL_3, NUCL_4, NUCL_5, NUCL_6, NUCL_7

    rna = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    # RNA.show_label(camera=models.default_camera, name=True)
    rna.rotate([0, 1, 1], [0, 3.14, 3.14])

    nucleotide_atoms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    NUCL_1 = rna.divide(nucleotide_atoms, 'nucleotide_1', offset=[-50, 0, 0])
    NUCL_2 = rna.divide(nucleotide_atoms, 'nucleotide_2', offset=[-50, 0, 0])
    NUCL_3 = rna.divide(nucleotide_atoms, 'nucleotide_3', offset=[-50, 0, 0])
    NUCL_4 = rna.divide(nucleotide_atoms, 'nucleotide_4', offset=[-50, 0, 0])
    NUCL_5 = rna.divide(nucleotide_atoms, 'nucleotide_5', offset=[-50, 0, 0])
    NUCL_6 = rna.divide(nucleotide_atoms, 'nucleotide_6', offset=[-50, 0, 0])
    NUCL_7 = rna.divide(nucleotide_atoms, 'nucleotide_7', offset=[-50, 0, 0])


def create_first_part(step_in_frame, two_fifth_of_animation):
    """ """
    one_sixth_of_scene = two_fifth_of_animation // 5
    two_sixth_of_scene = one_sixth_of_scene * 2
    three_sixth_of_scene = one_sixth_of_scene * 3
    four_sixth_of_scene = one_sixth_of_scene * 4
    five_sixth_of_scene = one_sixth_of_scene * 5

    distance = 50
    distance_per_frame = distance / one_sixth_of_scene

    if step_in_frame in range(0, one_sixth_of_scene):
        x_offset = step_in_frame * distance_per_frame - distance
        print(x_offset)
        NUCL_1.move_offset([x_offset, 0, 0])

    if step_in_frame in range(one_sixth_of_scene, two_sixth_of_scene):
        step_in_scene = step_in_frame - one_sixth_of_scene
        x_offset = step_in_scene * distance_per_frame - distance
        NUCL_1.move_offset([distance, 0, 0])
        NUCL_2.move_offset([x_offset, 0, 0])



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


    # # Sphere covering the RNA molecule
    # if step in range(n_frames // 5 * 2, n_frames // 5 * 3):
    #
    # # RNA division
    # if step in range(n_frames // 5 * 3, n_frames // 5 * 4):
    #
    # # Sphere division
    # if step in range(n_frames // 5 * 4, n_frames):

    # Return the Scene object for rendering
    return Scene(Camera('location', [0, 0, -50], 'look_at', [0, 0, 0]),
                 objects=[models.default_light] + NUCL_1.povray_molecule + NUCL_2.povray_molecule +
                 NUCL_3.povray_molecule + NUCL_4.povray_molecule + NUCL_5.povray_molecule +
                NUCL_6.povray_molecule + NUCL_7.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame, range(0, 10))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
