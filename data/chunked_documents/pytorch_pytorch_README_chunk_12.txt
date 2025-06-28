---
repo: pytorch/pytorch
readme_filename: pytorch_pytorch_README.md
stars: 91087
forks: 24541
watchers: 91087
contributors_count: 322
license: NOASSERTION
Header 2: Installation
Header 3: Building the Documentation
---
To build documentation in various formats, you will need Sphinx
and the pytorch_sphinx_theme2.  
Before you build the documentation locally, ensure `torch` is
installed in your environment. For small fixes, you can install the
nightly version as described in Getting Started.  
For more complex fixes, such as adding a new module and docstrings for
the new module, you might need to install torch from source.
See Docstring Guidelines
for docstring conventions.  
```bash
cd docs/
pip install -r requirements.txt
make html
make serve
```  
Run `make` to get a list of all available output formats.  
If you get a katex error run `npm install katex`.  If it persists, try
`npm install -g katex`  
> [!NOTE]
> If you installed `nodejs` with a different package manager (e.g.,
> `conda`) then `npm` will probably install a version of `katex` that is not
> compatible with your version of `nodejs` and doc builds will fail.
> A combination of versions that is known to work is `node@6.13.1` and
> `katex@0.13.18`. To install the latter with `npm` you can run
> ```npm install -g katex@0.13.18```  
> [!NOTE]
> If you see a numpy incompatibility error, run:
> ```
> pip install 'numpy ```  
When you make changes to the dependencies run by CI, edit the
`.ci/docker/requirements-docs.txt` file.  
#### Building a PDF  
To compile a PDF of all PyTorch documentation, ensure you have
`texlive` and LaTeX installed. On macOS, you can install them using:  
```
brew install --cask mactex
```  
To create the PDF:  
1. Run:  
```
make latexpdf
```  
This will generate the necessary files in the `build/latex` directory.  
2. Navigate to this directory and execute:  
```
make LATEXOPTS="-interaction=nonstopmode"
```  
This will produce a `pytorch.pdf` with the desired content. Run this
command one more time so that it generates the correct table
of contents and index.  
> [!NOTE]
> To view the Table of Contents, switch to the **Table of Contents**
> view in your PDF viewer.