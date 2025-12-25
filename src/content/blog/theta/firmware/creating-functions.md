# Creating New Functions for Theta Firmware
by Mitch Naake

> Additional information on our Theta series of engine management systems can be found [here](/blog/theta/overview).

## What is a function?
In the context of engine management systems, a function is a part of the firmware that performs specific actions, such as limiting fuel/ignition outputs, based on how the user has configured the different settings for that specific function. 

Functions vary widely in complexity, ranging from simple functions that trigger an output based on configured inputs (e.g. no-lift-shift), to complex functions that implement complex algorithms and track the state of the engine over a number of combustion cycles (e.g. rolling antilag).

## The 'BaseFunction' class
