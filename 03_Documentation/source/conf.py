# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# -- Path setup --------------------------------------------------------------
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
]

project = 'FallingFilmLoopingPhotoreactor'
copyright = '2025, Shibu Naskar, Daniel Kowalczyk et al'
author = 'Shibu Naskar, Daniel Kowalczyk et al'

# -- General configuration ----------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': False,
}

autodoc_mock_imports = ["numpy", "scipy", "matplotlib", "pandas", "tinkerforge", "PyQt5", "sklearn", "ICIW_Plots", "rtdpy"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
