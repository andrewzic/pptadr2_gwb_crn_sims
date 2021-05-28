#!/bin/bash

for i in `seq 0 3`; 
do 
    echo $i ; 
    cp params_all_mc_array_spin_v_spincommon_NX_20210524.dat params_all_mc_array_spin_v_spincommon_N${i}_20210524.dat; 
    sed -i 's|XYZ|'${i}'|g' params_all_mc_array_spin_v_spincommon_N${i}_20210524.dat; 
done

for i in params_all_mc_array_spin_v_spincommon_N*_20210524.dat;
do 
    echo $i;
    sed -i 's|zic006/ssb/ptasim/|zic006/pptadr2_gwb_crn_sims/|g' $i;
done
