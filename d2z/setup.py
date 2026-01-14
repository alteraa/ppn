import setuptools

setuptools.setup(
    name="deb2zip",
    version="0.0.1",
    author="John Doe",
    description="Convert deb packages to zip files.",
    py_modules=["deb2zip"],
    entry_points={
        "console_scripts": [
            "deb2zip=deb2zip:main",
        ],
    },
)
