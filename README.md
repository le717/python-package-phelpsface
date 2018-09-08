# python-package-phelpsface

> Conveniently add Angry Michael Phelps anywhere in your project!

**Maintainers**:

- Caleb Ely

**License**:

[The Unlicense](LICENSE)

## Brief

This package provides an easy-to-access Angry Michael Phelps image to use anywhere in your project, from internal tool to web app!

More seriously, this project's purpose is to provide a working example for converting a Python package into a wheel for publishing and/or use in other projects.

## Usage

- Be sure Python 3.5+ is installed!

```python
import phelpsface

# Get the direct URL to the image
phelpsface.as_url()

# Return an ASCII art version
phelpsface.as_ascii()

# Also available as an ANSI art version
phelpsface.as_ansi()

# Open the image in a new tab in your default browser
phelpsface.in_browser()
```

## Background

To ease the distribution and installation of a Python library, the maintainer(s) often convert the library into a Python wheel before uploading it to a Python package repository, such as [PyPi](https://pypi.org). However, it is not always clear to learn how to create a wheel. This project aims to ease that boundary by providing a complete Python library, build script, and full explanations from start  to finish.

## Setting Up

To start, we need some Python code to serve as our library. We will use the `./phelpsface/phelpsface.py` module for this purpose. If you open this file, you will see a few methods providing an image of [#PhelpsFace](https://knowyourmeme.com/memes/phelpsface-angry-michael-phelps) in various formats. There is no need to edit this file but you are free to do so if you wish.

Next, we need to install Python and the packages required to build a wheel. Python versions 3.5.0 and higher should work. Start by installing [Python](https://www.python.org) if needed, then installing the [`setuptools`](https://github.com/pypa/setuptools) package by running the following command in a terminal:

```shell
$ pip install setuptools
Collecting setuptools
...
Successfully installed setuptools-x.y.z
```

(The `$` indicates a new line in a bash prompt. You do not need to type it, only everything after the `$`. If you are running Windows, there will not a `$`.)

## `setup.py`

Now we come to the core of this documentation: `./setup.py`. We will use this script to build a wheel. This file is where all the metadata is defined, be it required or recommended. We will only cover the most basic information needed to build a wheel. If you want to get into the advanced usage, refer to the [official documentation](#additional-resources).

Let us open the file and see what it contains.

```python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


# Get the package's longer description
# (usually located in the README file)
with open("./README.md", "rt", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="phelpsface",
    version="1.0.0",
    description="#PhelpsFace",
    url="https://github.com/le717/python-package-phelpsface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Caleb Ely",
    author_email="le717@users.noreply.github.com",
    python_requires=">=3.5",
    package_dir={"": "phelpsface"},
    py_modules=find_packages()
)
```

That may look like a lot of stuff, but it really is not! Let us break it down into chunks.

```python
from setuptools import setup
```

This allows us to us to use the `setup` function from the `setuptools` package we installed earlier. This will perform all the magic of creating a wheel for us. All we have to do is feed it our package information.

```python
# Get the package's longer description
# (usually located in the README file)
with open("./README.md", "rt", encoding="utf-8") as f:
    long_description = f.read()
```

Here, we are reading the `./README.md` file into a variable called `long_description`. This makes it easier for us to provide more through documentation for the people who will use our package.

### Defining the Metadata

We will detour for just a moment to list and collect the information we need to create a wheel. To create a wheel, `setup` needs certain information. However, what information is that?

We require the following information to create a wheel:

- package name
- package version (in the format `major.minor.patch`)
- the file(s) that contains our code

Additionally, the following is a partial list of recommended information to include. We will be including these plus a little bit more in our script.

- summary
- longer description
- project URL (GitHub, GitLab, VSTS, etc.)
- maintainer name and email

### `setup()`

Now that we have defined what information we needed, let's continue looking at `./setup.py`, specifically the `setup()` function. We will take it one logical chunk at a time.

```python
name="phelpsface",
version="1.0.0",
description="#PhelpsFace",
url="https://github.com/le717/python-package-phelpsface",
```

In this block, we define our package name to be `phelpsface`, version it as `1.0.0`, write a brief summary (rather oddly called `description`), and provide the URL to the GitHub repository where the source control lives. So far, straightforward.

```python
long_description=long_description,
long_description_content_type="text/markdown",
```

Recall earlier that we read the contents of the `./README.md` file into a variable called `long_description`. Here, we use that content as the package's longer description. Because the file is written using [Markdown](https://daringfireball.net/projects/markdown/), we need to tell this to `setuptools` so it will handle it correctly.

```python
author="Caleb Ely",
author_email="le717@users.noreply.github.com",
```

Here, we define the package maintainer's name and email address. 👀

```python
python_requires=">=3.5",
package_dir={"": "phelpsface"},
py_modules=find_packages()
```

This is the most complicated part of the script, and as you will shortly see, it is not even that complicated.

- `python_requires=">=3.5"`: This package can only be installed on Python installations that are of version 3.5.0 or higher.
- `package_dir={"": "phelpsface"}`: Recall that our code is located at `./phelpsface/phelpsface.py`. When we build our wheel, we want to allow the user to run `import phelpsface` to use our code. Without this line, `setuptools` would not find the code. The dictionary key is the location that we want our code to exist. Using `""` as the key means we want it to be at the top-level. The value is the location of our code, in our case, `"phelpsface"`. There is no need to give any path separators.
- `py_modules=find_packages()`: `setuptools` contains a function called `find_packages()` that looks for a generates a list of files that contains your code is contained in. By calling this method, we do not have to worry about telling `setuptools` how to find our code. It finds it for us. Alternatively, if we did not want to call this function, we can specify the individual files in a list. For example, because our code lives in `phelpsface.py`, we would specify `phelpsface` without the file extension.

## Building a Wheel

Now we that we have defined all our metadata, we need to run the following command in a terminal:

```shell
$ python ./setup.py bdist_wheel
running bdist_wheel
running build
running build_py
...
```

When this process finishes, browse the newly created `./dist` directory to reveal an even newly created wheel. I am going to list the directory contents in the terminal but viewing the directory in File Explorer works just as well.

```shell
$ ls -la ./dist
total 12
drwxr-xr-x 1 Caleb 1049089    0 Sep  7 15:17 ./
drwxr-xr-x 1 Caleb 1049089    0 Sep  7 15:17 ../
-rw-r--r-- 1 Caleb 1049089 8022 Sep  7 15:28 phelpsface-1.0.0-py3-none-any.whl
```

The only file in the directory, `phelpsface-1.0.0-py3-none-any.whl` is our generated wheel. If everything in `./setup.py` was defined correctly, then you have successfully created a working Python wheel of #PhelpsFace! 👍

## Additional Resources

We have only scratched the surface on Python package generation. There is a whole metric ton of additional information available on the Internet. If you would like to learn more, the following are some great resources to consult.

- [Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/index.html)
- [Sample Python Package - Python Packaging Authority](https://github.com/pypa/sampleproject)
