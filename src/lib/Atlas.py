########################################################
# Atlas.py
# Xristos Dosis
# August 6, 2022
#
# Atlas class is responsible for parsing .atlas files
# and storing texture regions from a single image to
# JSDictionary(s), avoiding multiple texture loads
# form multiple images.
#
# .atlas files have a JSON like structure with only
# one level (for now) stored for category.
########################################################

from json import load
from os import sep
from os.path import join, dirname
from src.lib.jsDictionary import JSDictionary

CoreImage = None

class Atlas:

    def __init__(self, src_path):
        if not isinstance(src_path, str): raise ValueError('Specified file path must be a string.')
        if not src_path.endswith('.atlas'): raise ValueError('Source file must be an Atlas file (.atlas).')

        self.src_path = src_path.replace('/', sep)
        with open(self.src_path, 'r') as f:
            self.contents = load(f)

        IMG_Extentions = ('.png', '.jpg', '.jpeg')
        try: self.image, *_ = filter( lambda i: i.endswith(IMG_Extentions), tuple(self.contents.keys()) )
        except ValueError: raise ValueError('The specified Atlas file, does not target any acceptable image type.')
        self.original_textures = []
        self._load()

    def _load(self):
         #late import to prevent recursive import.
        global CoreImage
        if CoreImage is None:
            from kivy.core.image import Image as CoreImage

        d = dirname(self.src_path)
        img = join(d, self.image)
        texpool = self.contents[self.image]
        ci = CoreImage(img)
        atlas_texture = ci.texture
        self.original_textures.append(atlas_texture)
        textures = {}

        for subfilename, ids in texpool.items():
            textures[subfilename] = {}
            for region_id, region_coords in ids.items():
                textures[subfilename][region_id] = atlas_texture.get_region(*region_coords)
            textures[subfilename] = JSDictionary(textures[subfilename])
            if not subfilename in self.__dict__:
                setattr(self, subfilename, textures[subfilename])
