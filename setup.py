from distutils.core import setup

setup(
    name='Heart_disease',
    version='0.2.1',
    description='Classes for technical analysis of building dataset.',
    author='Sandeep Varma Uppalapati',
    author_email='suppalap@mail.yu.edu',
    license='MIT',
    url='https://github.com/monster2920/Analytical_Programming_Project3',
    packages=['Heart_Disease_Analysis'],
    install_requires=[
        'matplotlib>=3.7.1',
        'numpy>=1.24.3',
        'pandas>=1.5.3',
        'seaborn>=0.12.2',
    ],
)
