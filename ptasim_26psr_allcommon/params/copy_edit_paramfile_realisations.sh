#!/bin/bash

for i in `seq 0 9`; 
do 
    echo $i ; 
    cp params_all_mc_array_spin_v_spincommon_20210531_rX.dat params_all_mc_array_spin_v_spincommon_20210531_r${i}.dat; 
    sed -i 's|real_X|real_'${i}'|g' params_all_mc_array_spin_v_spincommon_20210531_r${i}.dat; 
    sed -i 's|20210531_X|20210531_'${i}'|g' params_all_mc_array_spin_v_spincommon_20210531_r${i}.dat;
done

for i in params_all_mc_array_spin_v_spincommon_20210531_r*.dat;
do 
    echo $i;
    sed -i 's|zic006/ssb/ptasim/|zic006/pptadr2_gwb_crn_sims/|g' $i;
done
