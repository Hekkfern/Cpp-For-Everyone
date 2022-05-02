# Configuration file for the Sphinx documentation builder.

from datetime import date

# -- Project information -----------------------------------------------------

project = 'C++ For All'
copyright = f"{date.today().year}, Hector Fernandez"
author = 'Hector Fernandez'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton',
    'sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

html_css_files = [
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/fontawesome.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/brands.min.css",
]

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Hekkfern/cppforall",
            "html": "",
            "class": "fa-brands fa-github",
        },
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_favicon = "images/favicon.png"
html_logo = "images/logo.png"

html_title = "C++ For All"

html_show_copyright = False
html_show_sphinx = False

# -- Extensions configuration ----------------------------

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2
