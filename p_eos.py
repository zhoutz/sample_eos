import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

s = sys.argv[1]

for f in Path(f"sample_eos/{s}").glob("*.txt"):
    data = np.loadtxt(f)
    plt.plot(data[:, 0], data[:, 1], ".", ms=0.5)

plt.xscale("log")
plt.yscale("log")

plt.xlim(1e1, 1e5)
plt.ylim(1e-1, 1e5)

plt.xlabel(r"$\epsilon [MeV/fm^3]$")
plt.ylabel(r"$P [MeV/fm^3]$")

plt.show()
