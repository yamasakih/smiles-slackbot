from slackbot.bot import respond_to
from slackbot.utils import download_file, create_tmp_file
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from rdkit.Chem.Draw.rdMolDraw2D import MolDraw2DSVG

haggle_bot_name = "smiles"


@respond_to('^( ?.*$)')
def convert_smiles(message, smiles):
    mol = Chem.MolFromSmiles(smiles.strip())
    if not mol:
        message.reply('smilesキーが正しくない可能性があります。')
    else:
        test_smiles = Chem.MolToSmiles(mol)
        test_molecule = Chem.MolFromSmiles(test_smiles)

        AllChem.Compute2DCoords(mol)
        #image = Draw.MolToImage(mol, size=(200, 200))

        drawer = MolDraw2DSVG(200, 200)
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        #canvas = drawer.GetDrawingText()
        svg = drawer.GetDrawingText()

        fw = open('test.svg', 'w')
        fw.write(svg)
        fw.close()

        message.channel.upload_file('%s.svg' % smiles, 'test.svg')

        """
        with create_tmp_file() as tmpf:
            #image.save(tmpf, 'PNG')
            #message.channel.upload_file('%s.png' % smiles, tmpf)

            fw = open(tmpf, 'w')
            fw.write(svg)
            message.channel.upload_file('%s.svg' % smiles, tmpf)
            fw.close()
        """
