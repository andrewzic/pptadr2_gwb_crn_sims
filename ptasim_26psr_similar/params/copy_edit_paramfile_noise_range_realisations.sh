#!/bin/bash



for N in `seq 0 5`; 
do 
    echo $N ;
    for r in `seq 0 9`; 
    do 
	echo $r ;
	newpf=params_all_mc_array_spin_v_spincommon_N${N}_20210524_r${r}.dat
	cp params_all_mc_array_spin_v_spincommon_NX_20210524_rABC.dat $newpf;
	sed -i 's|XYZ|'${N}'|g' $newpf;
	sed -i 's|ABC|'${r}'|g' $newpf;
	#sed -i 's|zic006/ssb/ptasim/|zic006/pptadr2_gwb_crn_sims/|g' $newpf
    done
done

