#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.readlines()

setuptools.setup(
    name='eks-rolling-update',
    version_format='{tag}.{commitcount}+{gitsha}',
    setup_requires=['setuptools-git-version'],
    description='EKS Rolling Update is a utility for updating the launch configuration or template of worker nodes in'
                ' an EKS cluster.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Craig Huber, Nicolas Bélanger, Sam Weston & contributors',
    url='https://github.com/hellofresh/eks-rolling-update',
    license='Apache License, Version 2.0',
    scripts=['eks_rolling_update.py'],
    packages=['', 'lib'],
    package_dir={'eks-rolling-update': '', 'eks-rolling-update/lib': 'lib'},
    package_data={'': ['README.md', 'LICENSE', 'logo.png']},
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
