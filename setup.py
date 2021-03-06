from setuptools import setup, find_packages

setup(
    name='qcodes-measurements',
    version='0.1',
    description='QNL qcodes measurement procedures',
    url='https://github.com/QNLSydney/qcodes-measurements',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Licence :: MIT Licence',
        'Topic :: Scientific/Engineering'
    ],
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=2.0.2',
        'pyqtgraph>=0.10.0',
        'qcodes>=0.1.3',
        'wrapt>=1.10.11'
    ],
    python_requires='>=3'
)
