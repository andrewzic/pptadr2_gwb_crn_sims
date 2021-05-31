import os
import numpy as np
import glob
import matplotlib.pyplot as plt
import gw_spectra_analytic as gwspec
from ptasim2enterprise import P02A
#import astropy.units as u

import sys

spec_globstr = sys.argv[1]

spec_files = sorted(glob.glob(spec_globstr))

spec_dir = os.path.dirname(spec_files[0]) + '/'

fig, (ax1) = plt.subplots(1,1)#,figsize=(10,7))#, xscale = 'log', yscale = 'log')

plt.sca(ax1)

for specf in spec_files:
    print(specf)
    spec = np.loadtxt(specf)
    freq = spec[:, 0]
    psd = spec[:, 1]
    plt.plot(freq, psd, label = os.path.splitext(os.path.basename(specf))[0])

ax1.legend()

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel(r'Frequency (day$^{{-1}}$)')
ax1.set_ylabel('PSD')

fig.tight_layout()
plt.savefig('{}_cholspec_similar.png'.format(spec_dir), dpi = 300, bbox_inches = 'tight', facecolor='white')
plt.show()
