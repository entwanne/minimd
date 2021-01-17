from setuptools import find_packages
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


with open('lucina/_about.py') as f:
    about = {}
    exec(f.read(), about)


setup(
    name='minimd',
    version=about['__version__'],
    description='Minimal markdown parser',
    long_description=readme(),
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
            'pytest-mock',
            'flake8',
            'isort',
        ]
    },
    license=about['__license__'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)
