import sys

from setuptools import setup

PLATFORM_HELP = "Platform must be specified using --platform=<platform>"
INSTALLER_HELP = "Installer must be specified using --installer=<installer>"


def parseArg(argName: str, helpStr: str) -> str:
    for arg in sys.argv:
        if arg.startswith(f"--{argName}="):
            sys.argv.remove(arg)

            parts = arg.split("=")
            if len(parts) != 2:
                print(helpStr)
                sys.exit(1)

            value = parts[1]
            if len(value) == 0:
                print(helpStr)
                sys.exit(1)

            return value

    print(helpStr)
    sys.exit(1)


VERSION = "v0.0.3"
NAME = "TemplateApp"
EXECUTABLE = "template_app"

PLATFORM = parseArg("platform", PLATFORM_HELP)
INSTALLER = parseArg("installer", INSTALLER_HELP)

print(NAME, EXECUTABLE, VERSION, PLATFORM, INSTALLER)

setup(
    name=NAME,
    version=VERSION,
    options={
        "build_apps": {
            # Build template_app.exe as a GUI application
            "gui_apps": {
                EXECUTABLE: "main.py",
            },
            # Specify the path to the requirements file
            "requirements_path": "../requirements.txt",
            # Set the icon for the app
            "icons": {
                EXECUTABLE: [
                    "assets/icon/icon-16.png",
                    "assets/icon/icon-24.png",
                    "assets/icon/icon-32.png",
                    "assets/icon/icon-48.png",
                    "assets/icon/icon-64.png",
                    "assets/icon/icon-128.png",
                    "assets/icon/icon-256.png",
                ],
            },
            # Set up output logging, important for GUI apps!
            "log_filename": "$USER_APPDATA/TemplateApp/output.log",
            "log_append": False,
            # Specify which files are included with the distribution
            "include_patterns": [
                "**/*.bam",
                "**/*.ico",
            ],
            "exclude_patterns": [
                "test/**",
            ],
            # Include the OpenGL renderer
            "plugins": [
                "pandagl",
                "p3openal_audio",
            ],
            # Specify platforms to build
            "platforms": [PLATFORM],
        },
        "bdist_apps": {
            "installers": {PLATFORM: INSTALLER},
        },
    },
)
