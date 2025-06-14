from setuptools import setup, find_packages

setup(
    name="md2svg-mcp",
    version="0.1.0",
    author="Yossi-lee",
    description="A tool to convert Markdown text into SVG images",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yossi-lee/md2svg-mcp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["fastmcp"],
    entry_points={
        "console_scripts": [
            "md2svg-mcp=md2svg:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)