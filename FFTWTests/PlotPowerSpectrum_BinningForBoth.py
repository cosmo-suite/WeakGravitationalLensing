from numpy import *
import matplotlib.pyplot as plt
import os

# Load data
data = loadtxt("k_vs_rho_k.txt")
k = data[:,0]
Pk = data[:,1]
Pk_exact = data[:,2]

# --- Logarithmic binning ---
num_bins = 30
kmin = k[k>0].min()  # ignore k=0
kmax = k.max()

bins = logspace(log10(kmin), log10(kmax), num_bins + 1)

# Arrays to store binned values
k_bin = []
Pk_bin = []
Pk_exact_bin = []

for i in range(num_bins):
    mask = (k >= bins[i]) & (k < bins[i+1])
    if mask.any():
        k_bin.append(mean(k[mask]))                  # mean k in this bin
        Pk_bin.append(mean(Pk[mask]))                # mean computed P(k)
        Pk_exact_bin.append(mean(Pk_exact[mask]))    # mean theoretical P(k) in the same bin

k_bin = array(k_bin)
Pk_bin = array(Pk_bin)
Pk_exact_bin = array(Pk_exact_bin)

# --- Plotting ---
plt.figure(figsize=(7,5))
plt.loglog(k, Pk, 'k', alpha=0.3, label='Computed (raw)')      # raw FFT data
plt.loglog(k_bin, Pk_bin, 'r-o', label='Computed (binned)')    # binned FFT
plt.loglog(k_bin, Pk_exact_bin, 'b-s', label='Theory (binned)')# binned theoretical spectrum

plt.xlabel(r'$k$', fontsize=15)
plt.ylabel(r'$P(k)$', fontsize=15)
plt.ylim([1e-10, 1e-3])
plt.legend()
plt.grid(True, which='both', ls='--', alpha=0.3)

# Save figure
directory = "Images"
if not os.path.exists(directory):
    os.makedirs(directory)
plt.savefig('./Images/kvsPk_binned.png')
plt.show()
