from flask import Flask
import unittest
import requests
import json

from main import app

class TestConnection(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(); 
    
    def tearDown(self):
        print('clear redis entry here')

    def test_server_running(self):
        response = requests.get('http://159.203.226.234:7000/')
        assert(response.status_code == 200)
    
    def test_landscape_generation(self):
        response = requests.get('http://159.203.226.234:7000/get_landscape')
        assert(response.status_code == 200)

    def test_error_case(self):
        response = requests.get('http://159.203.226.234:7000/nonexistant')
        assert(response.status_code, 500)


if __name__ == '__main__':
    unittest.main(); 

#assert regular url return string
#asset get landscape returns 
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)

# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()
# plt.savefig("test1.png")