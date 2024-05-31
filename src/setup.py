from setuptools import setup

setup(
    name="TemplateApp",
    options={
        "build_apps": {
            # Build template_app.exe as a GUI application
            "gui_apps": {
                "template_app": "main.py",
            },
            # Specify the path to the requirements file
            "requirements_path": "../requirements.txt",
            # Set the icon for the app
            "icons": {
                "template_app": [
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
            ],
            # Specify platforms to build
            "platforms": [
                "manylinux2014_x86_64",
                "win_amd64",
                "macosx_11_0_arm64",
                "macosx_10_15_x86_64",
            ],
        }
    },
)
