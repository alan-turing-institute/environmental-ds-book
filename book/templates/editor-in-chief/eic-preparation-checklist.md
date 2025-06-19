(templates-eic-preparation-checklist)=

```markdown
## Check notebook repository
- [ ] The notebook repository is available in a public personal repository
- [ ] The notebook runs in Binder according to the PR indicated by the author

## Set up Quay.io credentials
- [ ] Set `QUAY_PASSWORD` and `QUAYUSERNAME` keys and values in the repository secrets (go to to the repository settings, left panel > Secret and variables > Actions)

## Filename and README
- [ ] Create and checkout a new branch `preparation`
- [ ] Commit and push the following changes:
  - [ ] Rename the filename of the template to notebook.ipynb
  - [ ] Fill `notebook_name` and `quay_image` keys in the `config.json` file
  - [ ] Copy README template ([python](eic-readme-python.md), R, Julia) and replace the fields in the following lines:
    - [ ] replace `[repository name]` in 
      - [ ] L16, `<a href="https://github.com/eds-book/[repository name]/blob/main/LICENSE">`
      - [ ] L19, `<a href="https://notebooks.gesis.org/binder/v2/gh/eds-book/[repository name]/main?labpath=notebook.ipynb">`
      - [ ] L22, `<a href="https://github.com/eds-book/[repository name]/actions/workflows/publish.yml/badge.svg">`
      - [ ] L23, `<img alt="Continuous integration badge" src="https://github.com/eds-book/[repository name]/actions/workflows/publish.yml/badge.svg">`
      - [ ] L49, `git clone https://github.com/eds-book/[repository name].git`
      - [ ] L54, `cd [repository name]`
      - [ ] L60, `conda activate [repository name]`
    - [ ] replace `[rohub_w3id]` in L29
- [ ] Merge the new branch to main

## PRE-REVIEW
- [ ] Open a PRE-REVIEW issue
- [ ] Fill the required fields.  
- [ ] Validate reviewers interest and availability
- [ ] Close the PRE-REVIEW

## REVIEW
- [ ] Open a REVIEW issue
- [ ] Fill the required fields   
- [ ] Add reviewers
- [ ] Provide details of the notebook using [cloc](https://github.com/AlDanial/cloc).

```