#!/bin/csh

foreach psr ( `cat ./psrs.dat` )
echo $psr
#if ( $psr == "J1713+0747" ) then
set model=${psr}_input.model
tempo2 -gr cholSpectra -f $psr.par $psr.tim -dcf $model
end
