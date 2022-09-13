# Develop on a Windows OS Machine

- [Develop on a Windows OS Machine](#develop-on-a-windows-os-machine)
  - [Setup](#setup)
  - [How to work](#how-to-work)
    - [How to generate a release locally](#how-to-generate-a-release-locally)
    - [How to generate a release locally](#how-to-generate-a-release-locally-1)
    - [How to develop](#how-to-develop)

## Setup

1. Open a web browser, go to https://www.python.org/downloads/windows/ and download the python binary. Note: although there is no a minimum Python version, it is recommended to install 3.8 or newer.

2. Install Python from the previous downloaded installer. Note: use *Customize installation* option and make sure you check the checkbox to install `pip` package.

3. Open a PowerShell terminal.

4. Install `pipenv==2022.8.24` package for Python.

```shell
python3 -m pip install pipenv==2022.8.24
```

5. Download the source code of this repo (using `git clone` command or getting the ZIP file from the repository).

## How to work

### How to generate a release locally

### How to generate a release locally

1. Open a PowerShell terminal and set the current working path to the root folder of this repository.

2. Install the Python packages for this project:

```shell
python -m pipenv install
```

3. Execute:

```shell
python -m pipenv run make html
```

### How to develop

1. Open a PowerShell terminal and set the current working path to the root folder of this repository.

2. Install the Python packages for this project:

```shell
python -m pipenv install --dev
```

3. Execute:

```bash
python -m pipenv run sphinx-autobuild source build/html
```

5. Open a web browser and go to http://127.0.0.1:8000/.

6. When you want to stop developing, go to the terminal and press CTRL+C to stop the server.
