#!/bin/bash

for i in `seq 2 9`; 
do 
    echo $i ; 
    cp params_all_mc_array_spin_v_spincommon_20210524_r0.dat params_all_mc_array_spin_v_spincommon_20210524_r${i}.dat; 
    sed -i 's|real_0|real_'${i}'|g' params_all_mc_array_spin_v_spincommon_20210524_r${i}.dat; 
    sed -i 's|20210524_0|20210524_'${i}'|g' params_all_mc_array_spin_v_spincommon_20210524_r${i}.dat;
done

for i in params_all_mc_array_spin_v_spincommon_20210524_r*.dat;
do 
    echo $i;
    sed -i 's|zic006/ssb/ptasim/|zic006/pptadr2_gwb_crn_sims/|g' $i;
done
