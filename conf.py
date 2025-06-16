# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'Activate Your UnitedHealthcare UCard Online – Visit Activate.UHC.com Today'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare'

# The full version
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_title = "Activate Your UnitedHealthcare UCard Online – Visit Activate.UHC.com Today"
html_short_title = "UHC Card Activation"
html_favicon = 'favicon.ico'
html_theme = 'furo'  # SEO-friendly modern theme

html_show_sourcelink = False
html_allow_unsafe = True

html_theme_options = {
    'sidebar_hide_name': False,
    'navigation_with_keys': True,
}

# -- Meta tags for SEO -------------------------------------------------------
def setup(app):
    app.add_meta("description", "Easily activate your UnitedHealthcare UCard at activate.uhc.com. Log in with your member.uhc.com account to manage benefits, check balances, and start using your plan.")
    app.add_meta("keywords", "activate.uhc.com, UnitedHealthcare UCard activation, member.uhc.com login, UHC card activate, UCard benefits")
    app.add_meta("robots", "index, follow")
    app.add_meta("author", "UnitedHealthcare")
    app.add_meta("viewport", "width=device-width, initial-scale=1.0")
