**[summary](#Summary) | [contents](#Contents) | [usage](#Usage) | [running the notebooks](#Running-the-notebooks) | [citation](#Citation) | [issues](#Issues) |  [license](#License)**

# A physical property model for a fractured volume of rock

[![Build Status](https://travis-ci.org/simpeg-research/heagy-2018-fracture-physprops.svg?branch=master)](https://travis-ci.org/simpeg-research/heagy-2018-fracture-physprops)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/simpeg-research/heagy-2018-fracture-physprops/master)
[![Azure](https://notebooks.azure.com/launch.png)](https://notebooks.azure.com/import/gh/simpeg-research/heagy-2018-fracture-physprops)
[![License](https://img.shields.io/github/license/simpeg-research/heagy-2018-fracture-physprops.svg)](https://github.com/simpeg-research/heagy-2018-fracture-physprops/blob/master/LICENSE)
[![SimPEG](https://img.shields.io/badge/powered%20by-SimPEG-blue.svg)](http://simpeg.xyz)

## Summary

This repository contains the notebooks used to generate the examples shown in Chapter 2
of the thesis ["Electromagnetic methods for imaging subsurface injections"](https://github.com/lheagy/phd-thesis) by [Lindsey J. Heagy](https://github.com/lheagy). 

In hydraulic a fracturing operation, fluid is injected into the reservoir to fracture the rock and provide pathways for hydrocarbons to flow. In order to keep the fracture pathways open, sand or ceramic particles, known as proppant are also injected. One of the unknowns in fracturing operations is where the proppant goes. If the proppant were electrically conductive (e.g. by coating it with graphite), then electromagnetic (EM) methods can be used to detect the proppant. The first step to examining the feasibility of using EM methods for delineating the propped region of the reservoir is construcing an electrical conductivity model that can be used for numerical simulations. 

To estimate the conductivity of afractured volume of rock, 
I use effective medium theory in two steps. First, I estimate the conductivity of a mixture of proppant and fluid and second, I estimate the conductivity of a fractured volume of rock. In the final notebook, I perform a simulation of cross-well electromagntic data to demonstrate feasibility of using electromagnetic methods for detecting a propped, fractured volume of rock. 

<img src="https://raw.githubusercontent.com/lheagy/phd-thesis/master/thesis/figures/phys_prop_model/effective_medium_theory.png" width=60% align="middle">

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

## Citation

Heagy, L. J. (2018). Electromagnetic methods for imaging subsurface injections (T). University of British Columbia. Retrieved from https://open.library.ubc.ca/collections/ubctheses/24/items/1.0374170

```
@phdthesis{Heagy_2018, 
    series={Electronic Theses and Dissertations (ETDs) 2008+}, 
    title={Electromagnetic methods for imaging subsurface injections}, 
    url={https://open.library.ubc.ca/collections/ubctheses/24/items/1.0374170}, 
    DOI={http://dx.doi.org/10.14288/1.0374170}, 
    school={University of British Columbia}, 
    author={Heagy, Lindsey J.}, 
    year={2018}, 
    collection={Electronic Theses and Dissertations (ETDs) 2008+}
}
```

## Issues

If you run into problems or bugs, please let us know by [creating an issue](https://github.com/simpeg-research/heagy-2018-fracture-physprops/issues/new) in this repository.

## License

These notebooks are licensed under the [MIT License](/LICENSE) which allows academic and commercial re-use and adaptation of this work.
