import math


def velocity(pipe_internal_diameter, volumetric_flow_rate):
    x_sectional_area = math.pi * pipe_internal_diameter ** 2 / 4
    return volumetric_flow_rate / x_sectional_area


def reynolds(velocity, characteristic_length, density, viscosity):
    return velocity * characteristic_length * density / viscosity


def f_darcy(
        relative_roughness, reynolds_number, max_iterations=1000,
        threshold=1e-5):
    f = 1.0
    for i in range(max_iterations):
        f_new = (
            1 / (
                -2 * math.log10(
                    relative_roughness / (
                        (3.7 + 2.51) * reynolds_number * math.sqrt(f)
                    )
                )
            )
        ) ** 2
        if abs(f_new - f) < threshold:
            return f_new
        f = f_new
    else:
        raise ValueError('Did not converge')


def relative_roughness(roughness, internal_diameter):
    return roughness / internal_diameter


def delta_p(velocity, f_darcy, length, internal_diameter, density):
    return (
        velocity ** 2 * f_darcy * length * density / (2 * internal_diameter))
