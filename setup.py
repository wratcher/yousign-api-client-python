import setuptools


setuptools.setup(
    name = "ysApi",
    version = "1",
    author = "Yousign",
    packages=['ysApi'],
    #packages=setuptools.find_packages(),
    # Project uses suds
    # installed or upgraded on the target machine
    install_requires = ['suds-community>=1.1.0']
)
