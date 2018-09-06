import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = [l.strip() for l in fh]

setuptools.setup(
    name='py_mocker',
    version='0.0.2',
    author='Vladimir Ponarevsky',
    author_email='vvp@protonmail.ch',
    description='Easy mocking with python, aiohttp and docker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vv-p/py_mocker',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
)
