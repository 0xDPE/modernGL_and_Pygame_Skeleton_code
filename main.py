from pygame import GL_CONTEXT_PROFILE_CORE

import moderngl as mgl
import pygame as pg
import sys

from scene import Scene
from settings import *
from shader_reader import ShaderReader

class Engine:
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags=mgl.DEPTH_TEST| mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = "auto"

        self.clock = pg.time.Clock()
        self.deltaTime = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.shader_program = ShaderReader(self)
        self.scene = Scene(self)
    def update(self):
        self.shader_program.update()
        self.scene.update()

        self.deltaTime = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
    def render(self):
        self.ctx.clear(color= BG_COLOR)
        self.scene.render()
        pg.display.flip()
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()
if __name__ == "__main__":
    app = Engine()
    app.run()