# Develop on a Linux Machine

- [Develop on a Linux Machine](#develop-on-a-linux-machine)
  - [Setup](#setup)
  - [How to work](#how-to-work)
    - [How to generate a release locally](#how-to-generate-a-release-locally)
    - [How to develop](#how-to-develop)

## Setup

1. Install `pipenv==2022.8.24` package for Python.

```bash
python3 -m pip install pipenv==2022.8.24
```

2. Download the source code of this repo (using `git clone` command or getting the ZIP file from the repository).

## How to work

### How to generate a release locally

1. Install the Python packages for this project:

```bash
pipenv install
```

2. Open a terminal.
3. Inside the terminal, set the current folder as the root folder of this repository.
4. Execute:

```bash
pipenv shell
make html
exit
```

### How to develop

1. Install the Python packages for this project:

```bash
pipenv install --dev
```

2. Open a terminal.
3. Inside the terminal, set the current folder as the root folder of this repository.
4. Execute:

```bash
pipenv shell
sphinx-autobuild source build/html
```

5. Open a web browser and go to http://127.0.0.1:8000/.
6. When you want to stop developing, go to the terminal and press CTRL+C to stop the server.
