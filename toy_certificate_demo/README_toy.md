# Toy Certificate Extraction & Chebyshev Analysis

This package demonstrates certificate-driven function approximation for the toy function $f(x) = x^2$ on [0,1], using Chebyshev polynomials as basis.

## Files
- `toy_x.npy`: 500 x-points in [0,1]
- `toy_y.npy`: $f(x) = x^2$ at those points
- `toy_cheb_coeffs.npy`: Chebyshev coefficients for $k=20$
- `toy_certificate_errors.npy`: L2 error for N=1..20 Chebyshev terms
- `toy_error_decay.png`: Error decay plot
- `toy_cheb_reconstruction.png`: Certificate vs. true function
- `toy_stats_summary.json`: Summary of certificate size, errors, coeffs

## To Reproduce
1. `pip install numpy matplotlib`
2. Run `make_toy_certificates.py`

This code and data allow certificate extraction, error validation, and visual demonstration of spectral approximation.
