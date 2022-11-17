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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ПЛАН РОБОТИ'
copyright = '2022, Природниче Відділення'
author = 'Природниче відділення'

# The full version, including alpha/beta/rc tags
# release = '0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'matplotlib.sphinxext.plot_directive',
    "sphinx.ext.autodoc",
    'sphinxcontrib.tikz',
    'sphinx.ext.todo',
    # External stuff
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme =  'furo' # 'sphinx_rtd_theme'

html_theme_options = {
    "source_repository": "https://github.com/nat-dep-clg-chnu/template-work-plan/",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

latex_engine = 'pdflatex'
latex_theme = 'howto'
latex_additional_files = ["mystyle.sty"]
latex_elements = {
    'papersize': 'a4paper',
    'inputenc': '\\usepackage[utf8]{inputenc}',
           'pointsize': '12pt',
    'preamble': r'\usepackage{mystyle}',
    'babel': r'''
    \usepackage[ukrainian]{babel}
    ''',
    
    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1
        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
            \textbf{\Huge {ПЛАН РОБОТИ}}

            \vspace{0mm}
            \begin{figure}[!h]
                \centering
                \includegraphics[scale=0.3]{logo.png}
            \end{figure}

            \vspace{0mm}
            \Large \textbf{{ЦК}}

            \small Чернівці, 2022

            \vspace*{0mm}


            %% \vfill adds at the bottom
            \vfill
            \small \textit{Більше корисної інформації можна дізнатися на }{\href{http://college-chnu.cv.ua/}{ВСП <<Фаховий коледж ЧНУ>>}}
        \end{titlepage}


        \begin{titlepage}
            \centering

\begin{normalsize}
\textbf{МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ\\
Чернівецький національний університет імені Юрія Федьковича\\}
\end{normalsize}
{\small  \textbf{Відокремлений структурний підрозділ "Фаховий коледж Чернівецького національного університету імені Юрія Федьковича"}}

            \vspace*{20mm} %%% * is used to give space from top
            
\begin{tabular}{p{8cm}p{8cm}}
\begin{flushleft}
\begin{minipage}{8cm}
<<ПОГОДЖЕНО>>\\ 
Завідувач Природничого відділення\\
\underline{\hspace{3cm}}~J.~Doe\\
<<\underline{\hspace{0.5cm}}>> \underline{\hspace{4cm}}  20\underline{\hspace{0.5cm}}~р.\\
\end{minipage}
\end{flushleft}
&
\begin{flushright}
\begin{minipage}{8cm}
<<ЗАТВЕРДЖУЮ>>\\ 
Заступник директора з навчально-методичної роботи\\
\underline{\hspace{3cm}}~J.~Doe\\
<<\underline{\hspace{0.5cm}}>> \underline{\hspace{4cm}}  20\underline{\hspace{0.5cm}}~р.\\
\end{minipage}
\end{flushright} \\
\end{tabular}

\vspace{30mm} 
            \textbf{\Huge {ПЛАН РОБОТИ}}
            
            \vspace{10mm}
            \Large \textbf{{ЦК}}

\vspace{10mm}
            \large \textbf{{на 2022-2023 н.р.}}

            
            \vspace*{20mm}

\begin{flushleft}
\begin{minipage}{12cm}
План обговорено на засіданні циклової комісії\\ 
    Протокол №\underline{\hspace{0.5cm}} від <<\underline{\hspace{0.5cm}}>> \underline{\hspace{1cm}}  20\underline{\hspace{0.5cm}}~р.\\    
Голова циклової комісії "Прикладної математики та інформаційних технологій"\\
\underline{\hspace{3cm}}~J.~Doe\\
<<\underline{\hspace{0.5cm}}>> \underline{\hspace{4cm}}  20\underline{\hspace{0.5cm}}~р.\\
\end{minipage}
\end{flushleft}

            %% \vfill adds at the bottom
            \vfill
           \small Чернівці, 2022

        \end{titlepage}

        \clearpage
        \pagenumbering{arabic}

        ''',
}
latex_logo = '_static/logo.png'
latex_show_urls = 'footnote'
