from distutils.core import setup

setup(
    name='dimedbpy',
    version='0.0.1a',
    packages=['dimedbpy'],
    url='https://www.github.com/KeironO/dimedbpy',
    license='MIT',
    author='Keiron OShea',
    author_email = 'keo7@aber.ac.uk',
    description = 'Python wrapper for DIMEdb\'s REST API',
    install_requires=['requests']
)
