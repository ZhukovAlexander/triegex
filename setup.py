from setuptools import setup
import codecs

with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='triegex',
    description='Trie-ized regular expressions in python',
    long_description=readme,
    keywords='python regular expressions trie',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=['triegex'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
