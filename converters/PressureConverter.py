# -*- coding: utf-8 -*-

# Converts units of pressure: Pa, Bar, atm, Torr, psi

# at to pa
def at_to_pa(at):
    return at / 1.01971621298E-5


# at to bar
def at_to_bar(at):
    return at / 1.0197


# at to atm
def at_to_atm(at):
    return at / 1.03322755477


# at to torr
def at_to_torr(at):
    return at / 0.00135950982242


# at to psi
def at_to_psi(at):
    return at / 0.0703069578296


# Pa to bar
def Pa_to_bar(pa):
    return pa * 0.00001


# Bar to Pa
def bar_to_Pa(bar):
    return bar / 0.00001


# Pa to atm
def Pa_to_atm(pa):
    return pa / 101325


# atm to Pa
def atm_to_Pa(atm):
    return atm * 101325


# Pa to Torr
def Pa_to_Torr(pa):
    return pa * 0.00750062


# Torr to Pa
def Torr_to_Pa(torr):
    return torr / 0.00750062


# Pa to psi
def Pa_to_psi(pa):
    return pa / 6894.76


# psi to Pa
def psi_to_Pa(psi):
    return psi * 6894.76


# bar to atm
def bar_to_atm(bar):
    return bar / 1.01325


# atm to bar
def atm_to_bar(atm):
    return atm * 1.01325


# bar to Torr
def bar_to_Torr(bar):
    return bar * 750.062


# Torr to bar
def Torr_to_bar(torr):
    return torr / 750.062


# bar to psi
def bar_to_psi(bar):
    return bar * 14.5038


# psi to bar
def psi_to_bar(psi):
    return psi / 14.5038


# atm to Torr
def atm_to_Torr(atm):
    return atm * 760


# Torr to atm
def Torr_to_atm(torr):
    return torr / 760


# atm to psi
def atm_to_psi(atm):
    return atm * 14.6959


# psi to atm
def psi_to_atm(psi):
    return psi / 14.6959


# Torr to psi
def Torr_to_psi(torr):
    return torr / 51.7149


# psi to Torr
def psi_to_Torr(psi):
    return psi * 51.7149
