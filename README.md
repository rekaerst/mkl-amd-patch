# Intel MKL patches for AMD Zen

This patch bypass MKL's 'cripple AMD' functions

---

patched functions
```
mkl_serv_intel_cpu
mkl_serv_intel_cpu_true
```

---

Usage: 
```bash
sudo python patch.py \<path to libmkl_core.so\>
```

---

Reference: https://danieldk.eu/Posts/2020-08-31-MKL-Zen.html
