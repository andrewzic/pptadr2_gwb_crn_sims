import os
import numpy as np
import glob
import matplotlib.pyplot as plt
import gw_spectra_analytic as gwspec
from ptasim2enterprise import P02A
import astropy.units as u
import json
import sys

print("""usage: python publ_fig_cholspec.py "all_similar_regsamp/output/real_*/*.spec" "enterpirse_out/ptasim_ppta_mc_spin_vs_spincommon/all_similar_regsamp_20210524/" "psr_noise_vals/psr_noise_vals_1.dat" """)
plt.rcParams.update({
  "text.usetex": True,
  "font.family": "serif",
})

font = {'family' : 'serif',
        'size'   : 17}

spec_globstr = sys.argv[1]
enterprise_outdir = sys.argv[2]
input_psr_noise_file = sys.argv[3]

spec_files = sorted(glob.glob(spec_globstr))

spec_dir = os.path.dirname(spec_files[0]) + '/'

psr_list = np.loadtxt('./psrs.dat', dtype = 'str')
psr_noise_dict = json.load(open("{}/noisefiles/_credlvl.json".format(enterprise_outdir), "r"))

rednoise_log10_As = []
rednoise_gammas = []
for key, item in psr_noise_dict.items():
    if "red_noise" in key:
        if "gamma" in key:
            rednoise_gammas.append(item['50'])
        if "log10_A" in key:
            rednoise_log10_As.append(item['50'])

gw_gamma = psr_noise_dict["gw_gamma"]['50']
gw_log10_A = psr_noise_dict["gw_log10_A"]['50']

fig, (ax1) = plt.subplots(1,1, figsize = (6,5))# ,figsize=(10,7))#, xscale = 'log', yscale = 'log')
plt.sca(ax1)

spec_ch0s = [] #list for lowest frequency channel - storing for help setting ylims

for specf in spec_files:
    print(specf)
    spec = np.loadtxt(specf)
    freq = spec[:, 0]/86400.0
    psd = spec[:, 1]*((1.0*u.year).to(u.s).value)**3.0
    spec_ch0s.append(psd[0])
    plt.plot(freq, psd, label = os.path.splitext(os.path.basename(specf))[0], color = '#9E9E9E', linewidth = 0.5, alpha = 0.5)

#ax1.legend()

#plot the inferred common spectrum
crn_freq = np.logspace(np.log10(freq[0]/10.0), np.log10(freq[-1]*10.0), 1000)
crn_sp = gwspec.gw_spec(crn_freq*86400.0*365.25, 10.0**gw_log10_A, gw_gamma)*((1.0*u.year).to(u.s).value)**3.0
ax1.plot(crn_freq, crn_sp, linestyle = '-', label = '$\log_{{10}} \widehat{{A}}_{{}} = {:.2f}$\n $\widehat{{\gamma}}_{{}} = {:.2f}$'.format(gw_log10_A, gw_gamma), color = 'k') #linewidth = 3

input_psr_noise_vals = np.loadtxt(input_psr_noise_file)
input_gamms = input_psr_noise_vals[:, 0]
input_as = input_psr_noise_vals[:, 1]
input_wns = input_psr_noise_vals[:, 2]

_freq_ptasim = np.logspace(np.log10(spec[0,0]/10.0), np.log10(spec[-1,0]*10.0), 1000)*((1.0*u.year).to(u.day).value)
inp_psds = [( gwspec.ptasim_spec(_freq_ptasim, 0.01, a, g) ) * ( (1.0*u.year).to(u.s).value )**3.0 + w for a, g, w in zip(input_as, -input_gamms, input_wns)]
freq_ptasim = _freq_ptasim/( (1.0*u.year).to(u.s)).value
avg_inp_psd = np.average(inp_psds, weights = 1.0/input_wns**1.0, axis = 0)#*((1.0*u.year).to(u.s).value)**3.0

ax1.plot(freq_ptasim, avg_inp_psd, linestyle = '-', label = '$\overline{{P}}(f | A, \gamma ) + \overline{{\sigma}}$', color = '#1976D2', linewidth = 2.0, alpha = 1.0)

max_spec_ch0 = np.amax(spec_ch0s)
min_spec_ch0 = np.amin(spec_ch0s)

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel(r'$\mathrm{Frequency~[Hz]}$', fontdict=font)
ax1.set_ylabel(r'$P~\mathrm{{[s}}^3\mathrm{{]}}$', fontdict = font)
ax1.tick_params(axis='y', labelsize = font['size'])
ax1.tick_params(axis='x', labelsize = font['size'])
ax1.set_ylim(10**(int(np.log10(ax1.get_ylim()[0]))), 10**(int(np.log10(max_spec_ch0))))

ax1.set_xlim(10**(int(np.log10(freq[0])-1)), 1E-7)
ax1.set_ylim(10**(int(np.log10(min_spec_ch0))-4), 10**(int(np.log10(max_spec_ch0))))
#ax1.set_xlim(10**(int(np.log10(ax1.get_xlim()[0]) - 1)),1E-7)




fig.tight_layout()
plt.savefig('{}_publ_cholspec.png'.format(enterprise_outdir), dpi = 300, bbox_inches = 'tight', facecolor='white')
plt.savefig('{}/_publ_cholspec.pdf'.format(enterprise_outdir), dpi = 300, bbox_inches = 'tight', facecolor='white')
#plt.show()
print('{}/_publ_cholspec.pdf'.format(enterprise_outdir))
plt.show()

