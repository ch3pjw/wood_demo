# coding=utf8
import click

from .model import Fluid, Pipe, Flow


def validate_gt_zero(ctx, param, n):
    if n <= 0:
        raise click.BadParameter('Must be greater than zero')
    else:
        return n


def validate_gte_zero(ctx, param, n):
    if n < 0:
        raise click.BadParameter('Must be greater than or equal to zero')
    else:
        return n


@click.command()
@click.argument('density', type=float, callback=validate_gt_zero)
@click.argument('viscosity', type=float, callback=validate_gt_zero)
@click.argument('internal_diameter', type=float, callback=validate_gt_zero)
@click.argument('roughness', type=float, callback=validate_gte_zero)
@click.argument('length', type=float, callback=validate_gte_zero)
@click.argument('volumetric_flow_rate', type=float, callback=validate_gt_zero)
def command(
        density, viscosity, internal_diameter, roughness, length,
        volumetric_flow_rate):
    '''
    Calculate some properties of fluid flow in a pipe.

    Arguments:\n
      DENSITY:               Fluid density / kg m⁻³\n
      VISCOSITY:             Viscosity / centipose\n
      INTERNAL_DIAMTER:      Pipe internal diameter / mm\n
      ROUGHNESS:             Pipe roughness / mm\n
      LENGTH:                Pipe length / m\n
      VOLUMETRIC_FLOW_RATE:  Fluid flow rate / m³ h⁻¹\n
    '''
    # Normalise some units:
    viscosity /= 1000
    internal_diameter /= 1000
    roughness /= 1000
    volumetric_flow_rate /= 3600

    # Build our model
    fluid = Fluid(density, viscosity)
    pipe = Pipe(internal_diameter, roughness, length)
    flow = Flow(pipe, fluid, volumetric_flow_rate)

    print('Pipe pressure loss = {:0.1f} kPa'.format(flow.delta_p / 1000))
    print('Velocity = {:0.2f} m s⁻¹'.format(flow.velocity))
    print('Reynolds number = {:0.2e}'.format(flow.reynolds_number))
    print('Friction factor = {:0.5f}'.format(flow.f_darcy))
