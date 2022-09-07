# UBOOT - Tools of Engagement
List of contents:
 - [Overview](#overview)
 - [Tools & Historical Relevance](#tools--historical-relevance)
 - [Technical Details](#technical-details)
	 - [Kivy Framework - Usage In Project](#kivy-framework---usage-in-project)
	 - [Application Features](#application-features)
		 - [Custom Event Dispatch & Handling](#custom-event-dispatch--handling)
		 - [Component State Persistence](#component-state-persistence)
		 - [Contextualization of Tool Parts Using Buttons](#contextualization-of-tool-parts-using-buttons)
		 - [Singular Touch as Input](#singular-touch-as-input)
		 - [Documentation & Settings View](#documentation--settings-view)
 - [Testing](#testing)
 - [Building](#building)
 - [Glossary](#glossary)

## Overview
This is a small android application, designed to help submarine simulator enthusiasts have a more realistic experience commanding a WWII German Uboat. It is a collection of <a id="digitally-analog_src" href="#digitally-analog">digitally-analog</a> representations of navigation tools of 1939-1944 era, with the intension of simulating the difficulty of peforming trigonometric and other calculations as quickly/reliably as possible.

It uses the [Kivy Framework](https://github.com/kivy/kivy) and it is solely writen in Python and custom (OpenGL)GLSL shaders.

## Tools & Historical Relevance
The application comprises of two seperate tools, the "Angriffsscheibe" or "Attack Disc" and the "Sliderule Disc". Their primery purpose was to help officers locate and intercept allied convoy groups. At the early stages of the war, they were also utilized as a means to determine a correct gyroangle for early war torpedoes, which were notorious for being prone to unreliable gyroangle configuration via the TDC or Target Data Computer. The TDC was an electromechanical analog computer, housed onboard the submarine and was responsible for giving a torpedo firing solution. Due to faulty equipment and lack of experience amongst the crew with regards to TDC, officers additionaly often resorted in manual calculations with standard hand-held slide rule-type devices such as the tools mentioned above.
<br><br/>

### Attack Disc

![AD](doc/Attack_Disc.png)

The "Attack Disc" - which is the first tool a user is greeted upon using the application - is an enhanced version of a compass. It encorporates several smaller discs that cooperate in a triangulation effort to determine the actual course of target ship. For that to happen, the heading of own ship and a bearing to the target is provided as input. The unknown variable to be determined is the <a id="aob_src" href="#aob">Angle on Bow or AOB</a>, in short. Through estimation - at first - and constant refinement, in conjunction with information given by the Sliderule Disc, the AOB is demonstrated and the actual course is easily obtained.
<br><br/>

### Sliderule Disc

![SD](doc/SlideRule_Disc.png)

The "Sliderule Disc" is a logarithmic scale calculator. It encorporates an inner disc and a pointer. The outter disc represents values of the sin function in degrees while the inner disc has markings for speed in knots and distance in meters. The pointer has markings related to time and as it rotates it performs mathematical operations(primarely multiplication and division). The true power of this tool lies on the abstruction of calculations with regards to scale (thanks to the log), the minimal error and the fast output of results. Some of the common calculations done utilizing this tool were:

 - Measuring distance to target ship
 - Measuring speed of target ship
 - Measuring the AOB

The combination of those two tools gave accurate enough information for the officers to acquire optimal position for an abush, commence consistant torpedo attacks and even navigate the Uboat while submerged, evading depth charges from enemy convoy-escort ships.

In-depth details and examples of usage can be found on this [manual](https://www.dropbox.com/s/fikld8mavkfe5dc/Angriffsscheibe_Handbuch_3.pdf?dl=0).

## Technical Details
### Kivy Framework - Usage In Project
The Kivy Framework is a substantial utility framework for any android application project written in python. Today still is one of the most prefered/common solution for developers because it offers accsess to a wide range of integrated tools, while remaining consistant and intuitive compared to antagonistic frameworks. Using Kivy one can establish from the least basic application functionality, to the ability of entirely structuring every aspect of an application, without the need of any extra dependancies. Furthermore, it provides a very linear integration with both android and iOS systems.

However, the focus and purpose of this project is purelly educational and with no intention of producing a marketable product. Thus, the usage of kivy modules is supposed to be limmited to specific low-level services.

For example, Kivy creates a layer on top of an SDL2 window provider that manages touch input events, exposes OpenGL functions and constants as well as some math related objects/classes around vector and matrix operations. This layer also handles most of the rendering pipeline operations like swapchain configuration, batch rendering operations, texture and framebuffer/rendertarget creation, etc. The appliaction's event loop also resides in the layer by default but this application uses it very discreetly since a custom event system is used instead.

Kivy's only higher-level functionality in this application, is UI widgets and mostly the root widget class itself as a starting point for own custom widget generation.
<br><br/>

### Application Features
#### Custom Event Dispatch & Handling
The application and all UI elements have actions tied to a custom [event model](https://github.com/graphXDoses/UBOOT-Tools-of-Engagement/blob/main/src/lib/EventModel.py) system, that uses an [event bus](https://github.com/graphXDoses/UBOOT-Tools-of-Engagement/blob/main/src/lib/EventBus.py) object as a mediator to transfer messages from a sender to all listening recievers. These actions are actually callback functions that the event bus triggers as soon as the assosiated message is dispatched from the sender object. This approach allows sender objects and recievers to be [loosely coupled](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern#Loose_coupling). Another advantage of this event system, is that it manages to bypass the proccessing step for custom events of the Kivy build-in event system, while triggering only the relevant Kivy events that concern the reciever object (e.g. rendering). A slight increase in performance is to be expected this way.
<br><br/>
#### Component State Persistence
The application stores all nessecary information regarding components, such as views and tool parts(widgets) into the `app.ini` file. All occuring changes are logged as soon as they happen and the file is updated in real time. When the application starts, it recalls the states and values of the corresponding components. The recall proccess described is also initiated in between context changes.
<br><br/>

#### Contextualization of Tool Parts Using Buttons
The interaction of the user with application tools is of great importance, especially when it comes to applications such as this. The user should feel comfortable using all interactable components, while the experience of realism is kept as high as possible. With this in mind, intuitively users might expect direct interaction with individual parts (touch and move the part of interest) combined with standard UI helper functionality such as zoom/pan. However this application attempts to provide quality user experience in a different manner.

The UI is compartmentalized into two separate views, the **MainView** and **SettingsView**(WIP). The MainView contains both tools and each of them share the same ergonomic layout. The layout, ensures that the tool itself covers the most screen area availiable while giving way for info bars and button areas. Buttons are used to layer tool parts and enable unobstructed input to the part they are linked to. With layering, the user is benefited by having much more space to work with - meaning comfort and precision -, no chance of accidental interference with neighbouring parts and information related to the active part - such as role - which is crutial in retaining awareness while performing the nessecary calculations in a rapid and stressfull fashion.

<br><br/>
![Button Showcase](doc/Button_Showcase.gif)

<br><br/>

#### Singular Touch as Input

By default, touch events are proccessed as a group. That means for each touch and depending on what event it triggers by action, callback functions will be called as a response to the event trigger. This behaviour affects the active part multiple times in a single logic frame resulting in flickering, which of course is problematic. Flickering occurs due to logic and rendering operations happening on different threads, asyncronously. Even if touch input proccessing this way wasn't as visually unpleasant, the logic thread is overloaded with unesseccary work.

In an effort to prevent this from happening, the appliaction tracks the first touch recieved on Kivy's built-in `on_touch_down` event and allows only that to affect the active part. If the first touch is lost - via `on_touch_up` event - while other touches continue to be recieved, input proccessing stops.

Example:<br><br/>
![Singular Touch Proccessing Showcase](doc/Singular_Touch_Showcase.gif)
<br><br/>

#### Documentation & Settings View
Work-In-Progress

## Testing
Requirements for testing localy are:

 - [Python3](https://www.python.org/downloads/)
 - [Pipenv](https://pypi.org/project/pipenv/)

After cloning the repository, open a cmd and create a pipenv virtual environment:
```
pipenv shell
```
After the virtual environment has been created, install Kivy-base and dependencies:
```
pipenv run python -m pip install "kivy[base]"
```
To run the main.py make sure it is done through the virtual environment like so:
```
pipenv run py main.py
```

## Building
Requirements for building are:

 - [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) (WSL)
 - Ubuntu Terminal (found on Microsoft Store)
 - Python3 (on WSL)
 - [Buildozer](https://buildozer.readthedocs.io/en/latest/installation.html) (on WSL)

Once the above requirements are installed and configured accordingly, follow the [Quickstart](https://buildozer.readthedocs.io/en/latest/quickstart.html) guide.

## Glossary

- <strong id="digitally-analog">digitally analog</strong>: *Rasterized replicas of real life analog devices, in both appearence and interaction.* [↑](#digitally-analog_src)
- <strong id="aob">AOB</strong>: *The AOB or Angle on Bow, is the angle (in degrees) formed between the forward facing vector of target ship with the view direction from an observer. It ranges from 0° to 180°.* [↑](#aob_src)
