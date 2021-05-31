#!/bin/tcsh

set psrlist=$PWD"/psrs.dat"

set basedir=$PWD

set echo_path=$1 #"all_similar_regsamp/output/real_0"

foreach d (`echo all_similar_regsamp/output/real_*`)
    cd $d
    $basedir/runcholspec.csh $psrlist
    cd $basedir
    python plot_cholspec.py ${d}"/*_input.model"
end
   
    
