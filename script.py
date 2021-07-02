# Author: Edgar M. O.
# Description: reads user's parameters and creates the 'constants' file

file = open('data.txt', 'r')

# flow conditions
ti = float( file.readline().rstrip('\n') )
re = float( file.readline().rstrip('\n') )

# domain geometry
x1 = float( file.readline().rstrip('\n') )
x2 = float( file.readline().rstrip('\n') )
y1 = float( file.readline().rstrip('\n') )
y2 = float( file.readline().rstrip('\n') )
z1 = float( file.readline().rstrip('\n') )
z2 = float( file.readline().rstrip('\n') )

# number of cells
nx = int( file.readline().rstrip('\n') )

# number of time steps and write interval
ns = int( file.readline().rstrip('\n') )
ds = int( file.readline().rstrip('\n') )

file.close()


""" Calculate missing constants """
U = re * 1e-6 / 1                           # length is 1[m] and nu: nu(water)
ls = 0.08 * 1                               # length is 1[m]
k = 1.5 * (U * ti) ** 2                     # turbulent kinetic energy
e = pow(0.09, 0.75) * pow(k, 1.5) / ls      # epsilon
omega = pow(k, 0.5) / (pow(0.09, 0.25) * ls)# omega
nut = 0.09 * pow(k, 2) / e                  # nut

dx = x2 + x1                                # dx
dy = y1 + y2                                # dy
dz = z1 + z2                                # dz

ny = (dy / dx) * nx                         # ny
nz = (dz / dx) * nx                         # nz

""" write to new file """
constants = open('body', 'w')
constants.write('U\t{0:6.3f};\n'.format(U))
constants.write('tke\t{0:9.6f};\n'.format(k))
constants.write('omega\t{0:9.6f};\n'.format(omega))
constants.write('nut\t{0:9.6f};\n'.format(nut))
constants.write('x1\t{0:6.3f};\n'.format(-x1))
constants.write('y1\t{0:6.3f};\n'.format(-y1))
constants.write('z1\t{0:6.3f};\n'.format(-z1))
constants.write('x2\t{0:6.3f};\n'.format(x2))
constants.write('y2\t{0:6.3f};\n'.format(y2))
constants.write('z2\t{0:6.3f};\n'.format(z2))
constants.write('nx\t{0:6d};\n'.format(int(nx)))
constants.write('ny\t{0:6d};\n'.format(int(ny)))
constants.write('nz\t{0:6d};\n'.format(int(nz)))
constants.write('ns\t{0:6d};\n'.format(int(ns)))
constants.write('ds\t{0:6d};\n'.format(int(ds)))
constants.close()

filenames = ['banner', 'body']
with open('constants', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
