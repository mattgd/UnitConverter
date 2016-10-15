# FORCE CONVERSION


# Newtons to Dynes (dyn)
def n_to_dyn(n):
    return n * 10 ^ 5


# Dynes to Newtons (n)
def dyn_to_n(dyn):
    return dyn * 0.00001  # Precision of 5 significant digits


# Newtons to Poundals (pdl)
def n_to_pdl(n):
    return n * 7.23301  # Precision of 5 significant digits


# Poundals to Newtons (n)
def pdl_to_n(pdl):
    return pdl * 0.13826  # Precision of 5 significant digits


# Newtons to Kilogram-Force (kp)
def n_to_kp(n):
    return n * 0.10197  # Precision of 5 significant digits


# Kilogram-Force to Newtons
def kp_to_n(kp):
    return kp * 9.80665  # Precision of 5 significant digits


# Dyne to Kilogram-Force (kp)
def dyn_to_kp(dyn):
    return n_to_kp(dyn_to_n(dyn))


# Kilogram-Force to Dyne (dyn)
def kp_to_dyn(kp):
    return n_to_dyn(kp_to_n(kp))


# Dynes to Poundals (pdl)
def dyn_to_pdl(dyn):
    return n_to_pdl(dyn_to_n(dyn))


# Poundals to Dynes (dyn)
def pdl_to_dyn(pdl):
    return n_to_dyn(pdl_to_n(pdl))


# Kilogram-Force to Poundals (pdl)
def kp_to_pdl(kp):
    return n_to_pdl(kp_to_n(kp))


# Poundals to Kilogram-Force (kp)
def pdl_to_kp(pdl):
    return n_to_kp(pdl_to_n(pdl))
