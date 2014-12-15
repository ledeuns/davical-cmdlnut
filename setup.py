from distutils.core import setup
setup(name='davical-cmdlnutl',
    version='1.2.1',
    author='Jason Alavaliant',
    author_email='alavaliant@gmail.com',
    url='http://davical-cmdlnut.sourceforge.net/',
    description='Command line administration utility for interacting with a davical database',
    license='gpl',
    platforms='any',
    scripts=['davical-cmdlnutl'],
    data_files=[('/usr/share/doc/davical-cmdlnut/',['README'])]
    )

