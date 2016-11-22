"""Prints the heliocentric state vector of the earth using SpiceyPy (SPICE).
"""
from __future__ import print_function  # Needed for Python 2 compatibility
import sys
import spiceypy as sp

# These data files were obtained from
# http://naif.jpl.nasa.gov/pub/naif/generic_kernels
LEAP_SECOND_FILE = "data/naif0011.tls"
EPHEMERIDES_FILE = "data/de432s.bsp"


if __name__ == "__main__":
    # Script expects first argument to be a UTC timestamp
    if len(sys.argv) > 1:
        input_utc = sys.argv[1]
    else:
        input_utc = "2000-01-01T00:00:00"  # default for testing
    # Load the necessary data files
    sp.furnsh([LEAP_SECOND_FILE, EPHEMERIDES_FILE])
    # Convert UTC to ephemeris time
    epoch = sp.utc2et(input_utc)
    # State (position and velocity in cartesian coordinates)
    # of EARTH as seen from SUN in the ecliptic J2000 coordinate frame.
    state, lt, = sp.spkezr("EARTH", epoch, "ECLIPJ2000", "NONE", "SUN")
    # Show the output
    print("Input time = {}".format(input_utc))
    print("")
    print("# Position of the Earth in the heliocentric ecliptic (J2000) frame")
    print("X = {} km".format(state[0]))
    print("Y = {} km".format(state[1]))
    print("Z = {} km".format(state[2]))
    print("")
    print("# Velocity of the Earth in the same frame")
    print("dX = {} km/s".format(state[3]))
    print("dY = {} km/s".format(state[4]))
    print("dZ = {} km/s".format(state[5]))
    # As a sanity check, print the speed
    speed = (state[3]**2 + state[4]**2 + state[5]**2)**.5
    print("")
    print("# Orbital speed [sqrt(dX^2 + dY^2 + dZ^2)]")
    print("Speed = {} km/s".format(speed))
