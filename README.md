**[summary](#summary) | [contents](#contents) | [usage](#usage) | [running the notebooks](#running-the-notebooks) | [issues](#issues) | [citation](#citation) | [license](#license)**

# A physical property model for a fractured volume of rock

[![Build Status](https://travis-ci.org/simpeg-research/heagy-2018-fracture-physprops?branch=master)](https://travis-ci.org/simpeg-research/heagy-2018-fracture-physprops)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/simpeg-research/heagy-2018-fracture-physprops/master)
[![Azure](https://notebooks.azure.com/launch.png)](https://notebooks.azure.com/import/gh/simpeg-research/heagy-2018-fracture-physprops)
[![License](https://img.shields.io/github/license/simpeg-research/heagy-2018-fracture-physprops.svg)](https://github.com/simpeg-research/heagy-2018-fracture-physprops/blob/master/LICENSE)
[![SimPEG](https://img.shields.io/badge/powered%20by-SimPEG-blue.svg)](http://simpeg.xyz)

## Summary

This repository contains the notebooks used to generate the examples shown in Chapter 2
of the thesis "Electromagnetic methods for imaging subsurface injections" by [Lindsey J. Heagy](https://github.com/lheagy)

<img src="figures/emt_spherical_particles.png" width=40% align="middle">

## Contents

- [notebooks](notebooks):
    - [1_proppant_fluid_mixture.ipynb](/notebooks/1_proppant_fluid_mixture.ipynb)
    - [2_emt_fractures.ipynb](/notebooks/2_emt_fractures.ipynb)
    - [3_crosswell_survey.ipynb](/notebooks/3_crosswell_survey.ipynb)

## Usage

### Online
The notebooks can be run online through [mybinder](https://mybinder.org/v2/gh/simpeg-research/heagy-2018-fracture-physprops/master) or [azure notebooks](https://notebooks.azure.com/import/gh/simpeg-research/heagy-2018-fracture-physprops).

### Locally
To run them locally, you will need to have python installed, preferably through [anaconda](https://www.anaconda.com/download/).

You can then clone this reposiroty. From a command line, run

```
git clone https://github.com/simpeg-research/heagy-2018-fracture-physprops.git
```

Then `cd` into the `heagy-2018-fracture-physprops`

```
cd heagy-2018-fracture-physprops
```

To setup your software environment, we recommend you use the provided conda environment

```
conda env create -f environment.yml
source activate fracture-physprops-environment
```

alternatively, you can install dependencies through pypi
```
pip install -r requirements.txt
```

You can then launch Jupyter
```
jupyter notebook
```

Jupyter will then launch in your web-browser.

## Running the notebooks

Each cell of code can be run with `shift + enter` or you can run the entire notebook by selecting `cell`, `Run All` in the toolbar.

<img src="https://raw.githubusercontent.com/simpeg-research/heagy-2018-emcyl/master/figures/cell_run_all.png" width=80% align="middle">

For more information on running Jupyter notebooks, see the [Jupyter Documentation](https://jupyter.readthedocs.io/en/latest/)

## Issues

If you run into problems or bugs, please let us know by [creating an issue](https://github.com/simpeg-research/heagy-2018-fracture-physprops/issues/new) in this repository.

## Citation

coming soon...

## License

These notebooks are licensed under the [MIT License](/LICENSE) which allows academic and commercial re-use and adaptation of this work.
