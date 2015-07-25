from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='csscoco',
    version='0.1.12',
    description='A DSL for CSS Code Convetions',
    long_description="The package detects violations of CSS code conventions automatically. "\
      "It contains a number of predefined conventons sets, however, it also comprises a "\
      "domain-speicific language that is capable of expressing cusomt CSS conventions.",

    url='https://github.com/boryanagoncharenko/CssCoco',
    author='Boryana Goncharenko',
    author_email='boryana.goncharenko@gmail.com',
    license='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='css code conventions web development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['antlr4-python3-runtime'],
    extras_require={},
    package_data={
        'csscoco': ['css/*.*',
                    'node_modules/gonzales/*.*',
                    'node_modules/gonzales/lib/*.*',
                    'node_modules/gonzales/src/*.*', 
                    'node_modules/gonzales/web/*.*'],
    },
    data_files=[],
    entry_points={
      'console_scripts': [
              'csscoco=csscoco.main:main',
          ],
    },
)