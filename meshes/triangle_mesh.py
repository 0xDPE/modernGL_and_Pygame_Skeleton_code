import numpy as np

from meshes.base_mesh import BaseMesh

class TriangleMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.shader

        self.vbo_format = "3f 3f"
        self.attributes = ("in_position", "in_color")
        self.vao = self.get_vao()

    def get_vertex_data(self):
        vertices = [
            (-1.0, -1.0, 0.0), (1.0,-1.0, 0.0), (0.0, 1.0, 0.0),
        ]
        colors = [
            (1, 0, 0), (0, 1, 0), (0, 0, 1),
        ]
        vertex_data = np.hstack([vertices, colors],dtype="float32")
        return vertex_data
