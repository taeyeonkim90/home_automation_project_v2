# IoT Sunrise Alarm Clock Version 2


## Summary
This is a revision project of previous "home_automation_project" to split backend and frontend assets.
It is to improve maintainability of the code base and to modernize the architecture.


## Development Requirements
* Python 3.6
* Node.js >= 8.0
* Visual Studio Code


## Architecture
1. Backend
    * Django 2.0
        * provider for a RESTful api for alarm configuration
    * SQLite3
2. Frontend
    * React.js v16
        * Redux centered view application


## Notes
* Raspberry Pi's raspbian OS does not come with Python 3.6, but only with 3.2
* This project requires Python 3.6, and it cannot be installed through apt-get.
* You must download the Python 3.6 source code and compile on the machine.
* Did not find a way to properly run Node.js >= 8.0 on Raspberry Pi.
* Therefore, frontend production build assets needed to be built on a non-Raspberry Pi machine.