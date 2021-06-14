Shipping Python Apps using Podman
=================================

> Set up a Development Environment using Red Hat Container Tools

A quick introduction to Red Hat Container Tools for Pythonistas.
Building and running Python applications using Podman.
Exploring the manner containers benefit developers.

Speaker(s)
---------

### Elif MOSESSOHN-SAMEDIN

DevOps (Automation) Engineer with experience in Infrastructure Optimization and Management. Red Hat Certified Architect in Infrastructure. Advocate for Continuous Learning, Open Source Communities, and Technical Innovation. Espresso Addict.


Building the documentation
--------------------------

Building the presentation requires `pandoc` and `LaTeX` (for PDF output only).

As an alternative, a prebuild image with all required tools is provided on quay.io.

https://quay.io/repository/cmihai/docbuilder

To build the presentation:

```bash
# To build a PowerPoint presentation using pandoc:
make

# To build a PDF using LaTeX beamer:
make TRANSFORMATION=pdf
```

Note: when installing pandoc, make sure you're using the latest version from: https://pandoc.org/installing.html
