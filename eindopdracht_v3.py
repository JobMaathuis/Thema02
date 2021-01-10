# !/usr/bin/env python3

"""

"""

__author__ = 'Joukje Kloosterman, Job Maathuis'

import sys
from math import pi, sin, cos
from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene, Camera, Sphere, Texture, Pigment, Finish


def create_molecules():
    """ Creates the molecules """
    global NUCL_1, NUCL_2, NUCL_3, NUCL_4, NUCL_5, NUCL_6, NUCL_7, RNA_2, RNA_1

    # Create first RNA molecule
    RNA_1 = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation))
    RNA_1.rotate([0, 1, 1], [0, pi, pi])

    # Create second RNA molecule
    RNA_2 = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation))
    RNA_2.rotate([0, 1, 1], [0, pi, pi])

    # Create RNA molecule for the making of nucleotides
    rna_to_nucl = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation))
    rna_to_nucl.rotate([0, 1, 1], [0, pi, pi])

    # Determine which atoms make the nucelotides
    nucleotide_atoms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                        13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                        24, 25, 26, 27, 28, 29, 30, 31]

    # Creating all the different molecules
    NUCL_1 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_1', offset=[-70, 0, 0])
    NUCL_2 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_2', offset=[-70, 0, 0])
    NUCL_3 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_3', offset=[-70, 0, 0])
    NUCL_4 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_4', offset=[-70, 0, 0])
    NUCL_5 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_5', offset=[-70, 0, 0])
    NUCL_6 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_6', offset=[-70, 0, 0])
    NUCL_7 = rna_to_nucl.divide(nucleotide_atoms, 'nucleotide_7', offset=[-70, 0, 0])


def create_first_part_of_animation(frame_number, thirty_percent_of_total_frames):
    """
    In this function nucleotides move into the scene creating a RNA molecule.
    """
    # Determine total frames of the first part of the animation
    total_frames_of_first_part = thirty_percent_of_total_frames - 0

    # Dividing the total frames of this segment into fifths
    one_fifth_of_part = total_frames_of_first_part // 5
    two_fifth_of_part = total_frames_of_first_part // 5 * 2
    three_fifth_of_part = total_frames_of_first_part // 5 * 3
    four_fifth_of_part = total_frames_of_first_part // 5 * 4

    # The end x offset for nucleotides
    end_x_offset = 70

    # Calculating the distance per frame for moving the nucleotides
    distance = 70
    distance_per_frame = distance / one_fifth_of_part

    # In the first segment of this part the first nucleotide moves into the scene
    if frame_number in range(0, one_fifth_of_part):
        x_offset = frame_number * distance_per_frame
        NUCL_1.move_offset([x_offset, 0, 0])

    # In the second segment the next two nucleotides move into the scene
    elif frame_number in range(one_fifth_of_part, two_fifth_of_part):
        step_in_segment= frame_number - one_fifth_of_part
        x_offset =  step_in_segment * distance_per_frame
        NUCL_1.move_offset([end_x_offset, 0, 0])
        NUCL_2.move_offset([x_offset, 0, 0])
        NUCL_3.move_offset([x_offset, 0, 0])

    # In the third segment the next nucleotide moves into the scene
    elif frame_number in range(two_fifth_of_part, three_fifth_of_part):
        step_in_segment = frame_number - two_fifth_of_part
        x_offset = step_in_segment * distance_per_frame
        NUCL_1.move_offset([end_x_offset, 0, 0])
        NUCL_2.move_offset([end_x_offset, 0, 0])
        NUCL_3.move_offset([end_x_offset, 0, 0])
        NUCL_4.move_offset([x_offset, 0, 0])

    # In the fourth segment the next nucleotide moves into the scene
    elif frame_number in range(three_fifth_of_part, four_fifth_of_part):
        step_in_segment = frame_number - three_fifth_of_part
        x_offset = step_in_segment * distance_per_frame
        NUCL_1.move_offset([end_x_offset, 0, 0])
        NUCL_2.move_offset([end_x_offset, 0, 0])
        NUCL_3.move_offset([end_x_offset, 0, 0])
        NUCL_4.move_offset([end_x_offset, 0, 0])
        NUCL_5.move_offset([x_offset, 0, 0])

    # In the last segment the last two nucleotides move into the scene
    elif frame_number in range(four_fifth_of_part, total_frames_of_first_part):
        step_in_segment = frame_number - four_fifth_of_part
        x_offset = step_in_segment * distance_per_frame
        NUCL_1.move_offset([end_x_offset, 0, 0])
        NUCL_2.move_offset([end_x_offset, 0, 0])
        NUCL_3.move_offset([end_x_offset, 0, 0])
        NUCL_4.move_offset([end_x_offset, 0, 0])
        NUCL_5.move_offset([end_x_offset, 0, 0])
        NUCL_6.move_offset([x_offset, 0, 0])
        NUCL_7.move_offset([x_offset, 0, 0])


