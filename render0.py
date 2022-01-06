#!/usr/bin/env python

nx = 200
ny = 100

buffer = f'P3\n{nx} {ny}\n255\n'

for j in range(0, ny):
    for i in range(0, nx):
        r = i / nx
        g = j / ny
        b = 0.2
        ir = int(255.99 * r)
        ig = int(255.99 * g)
        ib = int(255.99 * b)
        buffer += f'{ir} {ig} {ib}\n'

with open('render0.ppm', 'w') as r0:
    r0.write(buffer)
