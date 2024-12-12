# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Illinois Legal Aid Online Documentation'
copyright = '2024, Illinois Legal Aid Online'
author = 'ILAO'

release = 'December 2024'
version = '150.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
 'css/custom.css'
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- todos
todo_include_todos = True
