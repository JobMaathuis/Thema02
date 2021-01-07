# !/usr/bin/env python3

"""

"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from assignment2a import legend
from math import pi, sin, cos
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene, Camera, Sphere, Texture, Pigment, Finish

# NUCL_1 = NUCL_2 = NUCL_3 = NUCL_4 = NUCL_5 = NUCL_6 = NUCL_7 = None


def create_molecules():
    """ Creates the molecules """
    global NUCL_1, NUCL_2, NUCL_3, NUCL_4, NUCL_5, NUCL_6, NUCL_7, RNA

    RNA = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation)) #, offset=[-100, 0, 0])
    # RNA.show_label(camera=models.default_camera, name=True)
    RNA.rotate([0, 1, 1], [0, pi, pi])

    nucleotide_atoms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    NUCL_1 = RNA.divide(nucleotide_atoms, 'nucleotide_1', offset=[-50, 0, 0])
    NUCL_2 = RNA.divide(nucleotide_atoms, 'nucleotide_2', offset=[-50, 0, 0])
    NUCL_3 = RNA.divide(nucleotide_atoms, 'nucleotide_3', offset=[-50, 0, 0])
    NUCL_4 = RNA.divide(nucleotide_atoms, 'nucleotide_4', offset=[-50, 0, 0])
    NUCL_5 = RNA.divide(nucleotide_atoms, 'nucleotide_5', offset=[-50, 0, 0])
    NUCL_6 = RNA.divide(nucleotide_atoms, 'nucleotide_6', offset=[-50, 0, 0])
    NUCL_7 = RNA.divide(nucleotide_atoms, 'nucleotide_7', offset=[-50, 0, 0])


def create_first_part(step_in_frame, two_fifth_of_animation):
    """ """
    one_sixth_of_scene = two_fifth_of_animation // 5
    two_sixth_of_scene = one_sixth_of_scene * 2
    three_sixth_of_scene = one_sixth_of_scene * 3
    four_sixth_of_scene = one_sixth_of_scene * 4
    five_sixth_of_scene = one_sixth_of_scene * 5

    distance = 100
    distance_per_frame = distance / one_sixth_of_scene

    if step_in_frame in range(0, one_sixth_of_scene):
        x_offset = step_in_frame * distance_per_frame - distance / 2
        NUCL_1.move_offset([x_offset, 0, 0])

    if step_in_frame in range(one_sixth_of_scene, two_sixth_of_scene):
        step_in_scene = step_in_frame - one_sixth_of_scene
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([x_offset, 0, 0])
        NUCL_3.move_offset([x_offset, 0, 0])

    if step_in_frame in range(two_sixth_of_scene, three_sixth_of_scene):
        step_in_scene = step_in_frame - two_sixth_of_scene
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([x_offset, 0, 0])

    if step_in_frame in range(three_sixth_of_scene, four_sixth_of_scene):
        step_in_scene = step_in_frame - three_sixth_of_scene
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([50, 0, 0])
        NUCL_5.move_offset([x_offset, 0, 0])

    if step_in_frame in range(four_sixth_of_scene, five_sixth_of_scene):
        step_in_scene = step_in_frame - four_sixth_of_scene
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([50, 0, 0])
        NUCL_5.move_offset([50, 0, 0])
        NUCL_6.move_offset([x_offset, 0, 0])
        NUCL_7.move_offset([x_offset, 0, 0])


def create_second_part(step_in_frame, three_fifth_of_animation):




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

    step_in_frame = step
    two_fifth_of_animation = n_frames // 5 * 2
    three_fifth_of_animation = n_frames // 5 * 3

    VESICLE = Sphere([100, 0, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                              Finish('phong', 0.4, 'reflection', 0.2)))

    camera_z = -100
    # Creation of RNA molecule
    if step in range(0, two_fifth_of_animation):
        create_first_part(step_in_frame, two_fifth_of_animation + 1)

    # Sphere covering the RNA molecule
    if step in range(two_fifth_of_animation, three_fifth_of_animation + 1):
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([50, 0, 0])
        NUCL_5.move_offset([50, 0, 0])
        NUCL_6.move_offset([50, 0, 0])
        NUCL_7.move_offset([50, 0, 0])

        step_in_frame = step - two_fifth_of_animation
        x_start = 100
        x_end = -50

        distance_x = x_end - x_start
        distance_per_frame_x = (distance_x / three_fifth_of_animation) * 2

        x_coord = x_start + step_in_frame * distance_per_frame_x
        y_coord = 2 * sin(x_coord/5)
        print(y_coord)

        VESICLE = Sphere([x_coord, y_coord, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                            Finish('phong', 0.4, 'reflection', 0.2)))


    # Vesicle growth
    if step in range(n_frames // 5 * 3, n_frames // 5 * 4 + 1):
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([50, 0, 0])
        NUCL_5.move_offset([50, 0, 0])
        NUCL_6.move_offset([50, 0, 0])
        NUCL_7.move_offset([50, 0, 0])
        VESICLE = Sphere([0, 0, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                            Finish('phong', 0.4, 'reflection', 0.2)))
        # camere movement
        if step in range(n_frames // 5 * 3, n_frames // 5 * 4 // 2):
            camera_z_start = -100
            camera_z_end = -150
            distance_camera_z = camera_z_end - camera_z_start
            z_camera_coord = step_in_frame * distance_per_frame - camera_z_start
    # # Sphere division
    # if step in range(n_frames // 5 * 4, n_frames):

    # Return the Scene object for rendering
    return Scene(Camera('location', [0, 0, camera_z], 'look_at', [0, 0, 0]),
                 objects=[models.default_light, VESICLE] + NUCL_1.povray_molecule + NUCL_2.povray_molecule +
                 NUCL_3.povray_molecule + NUCL_4.povray_molecule + NUCL_5.povray_molecule +
                         NUCL_6.povray_molecule + NUCL_7.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame, range(74, 75))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
