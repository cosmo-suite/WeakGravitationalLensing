from numpy import *
import matplotlib.pyplot as plt
import os

# Load data
data = loadtxt("k_vs_rho_k.txt")
k = data[:,0]
Pk = data[:,1]
Pk_exact = data[:,2]

# --- Logarithmic binning ---
num_bins = 50  # choose number of bins
kmin = k[k>0].min()  # ignore k=0
kmax = k.max()

# Create logarithmic bins
bins = logspace(log10(kmin), log10(kmax), num_bins + 1)

# Arrays to store binned values
k_bin = []
Pk_bin = []

# Bin the data
for i in range(num_bins):
    mask = (k >= bins[i]) & (k < bins[i+1])
    if mask.any():  # make sure there are points in this bin
        k_bin.append(mean(k[mask]))          # mean k in this bin
        Pk_bin.append(mean(Pk[mask]))        # mean P(k) in this bin

k_bin = array(k_bin)
Pk_bin = array(Pk_bin)

# --- Plotting ---
plt.figure(1)
plt.loglog(k, Pk, 'k', alpha=0.3, label='Computed')      # raw data, semi-transparent
plt.loglog(k_bin, Pk_bin, 'r-o', label='Binned')          # binned average
plt.loglog(k, Pk_exact, 'ok', label='Specified')          # exact/theory
plt.xlabel(r'$k$', fontsize=15)
plt.ylabel(r'$P(k)$', fontsize=15)
plt.ylim([1e-10,1e-3])
plt.legend()

# Save figure
directory = "Images"
if not os.path.exists(directory):
    os.makedirs(directory)
plt.savefig('./Images/kvsPk.png')
plt.show()

