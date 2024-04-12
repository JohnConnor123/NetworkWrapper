import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as file:
    requirements = file.read().split('\n')


setuptools.setup(
    name="nn-wrapper",
    version="1.0.0",
    author="JohnConnor123",
    author_email="ivan.eudokimoff2014@gmail.com",
    description="A wrapper class for neural networks that makes working with them easier.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/JohnConnor123/nn-wrapper",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    dependency_links=[
        'https://download.pytorch.org/whl/cu118',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
