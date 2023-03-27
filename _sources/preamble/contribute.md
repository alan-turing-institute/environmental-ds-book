(pr-how-contribute)=
# Contribute

Contributions are welcome, and they are greatly appreciated! 
Every little bit helps, and credit will always be given. 
You can contribute in the ways listed below.

## Repository structure

The public GitHub repository has the following structure:

```
| The Environmental Data Science Book
| ├── **/.github**
| │   ├── ISSUE_template
| │   ├── workflows
| │   └── ...
| ├── **/book**
| │   ├── _toc.yml
| │   ├── _config.yml
| │   └── ...
| ├── CODE_OF_CONDUCT.md
| ├── CONTRIBUTING.md
| └── ...
```

The `.github folder` refers to GitHub related deployment files and templates of issues/pull requests usually curated by the repository maintainers or developers. 
The `book folder` holds the website content and other relevant files (table of content and configuration files).  

For the book content, the following contributions are accepted:
* **Narrative content**: include plain text, citations, equations, figures, special content blocks and more.
* **Executable content**: consists of computational material in a given programming language e.g. python.

:::{seealso}
Please visit the corresponding Jupyter Book guidelines for [`narrative`](https://jupyterbook.org/content/index.html#write-narrative-content) and [`executable`]('https://jupyterbook.org/execute/index.html#write-executable-content) content. 
:::

The `_toc.yml` file sets the main sections of EDS book. 
It is a simple configuration file specifying a table of content from all the executable and narrative content found in the ``book`` folder (and in subfolders). 
The current version of the book consists of five key sections:

* **Preamble**: contains narrative content i.e. plain markdown files describing the aims of the book, the target audience, attribution and how to contribute.
* **Notebooks**: contains all published executable content listed within a gridded gallery or with individual links. 
* **Publishing**: provides an introduction of open review, its relevance to computational notebooks and guidelines to publish in EDS book.
* **Community**: compiles community-related resources such as activities in various open science communities and shared notes of EDS book co-working meetings.
* **Afterword**: describes miscellaneous material such as bibliography. 

## Roles
Inspired by [the Turing Way Guide for Collaboration](https://github.com/alan-turing-institute/the-turing-way/blob/main/book/website/collaboration/collaboration.md), EDS book has the following defined community roles: 

* **Maintainers**: to provide support with keeping the existing source code updated by keeping track of new contributions and/or update versions of the Jupyter book.
* **Contributors**: to create/design narrative and/or executable content.
* **Reviewers**: to review narrative and/or executable content.
* **Readers/Users**: to read/share content, occasionally raise errors such as typos and bugs and fix them.

## Recognising Contributions
We welcome and recognise all kinds of contributions, from fixing small errors, to developing documentation, maintaining the project infrastructure, writing or reviewing narrative and/or executable notebooks.

_EDS book_ follows the [all-contributors](https://allcontributors.org) specifications.
The all-contributors bot usage is described [here](https://allcontributors.org/docs/en/bot/usage).
You can see a list of current contributors [here](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/contributors.md). 

# Code of Conduct
Please note that EDS book open-source repository and community are aligned with a [Contributor Code of Conduct](./../../CODE_OF_CONDUCT.md). 
By contributing to EDS book you agree to abide by its terms.