from pypovray import pypovray, pdb, models, SETTINGS
from vapory.vapory import Scene, LightSource, Text, Texture, Pigment, Finish, Camera


def frame(step):
    global LIPID

    LIPID = pdb.PDBMolecule('{}/pdb/lipid_test.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    # RNA.show_label(camera=models.default_camera, name=True)
    # RNA.rotate([0, 1, 1], [0, 3.14, 3.14])

    if step < 15:
        LIPID.move_to([0, 0, 0])


    return Scene(Camera('location', [0, 0, -350], 'look_at', [0, 0, 0]),
                 objects=[models.default_light] + LIPID.povray_molecule)


if __name__ == '__main__':
    pypovray.render_scene_to_mp4(frame, range(0, 1))
