#!/bin/bash
#SBATCH --job-name=tar_out
#SBATCH --output=/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_similar/slurm_logs/tar_out_%A_%a.log
#SBATCH --ntasks=1
#SBATCH --time=0-02:00:00
#SBATCH --mem-per-cpu=7G
#SBATCH --tmp=8G
##SBATCH --array=0

# pyv="$(python -c 'import sys; print(sys.version_info[0])')"
# if [ "$pyv" == 2 ]
# then
#     echo "$pyv"
#     module load numpy/1.16.3-python-2.7.14
# fi

tar -cvf '/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_similar/enterprise_out.tar.gz' '/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_similar/enterprise_out/'

# module load singularity

# singularity exec /home/zic006/psr_gwb.sif which python3
# singularity exec /home/zic006/psr_gwb.sif echo $TEMPO2
# singularity exec /home/zic006/psr_gwb.sif echo $TEMPO2_CLOCK_DIR

# echo $SLURM_ARRAY_TASK_ID

# echo "/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_similar/params/params_all_pe_array_spin_20210524_r"$SLURM_ARRAY_TASK_ID".dat"
# singularity exec /home/zic006/psr_gwb.sif python3 /flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_similar/run_enterprise_simple.py --prfile "/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_similar/params/params_all_pe_array_spin_20210524_r"$SLURM_ARRAY_TASK_ID".dat"
