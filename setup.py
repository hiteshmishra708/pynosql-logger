from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='pymongo-logger',
    version='1.0.1',
    description='For logging & accessing application data into mongodb',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hiteshmishra708/pymongo-logger',
    author='Hitesh Mishra',
    author_email='hiteshmishra708@gmail.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='logger, django logger, flask logger, nosql logger, mongodb logger, setuptools, development',
    package_dir={'': 'mongologger'},
    packages=find_packages(),
    python_requires='>=3.6, <4',
    project_urls={
        'Bug Reports': 'https://github.com/hiteshmishra708/pymongo-logger/issues',
        'Say Thanks!': 'https://linkedin.com/in/hiteshmishra708/',
        'Source': 'https://github.com/hiteshmishra708/pymongo-logger/',
    },
)