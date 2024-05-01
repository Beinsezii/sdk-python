from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="runware",
    license="MIT",
    version="0.1.0",
    author="Runware Inc.",
    author_email="python.sdk@runware.ai",
    description="The Python Runware SDK is used to run image inference with the Runware API, powered by the RunWare inference platform. It can be used to generate imaged with text-to-image and image-to-image. It also allows the use of an existing gallery of models or selecting any model or LoRA from the CivitAI gallery. The API also supports upscaling, background removal, inpainting and outpainting, and a series of other ControlNet models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["Runware", "stable diffusion", "text to image", "image to text"],
    url="https://github.com/runware/sdk-python",
    project_urls={
        "Documentation": "https://docs.runware.ai/",
        "Changes": "https://github.com/runware/sdk-python/releases",
        "Code": "https://github.com/runware/sdk-python",
        "Issue tracker": "https://github.com/runware/sdk-python/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        # Add your SDK's dependencies here
        "websockets>=8.1",
        # ...
    ],
)
