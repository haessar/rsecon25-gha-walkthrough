from distutils.core import setup

setup(
    name="distutils-demo",
    version="0.1",
    package_dir={"": "src"},
    packages=["arithmetic", "genomics"],
)
