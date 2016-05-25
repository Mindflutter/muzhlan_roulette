from setuptools import setup


setup(name='muzhlan-roulette',
      version='0.0.1',
      description='Steam roulette giving random game',
      url='https://bitbucket.org/lomoveishiy/muzhlan_roulette',
      author='lomoveishiy',
      author_email='',
      license='MIT',
      packages=['muzhlan_roulette', 'resources', 'templates'],
      install_requires=['flask', 'steamapi', 'pyaml'],
      include_package_data=True,
      entry_points={'console_scripts': ['muzhlan-roulette = muzhlan_roulette.roulette:main']},
      zip_safe=False)
