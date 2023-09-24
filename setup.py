from setuptools import setup, find_packages

from avelo_map.version import __version__

requirements = [
    "geopandas",
    "matplotlib",
    "contextily"
]

setup(
    name="avelo_map",
    packages=find_packages(),
    description='Module pour me permettre de visualiser mes trajets àVélo',
    version=__version__,
    author='NicGrimpe',
    author_email='ngariepy1999@gmail.com',
    install_requires=requirements,
    extras_require={
        'dev': [
            'build',
        ]
    }
)
