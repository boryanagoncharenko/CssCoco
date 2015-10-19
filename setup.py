from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='csscoco',
    version='0.1.21',
    description='A tool that discovers violations of your CSS code conventions.',
    long_description="CssCoco is a tool that automatically discovers violations of code conventions in your CSS code. The tool is designed to offer great flexibility and cover a wide range of conventions, e.g. whitespacing, indentation, syntax preference and anti-patterns. Unlike other solutions, CssCoco uses a domain-specific language that allows you to tailor the conventions according to your own needs and preferences. And in case writing conventions in a new DSL is a bit too much, you can always use one of the popular ready-to-use convention sets available in the CssCoco GitHub repo. Happy coding!",

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