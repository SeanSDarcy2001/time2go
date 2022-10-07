import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time2go",
    version="0.0.0",
    author="Sean Darcy, Samuel Ydenberg",
    author_email="sdarcy2@jhu.edu",
    description="PA3 Programming Assignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "scipy", "rich", "click"],
    include_package_data=True,
    python_requires=">=3.9",
)