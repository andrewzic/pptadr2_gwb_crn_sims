import numpy as np

template_str = """MODEL 1
ALPHA {:.2f}
FC 0.01
AMP {:.2e}"""

fname = "psr_noise_vals.dat"
with open(fname, 'r') as f:
    with open("psrs.dat", 'r') as psr_f:
        lines = f.readlines()
        psrs = psr_f.readlines()
        for line, psr in zip(lines, psrs):
            
            print(psr.strip('\n'))
            
            row = np.array(line.strip().split('\t'), dtype = np.float64)
            alpha, p0, dt = row
            out_fname = "{}_input.model".format(psr.strip())
            with open(out_fname, 'w') as out_f:
                out_f.write(template_str.format(alpha, p0))
                out_f.close()
