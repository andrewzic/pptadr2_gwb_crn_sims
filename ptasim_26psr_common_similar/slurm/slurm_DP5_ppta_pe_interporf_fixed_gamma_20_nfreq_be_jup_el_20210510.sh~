#!/bin/bash
#SBATCH --job-name=DP5_ppta_pe_interporf_fixgam_20nfreq_be_jup_el
#SBATCH --output=/flush5/zic006/ephemeris_sims/slurm_logs/DP5_ppta_pe_interporf_fixed_gamma_7_nfreq_be_jup_el_20210510_%A_%a.log
#SBATCH --ntasks=10
#SBATCH --time=1-21:30
#SBATCH --mem-per-cpu=7G
#SBATCH --tmp=8G
##SBATCH --array=0-25

# pyv="$(python -c 'import sys; print(sys.version_info[0])')"
# if [ "$pyv" == 2 ]
# then
#     echo "$pyv"
#     module load numpy/1.16.3-python-2.7.14
# fi


module load singularity

singularity exec /home/zic006/psr_gwb.sif which python3
singularity exec /home/zic006/psr_gwb.sif echo $TEMPO2
singularity exec /home/zic006/psr_gwb.sif echo $TEMPO2_CLOCK_DIR

singularity exec /home/zic006/psr_gwb.sif python3 /flush5/zic006/ephemeris_sims/run_analysis.py --prfile "/flush5/zic006/ephemeris_sims/params/params_DP5_ppta_pe_interporf_fixed_gamma_20nfreq_be_jup_el_20210510.dat"
