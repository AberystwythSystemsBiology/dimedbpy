from distutils.core import setup

setup(
    name='dimedbpy',
    version='0.0.2',
    packages=['dimedbpy'],
    url='https://www.github.com/KeironO/dimedbpy',
    license='MIT',
    author='Keiron OShea',
    author_email = 'keo7@aber.ac.uk',
    description = 'Python wrapper for DIMEdb\'s REST API',
    install_requires=["pandas", "requests"],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers'
    ]
)
