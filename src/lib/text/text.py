from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task
from panda3d.core import TextNode, TextProperties, Vec4


class Text:
    def __init__(self, base: ShowBase) -> None:
        self.text = TextNode("text")
        self.text.setText("Hello, World")
        self.text.setTextColor(Vec4(1.0, 1.0, 0.0, 1.0))
        self.text.setTextScale(0.5)
        self.text.setAlign(TextProperties.A_center)
        self.textNode = self.text.generate()

        self.pivotNode = base.render.attachNewNode("pivot")
        self.textNodePath = self.pivotNode.attachNewNode(self.textNode)

        self.textNodePath.setY(-1.3)
        self.textNodePath.setTwoSided(True)
        self.textNodePath.setLightOff()

        self.updateTask = base.taskMgr.add(self.update, "text-update")

    def update(self, task: Task) -> int:
        self.pivotNode.setH(task.time * 30)

        return task.cont
