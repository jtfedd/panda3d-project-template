from setuptools import setup

setup(
    name="TemplateApp",
    options={
        "build_apps": {
            # Build template_app.exe as a GUI application
            "gui_apps": {
                "template_app": "src/main.py",
            },
            # Set up output logging, important for GUI apps!
            "log_filename": "$USER_APPDATA/TemplateApp/output.log",
            "log_append": False,
            # Specify which files are included with the distribution
            "include_patterns": ["**/*.glb"],
            "exclude_patterns": ["src/text/**"],
            # Include the OpenGL renderer
            "plugins": [
                "pandagl",
            ],
            # Specify platforms to build
            "platforms": [
                "manylinux2014_x86_64",
                "manylinux2014_aarch64",
                "win_amd64",
                "macosx_11_0_arm64",
                "macosx_10_9_x86_64",
            ],
        }
    },
)