def create_second_part_of_animation(frame_number, thirty_percent_of_total_frames, fifty_percent_of_total_frames):
    """
    In this function the whole RNA molecule is placed in the center of the scene and
    a sphere is moved over the molecule as a vesicle.
    """
    # Determine total frames of the second part of the animation
    total_frames_second_part = fifty_percent_of_total_frames - thirty_percent_of_total_frames

    # Determine in which step of the second part we are, starting with zero
    step_in_part = frame_number - (thirty_percent_of_total_frames + 1)

    # Place whole RNA molecule in the center of the scene
    RNA_1.move_to([0, 0, 0])

    # Determine the starting and ending x-coordinate of the vesicle
    x_start = 100
    x_end = 0

    # Calculating the distance per frame that the vesicle has to cover
    distance_x = x_end - x_start
    distance_per_frame_x = (distance_x / total_frames_second_part)

    # Calculating the x and y coordinates per frame according to the sine function
    x_coord = x_start + step_in_part * distance_per_frame_x
    y_coord = 2 * sin(x_coord / 5)

    # Making the vesicle with a sphere and placing it at the created x and y coordinates
    vesicle = Sphere([x_coord, y_coord, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                        Finish('phong', 0.4, 'reflection', 0.2)))

    return vesicle


def create_third_part_of_the_animation(frame_number, fifty_percent_of_total_frames, eighty_percent_of_total_frames):
    """
    In this function a RNA moleucle is placed in the center of the scene.
    The vesicle (a Sphere object) is placed over the molecule.
    Smaller vesicles move towards the big vesicle and makes the radius of the big vesicle larger.
    """
    # Place whole RNA molecule in the center of the scene
    RNA_1.move_to([0, 0, 0])

    # Creating the smaller vesicles and place them out of the scene
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

    # Determine total frames of second part
    total_frames_of_third_part = eighty_percent_of_total_frames - fifty_percent_of_total_frames

    # Determine in which step of the second part we are, starting with zero
    step_in_part = frame_number - (fifty_percent_of_total_frames + 1)

    # Dividing the frames of this part into fifths
    one_fifth_of_part = total_frames_of_third_part // 5
    two_fifth_of_part = total_frames_of_third_part // 5 * 2
    three_fifth_of_part = total_frames_of_third_part // 5 * 3
    four_fifth_of_part = total_frames_of_third_part // 5 * 4

    # Default variables: z coordinates for camera and radius for vesicle
    z_coord_camera = -150
    radius_vesicle = 20

    # Start and end coordinates for zooming out with camera
    z_start_camera = -100
    z_end_camera = -150

    # Calculating distance per frame for zooming out with the camera
    distance_z = z_end_camera - z_start_camera
    distance_per_frame_z = distance_z / one_fifth_of_part

    # Calculating the increase of the radius per frame
    radius_increase = 10
    radius_increase_per_frame = radius_increase / (total_frames_of_third_part // 5)

    # Start and end coordinates for smaller vesicles
    end_coord = 20
    start_coord = 120

    # Calculating distance per frame to cover for smaller vesicles
    distance = start_coord - end_coord
    distance_per_frame = distance / one_fifth_of_part

    # In first segment of this part the camera is zooming out
    if step_in_part in range(0, one_fifth_of_part):
        z_coord_camera = z_start_camera + step_in_part * distance_per_frame_z

    # In the second segment two small vesicles move towards the big vesicle
    elif step_in_part in range(one_fifth_of_part, two_fifth_of_part):
        step_in_segment = step_in_part - one_fifth_of_part
        x_coord = start_coord - distance_per_frame * step_in_segment
        small_vesicle_1 = Sphere([-x_coord, sin(x_coord/3), 0], 3, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                            Finish('phong', 0.4, 'reflection', 0.2)))
        small_vesicle_2 = Sphere([x_coord, cos(x_coord/3), 0], 5, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                            Finish('phong', 0.4, 'reflection', 0.2)))

    # In the third segment the radius of the big vesicle is increased
    elif step_in_part in range(two_fifth_of_part, three_fifth_of_part):
        step_in_segment = step_in_part - two_fifth_of_part
        radius_vesicle += radius_increase_per_frame * step_in_segment

    # In the fourth segment three small vesicles move towards the bigger vesicle
    elif step_in_part in range(three_fifth_of_part, four_fifth_of_part):
        step_in_segment = step_in_part - three_fifth_of_part
        x_coord = start_coord - distance_per_frame * step_in_segment
        radius_vesicle = 30
        small_vesicle_3 = Sphere([x_coord, sin(x_coord/3), 0], 2,
                         Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6), Finish('phong', 0.4, 'reflection', 0.2)))
        small_vesicle_4 = Sphere([sin(x_coord/3), x_coord, 0], 4,
                         Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6), Finish('phong', 0.4, 'reflection', 0.2)))
        small_vesicle_5 = Sphere([sin(x_coord/3), -x_coord, 0], 5,
                         Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6), Finish('phong', 0.4, 'reflection', 0.2)))

    # In the last segment the radius of the bigger vesicle is increased
    elif step_in_part in range(four_fifth_of_part, total_frames_of_third_part):
        radius_vesicle = 30
        part_in_scene = step_in_part - four_fifth_of_part
        radius_vesicle += radius_increase_per_frame * part_in_scene

    # Making the big vesicle (as a Sphere object) with its newly given radius
    vesicle = Sphere([0, 0, 0], radius_vesicle, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                            Finish('phong', 0.4, 'reflection', 0.2)))

    return vesicle, z_coord_camera, small_vesicle_1, small_vesicle_2, small_vesicle_3, small_vesicle_4, small_vesicle_5


