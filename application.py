from skyfield.api import load
from flask import Flask
from flask import request
import json
app = Flask("Astronomic distance service using JPL ephemerides")

planets = load('de421.bsp')

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/distance')
def compute_dist():
    pt1 = request.args.get('pt1')
    print(pt1)
    pt2 = request.args.get('pt2')
    print(pt2)

    # get the time
    ts = load.timescale()
    t = ts.now()

    # the planet objects
    planet1 = planets[pt1]
    planet2 = planets[pt2]

    astrometric = planet1.at(t).observe(planet2)

    # tuple containing the three measures
    ra, dec, distance = astrometric.radec()

    # create a dict with info about measures
    dd = {'ra': ra.hstr(), 'dec': dec.dstr(), 'distance (au)': str(distance.au) + 'au'}
    return json.dumps(dd)
