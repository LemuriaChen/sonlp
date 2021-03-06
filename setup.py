
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name='sonlp',
    version='1.0.1',
    description='A simple toolkit for natural language processing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='dandanlemuria',
    author_email='18110980003@fudan.edu.cn',
    url='https://github.com/LemuriaChen/sonlp',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
      ],
    keywords='abbreviation, nlp',
    packages=setuptools.find_packages(),
    install_requires=[
        'click==7.0',
        'lxml==4.4.1',
        'prettytable==0.7.2',
    ],
    scripts=["bin/abbr"],
)
