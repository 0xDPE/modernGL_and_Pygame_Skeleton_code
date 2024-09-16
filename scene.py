from meshes.triangle_mesh import TriangleMesh

class Scene:
    def __init__(self, app):
        self.app = app
        self.triangle = TriangleMesh(self.app)

    def update(self):
        pass
    def render(self):
        self.triangle.render()