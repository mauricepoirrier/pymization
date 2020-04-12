import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="optpy",
    version="0.1",
    scripts=["dokr"],
    author="Nicolas Camus & Maurice Poirrier",
    author_email="maurice@merkenlabs.com",
    description="A simple optimization solverp problem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mauricepoirrier/optpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
