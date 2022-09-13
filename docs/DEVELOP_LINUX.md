# Develop on a Linux OS Machine

- [Develop on a Linux OS Machine](#develop-on-a-linux-os-machine)
  - [Setup](#setup)
  - [How to work](#how-to-work)
    - [How to generate a release locally](#how-to-generate-a-release-locally)
    - [How to develop](#how-to-develop)

## Setup

1. Install `python3` (although it normally comes preinstalled).

2. Install `pipenv==2022.8.24` package for Python.

```bash
python3 -m pip install pipenv==2022.8.24
```

3. Download the source code of this repo (using `git clone` command or getting the ZIP file from the repository).

## How to work

### How to generate a release locally

1. Open a terminal and set the current working path to the root folder of this repository.

2. Install the Python packages for this project:

```bash
pipenv install
```

3. Execute:

```bash
pipenv run make html
```

### How to develop

1. Open a terminal and set the current working path to the root folder of this repository.

2. Install the Python packages for this project:

```bash
pipenv install --dev
```

3. Execute:

```bash
pipenv run sphinx-autobuild source build/html
```

5. Open a web browser and go to http://127.0.0.1:8000/.


6. When you want to stop developing, go to the terminal and press CTRL+C to stop the server.
