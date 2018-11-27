from .equations import relative_roughness, velocity, reynolds, delta_p, f_darcy


class Pipe:
    def __init__(self, internal_diameter, roughness, length):
        self.internal_diameter = internal_diameter
        self.roughness = roughness
        self.length = length

    @property
    def relative_roughness(self):
        return relative_roughness(self.roughness, self.internal_diameter)


class Fluid:
    def __init__(self, density, viscosity):
        self.density = density
        self.viscosity = viscosity


class Flow:
    def __init__(self, pipe, fluid, volumetric_flow_rate):
        self.pipe = pipe
        self.fluid = fluid
        self.volumetric_flow_rate = volumetric_flow_rate

    @property
    def velocity(self):
        return velocity(self.pipe.internal_diameter, self.volumetric_flow_rate)

    @property
    def reynolds_number(self):
        return reynolds(
            self.velocity, self.pipe.internal_diameter, self.fluid.density,
            self.fluid.viscosity)

    @property
    def f_darcy(self):
        return f_darcy(self.pipe.relative_roughness, self.reynolds_number)

    @property
    def delta_p(self):
        return delta_p(
            self.velocity, self.f_darcy, self.pipe.length,
            self.pipe.internal_diameter, self.fluid.density)
