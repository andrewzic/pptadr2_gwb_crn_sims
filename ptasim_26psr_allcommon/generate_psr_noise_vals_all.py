import numpy as np
import matplotlib.pyplot as plt
import os

psr_list = np.loadtxt('psrs.dat', dtype = 'str')

N_psr = len(psr_list)

np.random.seed(seed = 20210531)

ptasim_inp_template_fn = 'ptasim_all-1_common_26_template.inp'
ptasim_inp_template_f = open(ptasim_inp_template_fn, 'r')
ptasim_inp_template_str = ptasim_inp_template_f.read()

#print(ptasim_inp_template.format('test', 'ts', '2ff'))

#N = [0, 1, 10, 11, 2, 3]

alpha = -5.5
p0 = (8e-23)

alpha_low = -1.5

p0_lows = [(1.5e-28), (5e-29), (1e-29), (1e-31)]
p0_low = p0_lows[0]

low_list = ["J1713+0747"]

toaerrs = np.random.uniform(9e-8, 5e-7, size = N_psr)

toaerrs_low = np.random.uniform(3e-8, 9e-8, size = N_psr)

toaerrs_lows = [toaerrs_low, np.random.uniform(1e-8, 3e-8, size = N_psr), np.random.uniform(8e-9, 1e-8, size = N_psr), np.random.uniform(9e-10, 3e-9, size = N_psr)]

fmt_str_tnoise = "tnoise: psr={:s},alpha={:.1f},p0={:.1e},fc=0.01\n"
fmt_str_obs = "observe: psr={:s},toaerr={:.1e},freq=1400\n"
fmt_str_dat = "{:.4f}\t{:.4e}\t{:.4e}\n"
    
str_tnoise = ''
for psr in psr_list:
    if psr in low_list:
        str_tnoise += fmt_str_tnoise.format(psr, alpha_low, p0_low)
    else:
        str_tnoise += fmt_str_tnoise.format(psr, alpha, p0)

        
str_obs = ''
for psr, toaerr, toaerr_low in zip(psr_list, toaerrs, toaerrs_low):
    if psr in low_list:
        str_obs += fmt_str_obs.format(psr, toaerr_low)
    else:
        str_obs += fmt_str_obs.format(psr, toaerr)

    
if not os.path.exists('ptasim_all-1_common_26.inp'):
    with open('ptasim_all-1_common_26.inp', 'w') as ptasim_inp_f:
        ptasim_inp_f.write(ptasim_inp_template_str.format(str_tnoise, str_obs))
        ptasim_inp_f.close()
        
with open('psr_noise_vals_all-1_common.dat', 'w') as psr_datf:
    for psr, toaerr, toaerr_low in zip(psr_list, toaerrs, toaerrs_low):
        if psr in low_list:
            psr_datf.write(fmt_str_dat.format(alpha_low, p0_low, toaerr_low))
        else:
            psr_datf.write(fmt_str_dat.format(alpha, p0, toaerr))
    psr_datf.close()
        
#plt.scatter(alphas, p0s)

#plt.show()
