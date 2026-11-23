# Computational Simulation of the Ising Model

Python implementation of the 2D Ising model using Markov Chain Monte Carlo (MCMC) methods (Metropolis–Hastings algorithm) to investigate ferromagnetic phase transitions and spin dynamics.

Developed over a one-week seminar on the computational simulation of magnetism as part of the Heidelberger Life-Science Lab at the German Cancer Research Center (DKFZ).

> **Status:** Archived seminar project — cleaned up for reference.

<p align="center">
  <img src="figures/preview.png" alt="2D Ising model MCMC spin simulation preview" width="500" />
  <br />
  <em>2D Ising model MCMC simulation preview (see <code>figures/anim-3.mp4</code> for the full animation).</em>
</p>

## Repository Contents

- `main.py` — Stand-alone Python implementation of the MCMC Ising simulation and observable measurements
- `*.ipynb` — Seminar Jupyter notebook containing theoretical background and guided exercises (provided by the seminar host)
- `figures/` — Generated plots and animations, including `preview.png` and `anim-3.mp4`
- Presentation slides prepared for the DKFZ Theoretical Physics Working Group

## Prerequisites

Originally written without strict pinned version numbers.

- **Python:** 3.8+
- **Libraries:** `numpy`, `matplotlib`

## Getting Started

1. Install dependencies:
   ```bash
   pip install numpy matplotlib
