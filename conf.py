# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "NEST Desktop"
author = "Sebastian Spreizer"
copyright = "2016-present Sebastian Spreizer"
version = "4.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_immaterial.kbd_keys",
]

# Ensure unique targets

# root_doc = 'contents'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Include text at the beginning of every file.
if os.environ.get("READTHEDOCS") == "True":
    READTHEDOCS_VERSION = os.environ.get("READTHEDOCS_VERSION")
    if READTHEDOCS_VERSION in ["dev", "doc"]:
        rst_prolog = """.. warning:: This version of the documentation is NOT an official release. \
        You are reading the documentation version which is in active and ongoing development.
        """
    elif READTHEDOCS_VERSION not in ["latest", version]:
        rst_prolog = """.. warning:: You are not reading the documentation of the latest release of NEST Desktop. \
        Some guide might be outdated.
        """

rst_epilog = "\n.. include:: /substitutions.rst\n"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# See the documentation for a list of builtin themes.
#

# html_additional_pages = {'index': 'index.html'}

html_css_files = [
    "css/fontawesome.min.css",
    "css/brands.min.css",
    "css/solid.min.css",
    "css/styles.css",
]

html_logo = "_static/img/logo/nest-desktop-logo.svg"
html_favicon = "_static/favicon.ico"

html_js_files = []

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_theme = ["sphinx_book_theme", "sphinx_immaterial", "sphinx_material"][1]

if html_theme == "sphinx_book_theme":

    html_theme_options = {
        "home_page_in_toc": True,
        "path_to_docs": "docs",
        "repository_branch": "main",
        "repository_url": "https://github.com/nest-desktop/nest-desktop-docs",
        "use_edit_page_button": True,
        "use_fullscreen_button": False,
        "use_issues_button": True,
        "use_repository_button": True,
    }

elif html_theme == "sphinx_immaterial":

    extensions.append("sphinx_immaterial")

    html_theme_options = {
        "icon": {
            "repo": "fontawesome/brands/github",
            "edit": "material/file-edit-outline",
        },
        "site_url": "https://nest-desktop.github.io/",
        "repo_url": "https://github.com/nest-desktop/nest-desktop/",
        "repo_name": "NEST Desktop",
        "globaltoc_collapse": True,
        "features": [
            "content.tabs.link",
            # "header.autohide",
            "navigation.expand",
            "navigation.instant",
            "navigation.sections",
            # "navigation.tabs",
            "navigation.top",
            # "navigation.tracking",
            # "search.highlight",
            "search.share",
            "toc.follow",
            # "toc.integrate",
            "toc.sticky",
            "announce.dismiss",
        ],
        "palette": [
            {
                "media": "(prefers-color-scheme: light)",
                "scheme": "default",
                "primary": "deep-orange",
                "toggle": {
                    "icon": "material/weather-night",
                    "name": "Switch to dark theme",
                },
            },
            {
                "media": "(prefers-color-scheme: dark)",
                "scheme": "slate",
                "primary": "deep-orange",
                "accent": "lime",
                "toggle": {
                    "icon": "material/weather-sunny",
                    "name": "Switch to light theme",
                },
            },
        ],
        "font": {
            "text": "Roboto",  # used for all the pages' text
            "code": "Roboto Mono",  # used for literal code blocks
        },
        "toc_title_is_page_title": False,
        # BEGIN: social icons
        # "social": [
        #     {
        #         "icon": "fontawesome/brands/github",
        #         "link": "https://github.com/nest-desktop/nest-desktop",
        #         "name": "Source on github.com",
        #     },
        # {
        #     "icon": "fontawesome/brands/python",
        #     "link": "https://pypi.org/project/nest-desktop/",
        # },
        # {
        #     "icon": "fontawesome/brands/conda",
        #     "link": "https://anaconda.org/conda-forge/nest-desktop",
        # },
        # {
        #     "icon": "img/logo/ebrains-logo.svg",
        #     "link": "https://www.ebrains.eu/tools/nest-desktop",
        # },
        # ],
        # END: social icons
        # BEGIN: version_dropdown
        "version_dropdown": False,
        "version_info": [
            {
                "version": "https://nest-desktop.github.io",
                "title": "Github Pages",
                "aliases": [],
            },
            {
                "version": "https://nest-simulator.readthedocs.io",
                "title": "NEST Simulator",
                "aliases": [],
            },
        ],
        # END: version_dropdown
    }

    sphinx_immaterial_custom_admonitions = [
        # {
        #     "name": "question",
        #     "color": (255, 102, 51),
        #     "override": True,
        # },
        # {
        #     "name": "example",
        #     "color": (18, 129, 179),
        #     "override": True,
        # },
    ]

elif html_theme == "sphinx_material":

    import sphinx_material

    autosectionlabel_prefix_document = True

    extensions.append("sphinx_material")

    html_context = sphinx_material.get_html_context()

    html_show_sourcelink = False

    html_sidebars = {
        "**": ["globaltoc.html", "localtoc.html", "searchbox.html"]
        #     # "logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"
    }

    html_theme_options = {
        "base_url": "https://nest-desktop.readthedocs.io/en/latest/",
        "color_primary": "deep-orange",
        "color_accent": "white",
        "css_minify": True,
        "heroes": {},
        "globaltoc_collapse": True,
        "globaltoc_depth": 3,
        "globaltoc_includehidden": True,
        "html_minify": False,
        "html_prettify": False,
        "master_doc": False,
        "nav_links": [
            {
                "href": "https://nest-desktop.github.io/",
                "internal": False,
                "title": "Offical page",
            },
            {
                "href": "https://nest-simulator.readthedocs.io/",
                "internal": False,
                "title": "NEST Simulator",
            },
        ],
        "nav_title": "NEST Desktop",
        "repo_name": "Edit on GitHub",
        "repo_url": "https://github.com/nest-desktop/nest-desktop/",
        "theme_color": "ff6633",
        "version_dropdown": True,
    }

    html_show_sphinx = False
    html_show_copyright = False

    html_theme_path = sphinx_material.html_theme_path()

# add links to modules and objects.
intersphinx_mapping = {
    "nest-simulator": ("https://nest-simulator.readthedocs.io/en/latest/", None),
    "nestml": ("https://nestml.readthedocs.io/en/latest/", None),
    "norse": ("https://norse.github.io/norse", None),
}
