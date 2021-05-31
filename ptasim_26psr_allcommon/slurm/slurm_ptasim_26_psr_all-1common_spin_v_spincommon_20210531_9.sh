#!/bin/bash
#SBATCH --job-name=ppta_ptasim_26psr_all-1_common_mc_spin_v_spincommon_4_9
#SBATCH --output=/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_allcommon/slurm_logs/ppta_ptasim_26psr_all-1_common_mc_spin_v_spincommon_20210531_%A_%a.log
#SBATCH --ntasks=10
#SBATCH --time=0-12:00:00
#SBATCH --mem-per-cpu=7G
#SBATCH --tmp=8G
#SBATCH --array=9

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

echo $SLURM_ARRAY_TASK_ID

echo "/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_allcommon/params/params_all_mc_array_spin_v_spincommon_20210531_r"$SLURM_ARRAY_TASK_ID".dat"
singularity exec /home/zic006/psr_gwb.sif python3 /flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_allcommon/run_enterprise_simple.py --prfile "/flush5/zic006/pptadr2_gwb_crn_sims/ptasim_26psr_allcommon/params/params_all_mc_array_spin_v_spincommon_20210531_r"$SLURM_ARRAY_TASK_ID".dat"
