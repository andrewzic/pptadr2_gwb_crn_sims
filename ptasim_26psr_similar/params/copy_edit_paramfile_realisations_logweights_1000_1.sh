#!/bin/bash

for i in `seq 0 9`; 
do 
    echo $i ; 
    cp params_all_mc_array_spin_v_spincommon_logweights_1000_1_20210524_rX.dat params_all_mc_array_spin_v_spincommon_logweights_1000_1_20210524_r${i}.dat; 
    sed -i 's|real_X|real_'${i}'|g' params_all_mc_array_spin_v_spincommon_logweights_1000_1_20210524_r${i}.dat; 
    sed -i 's|20210524_0|20210524_'${i}'|g' params_all_mc_array_spin_v_spincommon_logweights_1000_1_20210524_r${i}.dat;
done

