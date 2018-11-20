import meep as mp
import numpy as np
import matplotlib.pyplot as plt
from meep.materials import fused_quartz

resolution = 50  # pixels/μm
CELL_SIZE = [30, 30, 0]
cell_size = mp.Vector3(*CELL_SIZE)
pml_layers = [ mp.PML(1.0) ]

wvl_min = 0.4
wvl_max = 0.8
fmin = 1 / wvl_max
fmax = 1 / wvl_min
fcen = 0.5 * (fmax + fmin)
df = fmax - fmin
nfreq = 50

# sources = [mp.Source(mp.GaussianSource(fcen,fwidth=df),
#                      component=mp.Ez,
#                      center=mp.Vector3(0, 0))]

sources = [mp.Source(mp.ContinuousSource(frequency=0.1),
                     component=mp.Ez,
                     center=mp.Vector3(0, 0))]

# ORG = mp.Medium(index=7)
#ORG = mp.Medium(index=1)

geometry = [mp.Block(mp.Vector3(mp.inf,mp.inf,mp.inf), # medium
                     center=mp.Vector3(0,0),
                    material=mp.Medium(epsilon=1.2)),
           mp.Block(mp.Vector3(6, 0.2, 0.2),    # waveguide
                    center=mp.Vector3(0,0),
                   material=mp.Medium(epsilon=12)),
           mp.Block(mp.Vector3(6, 0.2, 0.2),    # bottom cap
                   center=mp.Vector3(0, -0.1),
                   material=mp.Medium(epsilon=1.001)),
           mp.Block(mp.Vector3(1, 1, 1),
                   center=mp.Vector3(-3, 0),
                   material=mp.Medium(epsilon=1.001)),   # left cap
           mp.Block(mp.Vector3(1, 1, 1),
                   center=mp.Vector3(3, 0),
                   material=mp.Medium(epsilon=1.001))]   # right cap

sim = mp.Simulation(cell_size=cell_size,
                    boundary_layers=pml_layers,
                    geometry=geometry,
                    sources=sources,
                    resolution=resolution)

# sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Ez, mp.Vector3(), 1e-9))
sim.run(until=10)

eps_data = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Dielectric)

ez_data_x = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ex)
ez_data_y = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ey)
ez_data_z = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ez)

power = np.sqrt(ez_data_x ** 2 + ez_data_y ** 2 + ez_data_z ** 2)

plt.figure(dpi=100)
#plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='binary')
#plt.imshow(ez_data.transpose(), interpolation='spline36', cmap='RdBu', alpha=0.9)
plt.imshow(power.transpose(), interpolation='spline36', cmap='binary')
plt.imshow(power.transpose(), interpolation='spline36', cmap='RdBu', alpha=0.9)
plt.axis('off')
plt.show()
