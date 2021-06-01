#!/bin/bash



for chainf in `find "../enterprise_out/" -name "chain*.txt"`;
do
    echo $chainf
    result_dir=`dirname $chainf`
    python -m enterprise_warp.results -r $result_dir -b 1 -f 1 -l 1 > $result_dir/enterprise_warp.results.dat
done

for chainf in `find "../enterprise_out/" -name "chain*.txt"`;
do
    echo $chainf
    result_dir=`dirname $chainf`
    python -m enterprise_warp.results -r $result_dir -c 2 -a 1 -m 1 > $result_dir/enterprise_warp.plotresult.dat
    for psr in `cat ../psrs.dat`;
    do
	python -m enterprise_warp.results -r $result_dir -c 2 -p "$psr" > $result_dir/enterprise_warp.plotresult_$psr.dat
    done
    python -m enterprise_warp.results -r $result_dir -c 2 -p "gw" > $result_dir/enterprise_warp.plotresult_gw.dat
done


