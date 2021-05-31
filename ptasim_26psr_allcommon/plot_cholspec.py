import os
import numpy as np
import glob
import matplotlib.pyplot as plt
import gw_spectra_analytic as gwspec
from ptasim2enterprise import P02A
import astropy.units as u
print(10**P02A(8.0E-23, 0.01, 5.5))
spec_files = sorted(glob.glob('J[012]*.spec'))


fig, (ax1) = plt.subplots(1,1,figsize=(10,7))#, xscale = 'log', yscale = 'log')

plt.sca(ax1)
ax1.set_title('All pulsars with similar noise')
for specf in spec_files:
    print(specf)
    spec = np.loadtxt(specf)
    freq = spec[:, 0]
    psd = spec[:, 1]
    plt.plot(freq, psd, label = os.path.splitext(os.path.basename(specf))[0])

# plt.sca(ax2)
# ax2.set_title('J1713+0747 with weaker, shallower spin noise')
# spec_files = sorted(glob.glob('all-1_common_regsamp/timfiles/J[012]*.spec'))
# for specf in spec_files:
#     spec = np.loadtxt(specf)
#     freq = spec[:, 0]
#     psd = spec[:, 1]
#     plt.plot(freq, psd)#, label = os.path.splitext(os.path.basename(specf))[0])

    
ax1.legend()
for ax in [ax1]:#, ax2]:
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'Frequency (day$^{{-1}}$)')
    ax.set_ylabel('PSD')
    ax.set_ylim(1E-33, 1E-24)
    ax.set_xlim(10**(int(np.log10(freq[0]))-1.0), 1E-2)#freq[-1])
    #ax.axvline(1.0/40.0/2.0, ls = '--', c = 'k', alpha = 0.5)

#    "gw_gamma": 4.655765635261815,
#    "gw_log10_A": -15.176018932965718,
#    "nmodel": 0.2599923902636294
    
#ax1.plot(freq, gwspec.gw_spec(freq*365.25, 10**-15.176018932965718, 4.655765635261815), c = 'k', linewidth = 2.0)
psrs = ["J0437-4715", "J1600-3053", "J1022+1001", "J1713+0747", "J1744-1134", "J1909-3744", "J2145-0750", "J2241-5236"]
# gammas = []
# log10_As = []
# psr_noise_dict = {"J0437-4715_red_noise_gamma": 0.7978128179679721,
#                   "J0437-4715_red_noise_log10_A": -19.62328545188724,
#                   "J1022+1001_flag_efac": 0.9240074019760486,
#                   "J1022+1001_red_noise_gamma": 0.8005349364336569,
#                   "J1022+1001_red_noise_log10_A": -19.096707459615054,
#                   "J1600-3053_flag_efac": 0.9913271356861476,
#                   "J1600-3053_red_noise_gamma": 0.002703207502748217,
#                   "J1600-3053_red_noise_log10_A": -19.86691950051866,
#                   "J1713+0747_flag_efac": 0.9991045248767136,
#                   "J1713+0747_red_noise_gamma": 2.6080960340632338,
#                   "J1713+0747_red_noise_log10_A": -18.349702223363735,
#                   "J1744-1134_flag_efac": 1.0356291365199004,
#                   "J1744-1134_red_noise_gamma": 0.001094188598939283,
#                   "J1744-1134_red_noise_log10_A": -19.61249669924953,
#                   "J1909-3744_flag_efac": 0.9992451018113377,
#                   "J1909-3744_red_noise_gamma": 3.1874013163546104,
#                   "J1909-3744_red_noise_log10_A": -19.869801589918442,
#                   "J2145-0750_flag_efac": 0.9450606311287273,
#                   "J2145-0750_red_noise_gamma": 2.7992934115014485,
#                   "J2145-0750_red_noise_log10_A": -19.866615980612305,
#                   "J2241-5236_flag_efac": 1.0777624757854007,
#                   "J2241-5236_red_noise_gamma": 0.6019924430510368,
#                   "J2241-5236_red_noise_log10_A": -17.749353103296126
# }

# for key, item in psr_noise_dict.items():
    
#     if "gamma" in key:
#         gammas.append(item)
#     if "log10_A" in key:
#         log10_As.append(item)

#for psr, gamma, log10_A in zip(psrs, gammas, log10_As):
#    ax2.plot(freq, gwspec.gw_spec(freq*365.25, 10.0**log10_A, gamma), linestyle = '--', label = psr)
#    ax2.legend()

#common noise params in SN + CRN model
#ax2.plot(freq, gwspec.gw_spec(freq*365.25, 10.0**-15.455484441085986, 5.194386924508992), color = 'k', linestyle = '--', linewidth = 2.0, label = 'CRN + SN model')


"""    
    "gw_gamma": 5.194386924508992,
    "gw_log10_A": -15.455484441085986,
"""

#ax2.plot(freq, gwspec.gw_spec(freq*365.25, 10.0**-15.176018932965718, 4.655765635261815), color = 'b', linestyle = '--', linewidth = 2.0, label = 'CRN-only model')

"""
"gw_gamma": 4.655765635261815,
    "gw_log10_A": -15.176018932965718,
"""
print(10**P02A(8.0E-23, 0.01, 5.5))
print(10**P02A(1.5E-28, 0.01, 1.5))

#ax2.plot(freq, gwspec.ptasim_spec(freq*365.25, 0.01, 1.5E-28, 1.5), ls = '-', linewidth = 3.0, c = 'C3', label = 'Simulated J1713+0747 PSD')

#ax2.plot(freq, gwspec.ptasim_spec(freq*365.25, 0.01, 8E-23, 5.5), ls = '-', linewidth = 4.0, c = 'k', label = 'Simulated CRN PSD')

#ax2.plot(freq, gwspec.gw_spec(freq*365.25, 10**P02A(8E-23, 0.01, 5.5), 5.5), ls = '--', linewidth = 4.0, c = 'k')
#ax1.plot(freq, gwspec.ptasim_spec(freq*365.25, 0.01, 8E-23, 5.5), ls = '-', linewidth = 4.0, c = 'k')
ax1.legend()
#ax2.legend()
fig.tight_layout()
plt.savefig('cholspec_similar.png', dpi = 300, bbox_inches = 'tight', facecolor='white')
plt.show()
