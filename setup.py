## setup

from setuptools import setup



setup(

    name='PySyntext',

    version='1.0',

    author='H. Kaur, A. Pak, Y. Zhang',

    author_email='NA',

    packages=['PySyntext'],

    url='https://github.com/UBC-MDS/PySyntext',

    license='LICENSE.txt',

    description='Text Summarization Tools',

    long_description=open('README.md').read(),

    install_requires=[

        'pandas>=0.23.4',
        
        'nltk>=3.4',
    
        'pytest>=3.5.1',
        
        ]

)