def create_fourth_part_of_the_animation(frame_number, eighty_percent_of_animation, total_frames):
    """
    In this function a RNA-molecule is replicated, then the vesicle (as a Sphere object) is
    separated into two smaller vesicles, each vesicle containing a RNA-molecule.
    After that both cells/vesicles move in opposite directions.
    """
    # Place whole RNA molecule in the center of the scene
    RNA_1.move_to([0, 0, 0])

    # Create vesicle (placed in center of scene) and a duplicate (placed out of scene)
    vesicle = Sphere([0, 0, 0], 40, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                            Finish('phong', 0.4, 'reflection', 0.2)))
    vesicle_2 = Sphere([200, 0, 0], 40, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                            Finish('phong', 0.4, 'reflection', 0.2)))

    # Determining the total frames of the fourth part
    total_frames_of_fourth_part = total_frames - eighty_percent_of_animation

    # Determine in which step of the second part we are, starting with zero
    step_in_part = frame_number - (eighty_percent_of_animation + 1)

    # Dividing the frames of this part into fifths that are necessary
    one_fifth_of_part = total_frames_of_fourth_part // 5
    two_fifth_of_part = total_frames_of_fourth_part // 5 * 2
    four_fifth_of_part = total_frames_of_fourth_part // 5 * 4

    # Camera z-coordinate
    camera_z = -150

    # Determining the start and end coordinates of both RNA molecules
    end_coord_rna_split = 20
    start_coord_rna_split = 0

    # Calculating the distance per frame for moving both RNA molecules
    distance_rna_molecule = start_coord_rna_split - end_coord_rna_split
    distance_rna_molecule_per_frame = distance_rna_molecule / two_fifth_of_part

    # Determining the start and end coordinates of both cells
    end_coord_cell = 30
    start_coord_cell = 20

    # Calculating the distance per frame for moving both cells
    distance_cell = start_coord_cell - end_coord_cell
    distance_cell_per_frame = distance_cell / one_fifth_of_part

    # Default variable for radius of vesicle (as a Sphere object)
    radius = 40

    # Calculating the decrease of the radius per frame
    radius_decrease = 20
    radius_decrease_per_frame = radius_decrease / two_fifth_of_part

    # In the first segment of this part the RNA-molecule is split into two molecules
    if step_in_part in range(0, two_fifth_of_part):
        x_coord = start_coord_rna_split + step_in_part * distance_rna_molecule_per_frame
        RNA_1.move_to([-x_coord, 0, 0])
        RNA_2.move_to([x_coord, 0, 0])

    # In the third segment the vesicle is split into two, and both radius are decreased
    elif step_in_part in range(two_fifth_of_part, four_fifth_of_part):
        step_in_segment = step_in_part - two_fifth_of_part
        radius -= radius_decrease_per_frame * step_in_segment
        x_coord = start_coord_rna_split - distance_rna_molecule_per_frame * step_in_segment
        vesicle = Sphere([x_coord, 0, 0], radius, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                Finish('phong', 0.4, 'reflection', 0.2)))
        vesicle_2 = Sphere([-x_coord, 0, 0], radius, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                    Finish('phong', 0.4, 'reflection', 0.2)))
        RNA_1.move_to([-end_coord_rna_split, 0, 0])
        RNA_2.move_to([end_coord_rna_split, 0, 0])

    # In the last segment the vesicles with the RNA inside are moving apart
    elif step_in_part in range(four_fifth_of_part, total_frames_of_fourth_part):
        step_in_segment = step_in_part - four_fifth_of_part
        x_coord = start_coord_cell - distance_cell_per_frame * step_in_segment

        vesicle = Sphere([x_coord, 0, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                          Finish('phong', 0.4, 'reflection', 0.2)))
        vesicle_2 = Sphere([-x_coord, 0, 0], 20, Texture(Pigment('color', [0.7, 1, 1], 'filter', 0.6),
                                                             Finish('phong', 0.4, 'reflection', 0.2)))
        RNA_1.move_to([-x_coord, 0, 0])
        RNA_2.move_to([x_coord, 0, 0])

    return vesicle, vesicle_2, camera_z


