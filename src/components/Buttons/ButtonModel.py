from kivy.clock import mainthread
from kivy.uix.button import Button as ButtonSchema
from kivy.graphics.instructions import RenderContext
from kivy.graphics import Mesh
from src.constants.Colors import (
    BUTTON_NORMAL_BACKGROUND_COLOR,
    BUTTON_ILLUMINATION_BACKGROUND_COLOR,
    ICON_NORMAL_BACKGROUND_COLOR,
    ICON_ILLUMINATION_BACKGROUND_COLOR
)

class Button(ButtonSchema):

    def __init__(self, source, useShaders=True):
        super(Button, self).__init__()
        try:
            if len(source) > 0:
                self.source = source[0]
        except:
            self.source = source
        self.currentImage = self.source


        if useShaders:
            self.canvas = RenderContext(use_parent_projection=True)
            self.canvas.shader.source = 'src/shaders/button.glsl'

            self.vfmt = (
                (b'vPosition', 2, 'float'),
                (b'vCardinalUv', 2, 'float'),
                (b'vTexCoords0', 2, 'float')
            )

            #self.canvas["offsetX"]       = 0.0
            #self.canvas["offsetY"]       = 0.0
            self.canvas["hasFocus"]      = 0.0
            self.canvas["bg_color_norm"] = BUTTON_NORMAL_BACKGROUND_COLOR
            self.canvas["bg_color_on"]   = BUTTON_ILLUMINATION_BACKGROUND_COLOR

        if self.currentImage is None:
            self.build_mesh = None
            self.syncValues = None
            self.nextDraw   = None
        else:
            self.nextDraw()

    def build_mesh(self):
        tc = self.currentImage.tex_coords
        vertices = [
            self.pos[0], self.pos[1], 0, 0, tc[0], tc[1],
            self.pos[0]+self.size[0], self.pos[1], 0, 1, tc[2], tc[3],
            self.pos[0]+self.size[0], self.size[1]+self.pos[1], 1, 1, tc[4], tc[5],
            self.pos[0], self.size[1]+self.pos[1], 1, 0, tc[6], tc[7]
        ]

        indices = [0, 1, 2, 3]
        return Mesh(vertices=vertices, indices=indices, mode='triangle_fan', fmt=self.vfmt, texture=self.currentImage)

    @mainthread
    def nextDraw(self):
        with self.canvas:
            self.mesh = self.build_mesh()
        self.bind(pos=self.syncValues, size=self.syncValues)

    def syncValues(self, *args):
        tc = self.currentImage.tex_coords
        self.mesh.vertices = [
            self.pos[0], self.pos[1], 0, 0, tc[0], tc[1],
            self.pos[0]+self.size[0], self.pos[1], 0, 1, tc[2], tc[3],
            self.pos[0]+self.size[0], self.size[1]+self.pos[1], 1, 1, tc[4], tc[5],
            self.pos[0], self.size[1]+self.pos[1], 1, 0, tc[6], tc[7]
        ]
