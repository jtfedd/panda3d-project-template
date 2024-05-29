from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task
from panda3d.core import AmbientLight, PointLight, Vec4


class Environment:
    def __init__(self, base: ShowBase) -> None:
        base.disableMouse()
        base.camera.setY(-10)

        self.aLight = AmbientLight("ambient")
        self.aLight.setColor(Vec4(0.1, 0.1, 0.1, 1.0))
        self.alNP = base.render.attachNewNode(self.aLight)
        base.render.setLight(self.alNP)

        self.pivot = base.render.attachNewNode("pivot")
        self.pivot.setY(-1)

        self.pLight = PointLight("point")
        self.pLight.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.plNP = self.pivot.attachNewNode(self.pLight)
        self.plNP.setX(2)
        base.render.setLight(self.plNP)

        base.taskMgr.add(self.update, "lights-update")

    def update(self, task: Task) -> int:
        self.pivot.setR(50 * task.time)

        return task.cont
