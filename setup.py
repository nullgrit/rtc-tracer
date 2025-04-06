from setuptools import setup, find_packages

setup(
    name='rtc-tracer',
    version='0.1.0',
    description='WebRTC network diagnostics tool (archived)',
    author='dev-null',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
    ],
)
