from pypovray import pypovray, pdb, models, SETTINGS
from vapory.vapory import Scene, LightSource, Text, Texture, Pigment, Finish, Camera


def frame(step):
    global RNA

    RNA = pdb.PDBMolecule('{}/pdb/RNA2.pdb'.format(SETTINGS.AppLocation), offset=[-100, 0, 0])
    RNA.rotate([0, 1, 1], [0, 3.14, 3.14])
    if step < 15:
        RNA.move_to([0, 0, 0])


    return Scene(Camera('location', [0, 0, -50], 'look_at', [0, 0, 0]),
                 objects=[models.default_light] + RNA.povray_molecule)


if __name__ == '__main__':
    pypovray.render_scene_to_mp4(frame, range(0, 1))
