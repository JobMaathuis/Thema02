# !/usr/bin/env python3

"""

"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
import random
from math import pi, sin, cos
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene, Camera, Sphere, Texture, Pigment, Finish

# NUCL_1 = NUCL_2 = NUCL_3 = NUCL_4 = NUCL_5 = NUCL_6 = NUCL_7 = None


def create_molecules():
    """ Creates the molecules """
    global NUCL_1, NUCL_2, NUCL_3, NUCL_4, NUCL_5, NUCL_6, NUCL_7, RNA_2, RNA_1

    RNA_1 = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation))
    RNA_1.rotate([0, 1, 1], [0, pi, pi])

    RNA_2 = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation))
    RNA_2.rotate([0, 1, 1], [0, pi, pi])

    rna_to_nucl = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation)) #, offset=[-100, 0, 0])
    # RNA.show_label(camera=models.default_camera, name=True)
    rna_to_nucl.rotate([0, 1, 1], [0, pi, pi])

    nucleotide_atoms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    NUCL_1 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_1', offset=[-50, 0, 0])
    NUCL_2 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_2', offset=[-50, 0, 0])
    NUCL_3 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_3', offset=[-50, 0, 0])
    NUCL_4 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_4', offset=[-50, 0, 0])
    NUCL_5 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_5', offset=[-50, 0, 0])
    NUCL_6 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_6', offset=[-50, 0, 0])
    NUCL_7 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_7', offset=[-50, 0, 0])


def create_first_part(step_in_frame, two_fifth_of_animation):
    """ """
    part_in_scene = [two_fifth_of_animation // 5 * part_of_scene for part_of_scene in range(1, 6)]

    distance = 100
    distance_per_frame = distance / part_in_scene[0]

    if step_in_frame in range(0, part_in_scene[0]):
        x_offset = step_in_frame * distance_per_frame - distance / 2
        NUCL_1.move_offset([x_offset, 0, 0])

    if step_in_frame in range(part_in_scene[0], part_in_scene[1]):
        step_in_scene = step_in_frame - part_in_scene[0]
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([x_offset, 0, 0])
        NUCL_3.move_offset([x_offset, 0, 0])

    if step_in_frame in range(part_in_scene[1], part_in_scene[2]):
        step_in_scene = step_in_frame - part_in_scene[1]
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([x_offset, 0, 0])

    if step_in_frame in range(part_in_scene[2], part_in_scene[3]):
        step_in_scene = step_in_frame - part_in_scene[2]
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([50, 0, 0])
        NUCL_5.move_offset([x_offset, 0, 0])

    if step_in_frame in range(part_in_scene[3], part_in_scene[4]):
        step_in_scene = step_in_frame - part_in_scene[3]
        x_offset = step_in_scene * distance_per_frame - distance / 2
        NUCL_1.move_offset([50, 0, 0])
        NUCL_2.move_offset([50, 0, 0])
        NUCL_3.move_offset([50, 0, 0])
        NUCL_4.move_offset([50, 0, 0])
        NUCL_5.move_offset([50, 0, 0])
        NUCL_6.move_offset([x_offset, 0, 0])
        NUCL_7.move_offset([x_offset, 0, 0])


def create_second_part(step_in_frame, two_fifth_of_animation, three_fifth_of_animation):
    NUCL_1.move_offset([50, 0, 0])
    NUCL_2.move_offset([50, 0, 0])
    NUCL_3.move_offset([50, 0, 0])
    NUCL_4.move_offset([50, 0, 0])
    NUCL_5.move_offset([50, 0, 0])
    NUCL_6.move_offset([50, 0, 0])
    NUCL_7.move_offset([50, 0, 0])

    step_in_scene = step_in_frame - (two_fifth_of_animation + 1)
    x_start = 100
    x_end = -50

    distance_x = x_end - x_start
    distance_per_frame_x = (distance_x / three_fifth_of_animation) * 2

    x_coord = x_start + step_in_scene * distance_per_frame_x
    y_coord = 2 * sin(x_coord / 5)


    vesicle = Sphere([x_coord, y_coord, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                        Finish('phong', 0.4, 'reflection', 0.2)))

    return vesicle


def create_third_part(step_in_frame, three_fifth_of_animation, four_fifth_of_animation):
    NUCL_1.move_offset([50, 0, 0])
    NUCL_2.move_offset([50, 0, 0])
    NUCL_3.move_offset([50, 0, 0])
    NUCL_4.move_offset([50, 0, 0])
    NUCL_5.move_offset([50, 0, 0])
    NUCL_6.move_offset([50, 0, 0])
    NUCL_7.move_offset([50, 0, 0])

    small_vesicle_1 = Sphere([120, 0, 0], 3, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                          Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_2 = Sphere([120, 0, 0], 5, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                         Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_3 = Sphere([120, 0, 0], 2, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_4 = Sphere([120, 0, 0], 4, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_5 = Sphere([120, 0, 0], 5, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))

    total_frames = four_fifth_of_animation - three_fifth_of_animation
    step_in_scene = step_in_frame - three_fifth_of_animation

    z_start = -100
    z_end = -150
    z_coord = -150
    radius = 20

    end_coord = 20
    start_coord = 120
    distance = start_coord - end_coord
    distance_per_frame = distance / (total_frames // 5)

    if step_in_scene in range(0, total_frames // 5):
        distance_z = z_end - z_start
        distance_per_frame_z = distance_z / (total_frames // 5)
        z_coord = z_start + step_in_scene * distance_per_frame_z

    if step_in_scene in range(total_frames // 5, total_frames // 5 * 2):
        part_in_scene = step_in_scene - (total_frames // 5)
        x_coord = start_coord - distance_per_frame * part_in_scene
        small_vesicle_1 = Sphere([-x_coord, sin(x_coord/3), 0], 3, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                            Finish('phong', 0.4, 'reflection', 0.2)))
        small_vesicle_2 = Sphere([x_coord, cos(x_coord/3), 0], 5, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                            Finish('phong', 0.4, 'reflection', 0.2)))

    if step_in_scene in range(total_frames // 5 * 2, total_frames // 5 * 3):
        part_in_scene = step_in_scene - (total_frames // 5 * 2)
        radius_increase = 10
        radius_increase_per_frame = part_in_scene * radius_increase / (total_frames // 5)
        radius += radius_increase_per_frame

    if step_in_scene in range(total_frames // 5 * 3, total_frames // 5 * 4):
        part_in_scene = step_in_scene - (total_frames // 5 * 3)
        x_coord = start_coord - distance_per_frame * part_in_scene
        radius = 30
        small_vesicle_3 = Sphere([x_coord, sin(x_coord/3), 0], 2,
                         Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6), Finish('phong', 0.4, 'reflection', 0.2)))
        small_vesicle_4 = Sphere([sin(x_coord/3), x_coord, 0], 4,
                         Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6), Finish('phong', 0.4, 'reflection', 0.2)))
        small_vesicle_5 = Sphere([sin(x_coord/3), -x_coord, 0], 5,
                         Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6), Finish('phong', 0.4, 'reflection', 0.2)))

    if step_in_scene in range(total_frames // 5 * 4, total_frames):
        radius = 30
        part_in_scene = step_in_scene - (total_frames // 5 * 4)
        radius_increase = 10
        radius_increase_per_frame = part_in_scene * radius_increase / (total_frames // 5)
        radius += radius_increase_per_frame


    vesicle = Sphere([0, 0, 0], radius, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                            Finish('phong', 0.4, 'reflection', 0.2)))

    return vesicle, z_coord, small_vesicle_1, small_vesicle_2, small_vesicle_3, small_vesicle_4, small_vesicle_5


def create_fourth_part(step_in_frame, four_fifth_of_animation, n_frames):
    """ """
    NUCL_1.move_offset([500, 0, 0])
    NUCL_2.move_offset([500, 0, 0])
    NUCL_3.move_offset([500, 0, 0])
    NUCL_4.move_offset([500, 0, 0])
    NUCL_5.move_offset([500, 0, 0])
    NUCL_6.move_offset([500, 0, 0])
    NUCL_7.move_offset([500, 0, 0])
    vesicle = Sphere([0, 0, 0], 40, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                            Finish('phong', 0.4, 'reflection', 0.2)))
    vesicle_2 = Sphere([200, 0, 0], 40, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                            Finish('phong', 0.4, 'reflection', 0.2)))

    total_frames = n_frames - four_fifth_of_animation
    step_in_scene = step_in_frame - four_fifth_of_animation

    end_coord = 20
    start_coord = 0
    distance = start_coord - end_coord
    distance_per_frame = distance / (total_frames // 5 * 2)

    radius = 40
    radius_decrease = 20

    if step_in_scene in range(0, total_frames // 5 * 2):
        x_coord = start_coord + step_in_scene * distance_per_frame

        RNA_1.move_to([-x_coord, 0, 0])
        RNA_2.move_to([x_coord, 0, 0])

    if step_in_scene in range(total_frames // 5 * 2, total_frames // 5 * 4):
        part_in_scene = step_in_scene - (total_frames // 5 * 2)
        radius_decrease_per_frame = part_in_scene * radius_decrease / (total_frames // 2)
        radius -= radius_decrease_per_frame
        x_coord = start_coord - distance_per_frame * part_in_scene

        vesicle = Sphere([x_coord, 0, 0], radius, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                Finish('phong', 0.4, 'reflection', 0.2)))
        vesicle_2 = Sphere([-x_coord, 0, 0], radius, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                    Finish('phong', 0.4, 'reflection', 0.2)))

        RNA_1.move_to([-end_coord, 0, 0])
        RNA_2.move_to([end_coord, 0, 0])

    if step_in_scene in range(total_frames // 5 * 4, total_frames):
        part_in_scene = step_in_scene - (total_frames // 5 * 4)

        end_coord = 30
        start_coord = 20
        distance = start_coord - end_coord
        distance_per_frame = distance / (total_frames // 5)
        x_coord = start_coord - distance_per_frame * part_in_scene

        vesicle = Sphere([x_coord, 0, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                          Finish('phong', 0.4, 'reflection', 0.2)))
        vesicle_2 = Sphere([-x_coord, 0, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                             Finish('phong', 0.4, 'reflection', 0.2)))
        RNA_1.move_to([-x_coord, 0, 0])
        RNA_2.move_to([x_coord, 0, 0])

    return vesicle, vesicle_2


def frame(step):
    """ """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames
    n_frames = eval(SETTINGS.NumberFrames)

    # obtain molecules from function
    create_molecules()

    step_in_frame = step
    one_fifth_of_animation = n_frames // 5
    two_fifth_of_animation = n_frames // 5 * 2
    three_fifth_of_animation = n_frames // 5 * 3
    four_fifth_of_animation = n_frames // 5 * 4

    camera_z = -100

    small_vesicle_1 = Sphere([120, 0, 0], 3, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_2 = Sphere([120, 0, 0], 5, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_3 = Sphere([120, 0, 0], 2, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_4 = Sphere([120, 0, 0], 4, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))
    small_vesicle_5 = Sphere([120, 0, 0], 5, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                     Finish('phong', 0.4, 'reflection', 0.2)))
    vesicle = Sphere([120, 0, 0], 5, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                             Finish('phong', 0.4, 'reflection', 0.2)))
    vesicle_2 = Sphere([200, 0, 0], 40, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                Finish('phong', 0.4, 'reflection', 0.2)))

    RNA_1.move_to([500, 0, 0])
    RNA_2.move_to([500, 0, 0])
    # Creation of RNA molecule
    if step in range(0, two_fifth_of_animation):
        vesicle = Sphere([100, 0, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                  Finish('phong', 0.4, 'reflection', 0.2)))
        create_first_part(step_in_frame, two_fifth_of_animation)

    # Sphere covering the RNA molecule
    if step in range(two_fifth_of_animation, three_fifth_of_animation):
        vesicle = create_second_part(step_in_frame, two_fifth_of_animation, three_fifth_of_animation)

    # Vesicle growth
    if step in range(three_fifth_of_animation, four_fifth_of_animation):
        vesicle, camera_z, small_vesicle_1, small_vesicle_2, small_vesicle_3, \
        small_vesicle_4, small_vesicle_5 = create_third_part(step_in_frame, three_fifth_of_animation, four_fifth_of_animation)

    if step in range(n_frames // 5 * 4, n_frames):
        vesicle, vesicle_2 = create_fourth_part(step_in_frame, four_fifth_of_animation, n_frames)

    # Return the Scene object for rendering
    return Scene(Camera('location', [0, 0, camera_z], 'look_at', [0, 0, 0]),
                 objects=[models.default_light, vesicle, vesicle_2, small_vesicle_1, small_vesicle_2, small_vesicle_3, small_vesicle_4, small_vesicle_5] + NUCL_1.povray_molecule + NUCL_2.povray_molecule +
                 NUCL_3.povray_molecule + NUCL_4.povray_molecule + NUCL_5.povray_molecule +
                         NUCL_6.povray_molecule + NUCL_7.povray_molecule + RNA_1.povray_molecule + RNA_2.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
