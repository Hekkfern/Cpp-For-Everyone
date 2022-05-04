# C++ For All

- [C++ For All](#c-for-all)
- [How to generate](#how-to-generate)
- [How to develop](#how-to-develop)

# How to generate

1. Install `pipenv==2022.5.2` package for Python.

```bash
python3 -m pip install pipenv==2022.5.2
```

**NOTE**: More info about installing `pipenv` in different OS can be found in [the official repo](https://github.com/pypa/pipenv/blob/main/README.md).

2. Install the Python packages for this project:

```bash
pipenv install
```

3. Open a terminal.
4. Inside the terminal, set the current folder as the root folder of this repository.
5. Execute:

```bash
pipenv shell
make html
exit
```

# How to develop

1. Install `pipenv==2022.5.2` package for Python.

```bash
python3 -m pip install pipenv==2022.5.2
```

**NOTE**: More info about installing `pipenv` in different OS can be found in [the official repo](https://github.com/pypa/pipenv/blob/main/README.md).

2. Install the Python packages for this project:

```bash
pipenv install --dev
```

3. Open a terminal.
4. Inside the terminal, set the current folder as the root folder of this repository.
5. Execute:

```bash
pipenv shell
sphinx-autobuild source build/html
```

6. Open a web browser and go to http://127.0.0.1:8000/.
7. When you want to stop developing, go to the terminal and press CTRL+C to stop the server.
