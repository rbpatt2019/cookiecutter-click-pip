#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.rst") as f:
    long_description = f.read()

setuptools.setup(
        name='{{cookiecutter.project_name}}', 
        version="0.0.0",
        author='{{cookiecutter.author_name}}',
        author_email='{{cookiecutter.email}}',
        description='{{cookiecutter.description}}',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        url='https://github.com/{{cookiecutter.user_name}}/{{cookiecutter.project_name}}',
        package_dir = {"": "src"},
        packages = setuptools.find_packages('src'),
        entry_points={
            'console_scripts':[
                'hello = command_line.example:hello']
        },
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: Unix',
            'Programming Language :: Python :: 3.7'
            ],
        install_requires=['click'],
        python_requires='>=3.7',
        tests_requires=[
            'pytest', 
            'pytest-runner', 
            'pytest-cov',
            'coverage', 
            'pytest-mypy', 
            'mypy', 
            'pytest-instafail'
            ]
        )
