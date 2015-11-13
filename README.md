# earth-state-vector 
***Prints the heliocentric state vector of the earth using SpiceyPy (SPICE).***

A little tool intended to demonstrate the use of SPICE, through the [SpiceyPy Python wrapper](http://spiceypy.readthedocs.org), to print the state vector of the earth (i.e. position and velocity) in heliocentric ecliptic (J2000) coordinates.

### Example use
```
$ python earth-state-vector.py 2015-11-13T09:43:00
```

Output:
```
Input time = 2015-11-13T09:43:00

# Position of the Earth in the heliocentric ecliptic (J2000) frame
X = 94234331.6256016 km
Y = 114193407.5443151 km
Z = -4953.757979899645 km

# Velocity of the Earth in the same frame
dX = -23.4721139580071 km/s
dY = 18.852699520611225 km/s
dZ = -0.0009050242759034433 km/s

# Orbital speed [sqrt(dX^2 + dY^2 + dZ^2)]
Speed = 30.10588669498368 km/s
```

### Installation

[SpiceyPy](http://spiceypy.readthedocs.org) must be installed.
For example:
```
$ git clone git@github.com:AndrewAnnex/SpiceyPy.git
$ cd SpiceyPy
$ python setup.py install
```

Then simply download or clone this repository and run the Python script, e.g.
```
$ git clone git@github.com:barentsen/earth-state-vector.git
$ cd earth-state-vector
$ python earth-state-vector.py 2015-11-13T09:43:00
```
