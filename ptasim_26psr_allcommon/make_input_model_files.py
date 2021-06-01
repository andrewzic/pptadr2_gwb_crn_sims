import numpy as np
import sys

noiseval_fname = sys.argv[1] #.dat file containing alpha, p0, and toa errbar for each psr

template_str = """MODEL 1
ALPHA {:.2f}
FC 0.01
AMP {:.2e}"""


with open(noiseval_fname, 'r') as noise_f:
    with open("psrs.dat", 'r') as psr_f:
        lines = noise_f.readlines()
        psrs = psr_f.readlines()
        for line, psr in zip(lines, psrs):
            
            print(psr.strip('\n'))
            
            row = np.array(line.strip().split('\t'), dtype = np.float64)
            alpha, p0, dt = row
            out_fname = "cholspec_inp_files/{}_input.model".format(psr.strip())
            with open(out_fname, 'w') as out_f:
                out_f.write(template_str.format(-1.0*alpha, p0)) #negating alpha because it should be negative in dat file
                out_f.close()