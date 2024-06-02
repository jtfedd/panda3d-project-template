from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData

from lib.app.app import App

CONFIG = """
window-title Template App
icon-filename assets/icon/icon.ico
"""

if __name__ == "__main__":
    loadPrcFileData("", CONFIG)

    base = ShowBase()
    app = App(base)
    base.run()
