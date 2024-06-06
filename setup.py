from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PythonOverlayLib',
    version='1.0.1',
    url='https://github.com/LUXTACO/PythonOverlayLib',
    author='Takkeshi',
    author_email='tacomastabusiness@gmail.com',
    description='Python library designed to create customizable overlays for desktop applications. It uses PyQt5 to draw shapes such as circles, rectangles, and lines on a transparent window that stays on top of other windows.',
    long_description=long_description,  # Add this line
    long_description_content_type='text/markdown',
    packages=find_packages(),    
    install_requires=['PyQt5 >= 5.15.4'],
)