def frame(step):
    """ """
    # Feedback to user in terminal about render status
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    # Calculates the total frames of animation
    total_frames = eval(SETTINGS.NumberFrames)

    # Calculating the percentages that are necessary, each represent a part of the animation
    thirty_percent_of_total_frames = total_frames // 10 * 3
    fifty_percent_of_total_frames = total_frames // 2
    eighty_percent_of_total_frames = total_frames // 5 * 4

    # Obtain molecules from function
    create_molecules()

    # Initializing different sizes of vesicles out of scene
    small_vesicle_1 = Sphere([120, 0, 0], 3)
    small_vesicle_2 = Sphere([120, 0, 0], 5)
    small_vesicle_3 = Sphere([120, 0, 0], 2)
    small_vesicle_4 = Sphere([120, 0, 0], 4)
    small_vesicle_5 = Sphere([120, 0, 0], 5)
    vesicle = Sphere([120, 0, 0], 5)
    vesicle_2 = Sphere([200, 0, 0], 40)

    # Initializing two RNA molecules out of scene
    RNA_1.move_to([500, 0, 0])
    RNA_2.move_to([500, 0, 0])

    # Default z-coordinate for camera
    camera_z = -100

    # Creation of RNA molecule in the first thirty percent of the animation
    if step in range(0, thirty_percent_of_total_frames):
        create_first_part_of_animation(step, thirty_percent_of_total_frames)

    # Sphere covering the RNA molecule in the next twenty percent of the animation
    elif step in range(thirty_percent_of_total_frames, fifty_percent_of_total_frames):
        vesicle = create_second_part_of_animation(step, thirty_percent_of_total_frames, fifty_percent_of_total_frames)

    # Vesicle growing in the next thirty percent of the animation
    elif step in range(fifty_percent_of_total_frames, eighty_percent_of_total_frames):
        vesicle, camera_z, small_vesicle_1, small_vesicle_2, small_vesicle_3, \
        small_vesicle_4, small_vesicle_5 = create_third_part_of_the_animation(step, fifty_percent_of_total_frames, eighty_percent_of_total_frames)

    # Replicating the RNA-molecule and the vesicle, becoming two individual cells with RNA
    elif step in range(eighty_percent_of_total_frames, total_frames):
        vesicle, vesicle_2, camera_z = create_fourth_part_of_the_animation(step, eighty_percent_of_total_frames, total_frames)

    # Return the Scene object for rendering
    return Scene(Camera('location', [0, 0, camera_z], 'look_at', [0, 0, 0]),
                 objects=[models.default_light, vesicle, vesicle_2, small_vesicle_1, small_vesicle_2,
                          small_vesicle_3, small_vesicle_4, small_vesicle_5] + NUCL_1.povray_molecule +
                         NUCL_2.povray_molecule + NUCL_3.povray_molecule + NUCL_4.povray_molecule +
                         NUCL_5.povray_molecule + NUCL_6.povray_molecule + NUCL_7.povray_molecule +
                         RNA_1.povray_molecule + RNA_2.povray_molecule)


def main(args):
    """ Main function of this program """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
