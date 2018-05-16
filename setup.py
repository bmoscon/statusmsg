from setuptools import find_packages, setup, Command



setup(
    name='statusmsg',
    version='1.0.0',
    description='Status message decorator and context manager',
    long_description='Colorful status message decorator and context manager',
    author='Bryant Moscon',
    author_email='bmoscon@gmail.com',
    python_requires='>=3.5',
    url='http://github.com/bmoscon/statusmsg',
    packages=find_packages(exclude=('tests',)),
    install_requires=[],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)