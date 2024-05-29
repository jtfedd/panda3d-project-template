import math

from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task


class Sphere:
    def __init__(self, base: ShowBase) -> None:
        sphere = base.loader.loadModel("assets/sphere.glb")
        if sphere is None:
            return

        self.sphere = sphere

        self.sphere.reparentTo(base.render)
        self.updateTask = base.taskMgr.add(self.update, "sphere-update")

    def update(self, task: Task) -> int:
        self.sphere.setZ(math.sin(task.time * 1.5))
        self.sphere.setColorScale(0.1, 0.4, 1.0, 1.0)

        return task.cont
