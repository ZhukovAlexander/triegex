from setuptools import setup
import codecs

with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='triegex',
    url='https://github.com/ZhukovAlexander/triegex',
    author='Alexander Zhukov',
    author_email='zhukovaa90@gmail.com',
    description='Trie-ized regular expressions in python',
    long_description=readme,
    keywords='python regular expressions trie',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    py_modules=['triegex'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
