from setuptools import setup

setup(
    name="vizdoomgym",
    version="0.0.2",
    description="OpenAI Gym wrapper for ViZDoom",
    author="Simon Hakenes",
    author_email="simon.hakenes@ini.rub.de",
    install_requires=[
        "gym",
        "vizdoom@https://github.com/mwydmuch/ViZDoom/tarball/1.1.8pre",
        "numpy",
        "pre-commit",
    ],
)
