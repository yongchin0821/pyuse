#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 11:10 AM
# @Author  : Yongchin

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyuse-core",
    version="0.0.3",
    author="Yongchin",
    author_email="yongchin39@qq.com",
    description="A pkg of wheels. Hope it helps you to write less code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yongchin0821/pyuse",
    project_urls={
        "Bug Tracker": "https://github.com/yongchin0821/pyuse/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"src": ""},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)