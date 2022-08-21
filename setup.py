import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="digit_file_mgmt",
    version="0.1.2",
    author="Håkan Persson",
    author_email="hakan.persson@haninge.se",
    description="gRPC proto package for Digi:T file management services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haninge-digit/digit-py-package-file_mgmt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=reqs,
)
