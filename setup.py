from distutils.core import setup

setup(
    name='dimedbpy',
    version='0.1.0',
    packages=['dimedbpy'],
    py_modules=['dimedbpy'],
    url='https://github.com/AberystwythSystemsBiology/dimedbpy',
    license='MIT',
    author='Keiron O\'Shea',
    author_email = 'keo7@aber.ac.uk',
    description = 'Python wrapper for DIMEdb\'s REST API',
    install_requires=["pandas", "requests", "click", "prettytable"],
    entry_points='''
        [console_scripts]
        dimedbpy=dimedbpy.__init__:mass_search
    ''',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers'
    ]
)
