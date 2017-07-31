from distutils.core import setup

setup(
    name='dimedbpy',
    version='0.0.1',
    packages=['pyidick'],
    url='https://www.github.com/dimedbpy',
    license='MIT',
    author='Keiron OShea',
    author_email = 'keo7@aber.ac.uk',
    description = 'Python wrapper for DIMEdbs REST API',
    package_data={
      'pyidick': ['data/*.json'],
   },
)