class ShaderReader:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.shader = self.get_program(shader_name="shader")

    def update(self):
        pass

    def get_program(self, shader_name):
        with open(f"shaders/{shader_name}.vert") as file:
            vertex_shader = file.read()

        with open(f"shaders/{shader_name}.frag") as file:
            fragment_shader = file.read()
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader= fragment_shader)
        return program