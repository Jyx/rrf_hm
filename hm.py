#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import csv

def main():
    print("Generate heightmap")
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    with open("heightmap.csv") as f:
        hm = f.readlines()
    hm = [x.strip() for x in hm]

    data = hm[2].split(",")
    data = list(map(float, data))
    xmin = data[0]
    xmax = data[1]
    ymin = data[2]
    ymax = data[3]
    radius = data[4]
    spacing = data[5]
    xnum = int(data[6])
    ynum = int(data[7])

    Z = []
    for i in hm[3:]:
        tmp = []
        for z in i.split(","):
            tmp.append(float(z))
        Z.append(tmp)

    X = np.arange(xmin, xmax, spacing)
    #X = np.arange(-5, 5, 0.25)
    Y = np.arange(ymin, ymax, spacing)
    #Y = np.arange(-5, 5, 0.25)
    xx, yy = np.meshgrid(X, Y)
    print("X: %s" % X)
    print("Y: %s" % Y)
    print("Z: %s (%d elements)" % (Z, len(Z)))
    print("xx: %s" % xx)
    print("yy: %s" % yy)

    # Plot the surface.
    surf = ax.plot_surface(xx, yy, Z, cmap=cm.coolwarm,
                                   linewidth=0, antialiased=True)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    ax.text(-60.60, -42.50, 0, "X-tower", color='red')
    ax.text(60.60, -42.50, 0, "Y-tower", color='red')
    ax.text(0, 67, 0, "Z-tower", color='red')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()

if __name__ == "__main__":
    main()
