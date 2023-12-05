from setuptools import setup

setup(
    name='pyspectator',
    version='0.0.1',
    packages=['pyspectator'],
    install_requires=[
        'watchdog'
    ],
    author="Rachid Jeffali",
    description="Une bibliothèque de surveillance (watchdog) simple mais puissante pour les changements dans les fichiers et répertoires, avec une prise en charge avancée de la gestion d'événements."
)
