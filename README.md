# Nasa Hackathon18

A simple web server that provides Astronomic distance between planets using NASA JPL ephemerides.
Later it will be used for various purposes.

### Dependencies
* skyfield==1.9
* Flask==1.0.2


### Instructions
1. Open your terminal in your preferred directory and clone this project
```bash
$ git clone https://github.com/anilbey/nasa_hackathon18
```
2. Enter the project directory
```bash
$ cd nasa_hackathon18
```
3. Export FLASK_APP Environment variable
```bash
export FLASK_APP=astronomy_services.py 
```
4. Run the flask app
```bash
python -m flask run
```
A sample request that computes the standard ICRF right ascension and declination between the sun at the moon at the current timestamp.
```shell
http://127.0.0.1:5000/distance?pt1=sun&pt2=moon
```

