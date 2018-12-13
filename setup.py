import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visbeat",
    version="0.0.6",
    author="Abe Davis",
    author_email="everyonehasadance@gmail.com",
    description="Code for 'Visual Rhythm and Beat' SIGGRAPH 2018",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abedavis/visbeat",
    project_urls={
        'Abe Davis': 'http://www.abedavis.com/',
        'Visual Rhythm and Beat': 'http://www.abedavis.com/visualbeat/',
        'Source': 'https://github.com/abedavis/visbeat',
        'Demo': 'http://www.abedavis.com/visualbeat/demo/',
    },
    install_requires=[
        'numpy',
        'scipy',
        'bs4',
        'librosa',
        'imageio',
        'requests',
        'moviepy',
        'termcolor',
        'youtube-dl',
        'matplotlib',
    ],
    scripts=['bin/dancefer'],
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
)
