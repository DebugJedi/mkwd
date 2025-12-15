# """Setup script for mkwd CLI tool"""
# from setuptools import setup

# setup(
#     name='mkwd',
#     version='1.0.0',
#     description='Professional web project scaffolding tool',
#     author='Priyank Rao',
#     author_email='your.email@example.com',
#     py_modules=['mkwd'],
#     entry_points={
#         'console_scripts': [
#             'mkwd=mkwd:main',
#         ],
#     },
#     install_requires=[],
#     python_requires='>=3.7',
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#     ],
# )

from setuptools import setup

setup(
    name="mkwd",
    version="0.1.0",
    py_modules=["mkwd"],
    entry_points={
        "console_scripts": [
            "mkwd = mkwd:main"
        ],
    },
    python_requires=">=3.7",
)
