
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.chebyshev import Chebyshev
import json

n_samples = 500
x = np.linspace(0, 1, n_samples)
y = x**2
np.save('toy_x.npy', x)
np.save('toy_y.npy', y)

def cheb_basis(x, k):
    X = 2 * x - 1
    return np.array([Chebyshev.basis(d)(X) for d in range(k)]).T

k_max = 20
B = cheb_basis(x, k_max)
coeffs = np.linalg.lstsq(B, y, rcond=None)[0]
np.save('toy_cheb_coeffs.npy', coeffs)

errors = []
for N in range(1, k_max+1):
    y_approx = B[:, :N] @ coeffs[:N]
    error = np.sqrt(np.mean((y - y_approx)**2))
    errors.append(error)
errors = np.array(errors)
np.save('toy_certificate_errors.npy', errors)
N_cert = int(np.min(np.where(errors < 0.01)) + 1)

plt.figure()
plt.plot(np.arange(1, k_max+1), errors, 'o-')
plt.axhline(0.01, color='r', ls='--', label='L2 Error = 0.01')
plt.xlabel('Number of Chebyshev terms (N)')
plt.ylabel('L2 Error')
plt.title(r'Chebyshev Certificate Error Decay for $f(x) = x^2$')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('toy_error_decay.png')
plt.close()

y_cert = B[:, :N_cert] @ coeffs[:N_cert]
plt.figure()
plt.plot(x, y, label='True $f(x)=x^2$')
plt.plot(x, y_cert, '--', label=f'Chebyshev approx (N={N_cert})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Certificate Approximation vs. True Function')
plt.legend()
plt.tight_layout()
plt.savefig('toy_cheb_reconstruction.png')
plt.close()

toy_stats = {
    "n_samples": n_samples,
    "k_max": int(k_max),
    "N_cert_0.01": int(N_cert),
    "L2_error_at_N_cert": float(errors[N_cert-1]),
    "certificate_errors_first_10": errors[:10].tolist(),
    "cheb_coeffs_first_5": coeffs[:5].tolist()
}
with open('toy_stats_summary.json', 'w') as f:
    json.dump(toy_stats, f, indent=2)
print("All toy certificate files generated!")
