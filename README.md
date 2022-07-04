# Overview
This is a small application for android, designed to help subsimers have a more realistic experience commanding a WWII submarine. It is a collection of digitally analog(they interact as their real counterparts, but are rasterized) representations of navigation tools of 1939-1944 era, with the intension of simulating the difficulty of peforming trigonometric and other calculations as quickly/reliably as possible.

It uses the Kivy framework and it is solely writen in Python and custom (OpenGL)GLSL shaders.

# Details - Historical Relevancy
The application comprises of two seperate tools, the "Angriffsscheibe" or "Attack Disc" and the "Sliderule disc". Their purpose was to help officers locate and intercept allied convoy groups and even determine a correct gyroangle for early war torpedoes, which were notorious for having unreliable means of setting that with the TDC or Target Data Computer - an analog computer housed onboard the submarine for that purpose -.

The "Attack Disc" - which is the first tool a user is greeted upon using the application - is an enhanced version of a compass. It encorporates several smaller discs that - in simple terms - provide the heading of own ship and a bearing indicating the direction of a target. With that information another disc triangulates the actual course of the target.

The "Sliderule disc" is a logarithmic calculator. It encorporates an inner disc and a pointer. The outter disc represents values of the sin function in degrees while the inner disc has markings for speed in knots and distance in meters. The pointer has markings related to time and as it rotates it performs mathematical operations
(primarely multiplication and division). The true power of this tool lies on the abstruction of calculations with regards to scale (thanks to the log), the minimal error and the blazing speed of producing results. Some of the common calculations done utilizing this tool was:
<ul>
  <li>
    Measuring distance
  </li>
  <li>
    Measuring speed
  </li>
  <li>
    Measuring the angle on bow (orientation with respect to ship direction)
  </li>
</ul>

The combination of those two tools gave accurate enough information for the officers to commence consistant torpedo attacks.

# Testing
Requirements for testing localy are:
<ul>
<li>Pipenv</li>
</ul>

After cloning the repository, open a cmd and create a pipenv virtual environment:
```
pipenv shell
```
After the virtual environment has been created, run this:
```
pipenv install
```
To run the main.py make sure it is done through the virtual environment like this:
```
pipenv run py main.py
```

# Building
Requirements for building are:
<ul>
<li>Buildozer</li>
<li>Ubuntu Virtual Machine</li>
</ul>
