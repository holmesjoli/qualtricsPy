import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qualtricsPy",
    version="0.0.1",
    author="Joli Holmes",
    author_email="holmesjoli@gmail.com",
    description="Qualtrics API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holmesjoli/qualtricsPy",
    packages=setuptools.find_packages(),
    install_requires=["requests",
                      "utilsPy"]
)
