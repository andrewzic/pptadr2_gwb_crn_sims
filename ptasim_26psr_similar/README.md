NOTES:

- simulated datasets w/ different ranges of injected red noise spectra are in allsimilar_regsamp_<N>
  	    - N	           = [0,    1,     2,     3,   4,   5 ]
  	    - alpha_uppers = [-4,  -3,  -2.8,  -2.4,  -2,  -1 ]
	    - alpha_lowers = [-4,  -5,  -5.2,  -5.6,  -6,  -7 ]
	    - p0_uppers    = [-23, -22, -21.8, -21.5, -21, -20]
	    - p0_lowers    = [-23, -24, -24.2, -24.5, -25, -26]

- Generate noise vals by running `python generate_prs_noise_vals_all.py`. This should write a noise dat file into the psr_noise_vals/ dir
- Run ptaSimulate using run_ptasim_all_noise.csh
- generate cholspec model input files using make_input_model_files.py
- run cholspec plugin and plot using run_cholspec_plot_cholspec.csh with input argument glob string pointing to realisation directories e.g. allsimilar_regsamp_1/output/real_*
- plot all cholesky spectra with publ_fig_cholspec.py (usage in script)
- plot log10_A, gamma posteriors with publ_fig_log10A_gamma.py