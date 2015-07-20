from setuptools import setup, find_packages
import sys, os

version = '0.3'

setup(name='csscoco',
      version=version,
      description="",
      long_description="""This is a language for expressing CSS code conventions""",
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='css',
      author='Boryana Goncharenko',
      author_email='boryana.goncharenko@gmail.com',
      url='https://github.com/boryanagoncharenko/CssCoco',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points= {
        'console_scripts': [
            'csscoco=csscoco:main',
        ],
      },
)
