from direct.showbase.ShowBase import ShowBase

from lib.environment.environment import Environment
from lib.sphere.sphere import Sphere
from lib.text.text import Text


class App:
    def __init__(self, base: ShowBase):
        self.camera = Environment(base)
        self.sphere = Sphere(base)
        self.text = Text(base)
