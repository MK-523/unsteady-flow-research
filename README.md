# unsteady-flow-research
Research on unsteady flow phenomena, turbulence, flow instabilities, and flow-generated sound

# Unsteady Flow Research

This repository contains research and projects on unsteady flow phenomena, turbulence, flow instabilities, and flow-generated sound.

## Projects

Shock-Turbulent Boundary layer Interactions:
  1. x represents location along boundary layer.
     u is a simple oscillatory velocity to mimic turbulence.
     shock adds a step function at x=0.5 to simulate shock wave.
     interaction shows how the turbulence interacts with the shock.

  Output: Time-space plot showing shock-turbulence interaction.


SuperSonic Jet Noise
  2. t is the time vector for the simulation.
     frequency represents main tone of the jet noise.
     pressure simulates damped sine wave to mimic acoustic pressure fluctuations in supersonic jet.
     FFT analysis converts the signal to the frequency domain to identify dominant noise frequencies.

  Output: Time-domain plot of jet noise and frequency spectrum.

Wind Turbine Aeroacoustics
 3. t is a time vector.
    blade_pass_freq simulates the frequency of blades passing a point.
    turbulence_noise adds random fluctuations to simulate realistic wind turbulence.
    pressure_signal combines periodic blade noise and turbulence.
    FFT analysis is used to study frequency content.

Output: Time-domain and frequency-domain plots of blade noise. 

Analysis Notebook
 4. Demonstrates a generic turbulent signal with noise.
    Visualizes it in the time domain and analyzes its frequency spectrum using FFT.

  Purpose: Provides example techniques for analyzing flow and acoustic data from simulations.

## Simulations

Numerical simulations and modeling codes.
