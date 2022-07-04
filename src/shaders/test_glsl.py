from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics.instructions import RenderContext
from kivy.graphics import Rectangle, Color, Mesh
from kivy.atlas import Atlas
from constants.Colors import (
    BUTTON_NORMAL_BACKGROUND_COLOR,
    BUTTON_ILLUMINATION_BACKGROUND_COLOR,
    ICON_NORMAL_BACKGROUND_COLOR,
    ICON_ILLUMINATION_BACKGROUND_COLOR
)

buttons = Atlas("data/buttons.atlas")

class BTN(Button):

    def __init__(self):
        super().__init__(size_hint=(None, None), width=75, height=75,
                pos_hint={'center_x':.5, 'center_y':1})

        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'Shaders/button.glsl'

        self.vfmt = (
            (b'vPosition', 2, 'float'),
            (b'vCardinalUv', 2, 'float'),
            (b'vTexCoords0', 2, 'float')
        )
        self.tex = buttons["RESET"]
        self.onoff = self.switchGen()
        self.canvas["hasFocus"] = next(self.onoff)
        self.canvas["bg_color_norm"] = BUTTON_NORMAL_BACKGROUND_COLOR
        self.canvas["bg_color_on"]   = BUTTON_ILLUMINATION_BACKGROUND_COLOR

        with self.canvas:
            self.mesh = self.build_mesh()
        self.bind(pos=self.syncValues, size=self.syncValues)
        self.bind(on_press=self.btnDown)

    @staticmethod
    def btnDown(i=None):
        i.canvas["hasFocus"] = next(i.onoff)

    def syncValues(self, *args):
        tc = self.tex.tex_coords
        self.mesh.vertices = [
            self.pos[0], self.pos[1], 0, 0, tc[0], tc[1],
            self.pos[0]+self.size[0], self.pos[1], 0, 1, tc[2], tc[3],
            self.pos[0]+self.size[0], self.size[1]+self.pos[1], 1, 1, tc[4], tc[5],
            self.pos[0], self.size[1]+self.pos[1], 1, 0, tc[6], tc[7]
        ]

    def switchGen(self):
        n = 0
        while 1:
            yield n % 2
            n += 1

    def build_mesh(self):
        tc = self.tex.tex_coords
        vertices = [
            self.pos[0], self.pos[1], 0, 0, tc[0], tc[1],
            self.pos[0]+self.size[0], self.pos[1], 0, 1, tc[2], tc[3],
            self.pos[0]+self.size[0], self.size[1]+self.pos[1], 1, 1, tc[4], tc[5],
            self.pos[0], self.size[1]+self.pos[1], 1, 0, tc[6], tc[7]
        ]
        indices = [0, 1, 2, 3]
        return Mesh(vertices=vertices, indices=indices, mode='triangle_fan', fmt=self.vfmt, texture=self.tex)


class MainWidget(FloatLayout):

    def __init__(self):
        super().__init__(size_hint=(1., 1.))
        self.add_widget(BTN())


class Application(App):

    def build(self):
        self.root = BoxLayout(orientation="vertical")
        btn = BTN()
        self.root.add_widget(btn)

        return self.root

if __name__ == '__main__':
    Application().run()
