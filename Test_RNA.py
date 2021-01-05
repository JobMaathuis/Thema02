from pypovray import pypovray, pdb, models, SETTINGS
from vapory.vapory import Scene, LightSource, Text, Texture, Pigment, Finish, Camera


def frame(step):
    global NUCL_1, NUCL_2, NUCL_3, NUCL_4, NUCL_5, NUCL_6, NUCL_7

    RNA = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    # RNA.show_label(camera=models.default_camera, name=True)
    RNA.rotate([0, 1, 1], [0, 3.14, 3.14])

    nucleotide_atoms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    NUCL_1 = RNA.divide(nucleotide_atoms, 'nucleotide_1')
    NUCL_2 = RNA.divide(nucleotide_atoms, 'nucleotide_2')
    NUCL_3 = RNA.divide(nucleotide_atoms, 'nucleotide_3')
    NUCL_4 = RNA.divide(nucleotide_atoms, 'nucleotide_4')
    NUCL_5 = RNA.divide(nucleotide_atoms, 'nucleotide_5')
    NUCL_6 = RNA.divide(nucleotide_atoms, 'nucleotide_6')
    NUCL_7 = RNA.divide(nucleotide_atoms, 'nucleotide_7')


    if step < 15:
        RNA.move_to([0, 0, 0])


    return Scene(Camera('location', [0, 0, -50], 'look_at', [0, 0, 0]),
                 objects=[models.default_light] + NUCL_1.povray_molecule + NUCL_4.povray_molecule)


if __name__ == '__main__':
    pypovray.render_scene_to_mp4(frame, range(0, 1))
