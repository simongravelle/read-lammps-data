from setuptools import setup

setup(name='read_lammps_data',
      version='v0.0.1',
      description='Import LAMMPS data into Python',
      long_description=open('README.rst').read(),
      long_description_content_type='text/x-rst',
      url='https://github.com/simongravelle/nmrformd',
      download_url='https://github.com/simongravelle/nmrformd/archive/refs/tags/v0.0.6.tar.gz',
      author='Simon Gravelle',
      author_email='simon.gravelle@live.fr',
      license='GNU GENERAL PUBLIC LICENSE',
      packages=['readlammps'],
      zip_safe=False,
         install_requires=[
       "mdanalysis",
       "pytest",
       "numpy",
       "scipy",
      ]      
      )
