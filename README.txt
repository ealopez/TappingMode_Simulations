
This repository contains code for the simulation of an atomic force microscopy probe (parabolic) penetrating a viscoelastic surface containing multiple characteristic times.
The contact mechanics are performed following two main frameworks:

- The case for a monotonic increase of contact radius. (Lee, E. Ho, and Jens Rainer Maria Radok. "The contact problem for viscoelastic bodies."
 Journal of Applied Mechanics 27, no. 3 (1960): 438-444.)

- The general case of arbitrary loading history. (Ting, Thomas Chi-tsai. 
"The contact stresses between a rigid indenter and a viscoelastic half-space." ASME, 1966.)



Repository structure:
The repository contains three main folders: Epoxy, PC, PIB containing simulations for the case of Epoxy, polycarbonate, and polyisobutylene, respectively.
Each folder has the same internal structure:

- AFM_lib.py  --> This is the library containing the main functions to make the simulations.
- AFM_calculations  --> This library contains functions to perform postprocessing of simulations data such as calculation of amplitude and phase of the tip trajectory.
- Simulation_SoftMatter_1stMode.ipynb  --> This jupyter notebook performs the simulations for single tapping mode with the 1st mode excited
- Simulation_SoftMatter_2ndMode.ipynb --> This jupyter notebook performs the simulations for single tapping mode with the 2nd mode excited
- Simulation_SoftMatter_Bimodal.ipynb --> This jupyter notebook performs the simulations for bimodal tapping mode with the 1st and 2nd modes excited
- PIB.txt (or Epoxy.txt, PC.txt) -- > contains the values of the Generalized Maxwell parameters (left column relaxation times, right column moduli of each arm)


The simulations inside the PIB folder correspond to the results published in:
Nikfarjam, M., López-Guerra, E. A., Solares, S. D., & Eslami, B. (2018). Imaging of viscoelastic soft 
matter with small indentation using higher eigenmodes in single-eigenmode amplitude-modulation atomic force microscopy. 
Beilstein journal of nanotechnology, 9, 1116.

The code associated to this repository may be cited as:

ealopez (2017) elopez/TappingMode_Simulations.
https://zenodo.org/record/1087460.