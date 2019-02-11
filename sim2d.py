import numpy as np
import matplotlib.pyplot as plt


sky = np.zeros((500, 500))

tx = np.array([(0, 0])

E_CHARGE = 1.6021765e-19
E_MASS = 9.109e-31
EPS_0 = 8.854e-12


def critfreq(density):
	return np.sqrt(density * E_CHARGE / EPS_0 / E_MASS)

def refidx(density, infreq):
	return np.sqrt(1 - critfreq(density) ** 2 / infreq ** 2)

def newangle(n1, n2, theta1):
	return np.arcsin(np.sin(theta1) / n1 / n2)


theta = np.deg2rad(45)
pos = tx
 
for i in range(1000):
	pos = 

