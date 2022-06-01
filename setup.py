from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='chehro',
    version='0.0.1', 
    author='Muhammadreza Haghiri',
    author_email='<haghiri75@gmail.com>',
    url='https://github.com/prp-e/chehro',
    license='MIT',
    description='A face detection system with mediapipe backend.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv', 'mediapipe'],
    keywords = ['face detection', 'cv', 'computer-vision'],
    classifiers = ["Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",]
)