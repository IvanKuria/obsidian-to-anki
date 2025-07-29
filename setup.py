from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="obsidian-to-anki",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert Obsidian markdown notes to Anki flashcards using AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/obsidian-to-anki",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Text Processing :: Markup",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "obsidian-to-anki=main:main",
        ],
    },
    keywords="obsidian, anki, flashcards, markdown, ai, openai",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/obsidian-to-anki/issues",
        "Source": "https://github.com/yourusername/obsidian-to-anki",
        "Documentation": "https://github.com/yourusername/obsidian-to-anki#readme",
    },
) 