# Table Design Overview
by Mitch Naake

> Additional information on our Theta series of engine management systems can be found [here](/blog/theta/overview).

## What is a table?
Tables are used to calculate an output value based on one or two inputs (e.g. engine speed vs. engine load). 

| Group Type | Description | ID Range (Inclusive) | Total Unique | 
| :--------: | ----------- | -------------------- | ------------ |
| Static  | These are system tables that require static IDs. | 0-499 | 500 |
| Dynamic | Tables that are created/deleted on-demand for Functions, Sensors, etc. | 1000-1999 |

*Note: Theta series ECUs only have 256KB of system memory, and will never be able to instantiate enough tables to reach the ID limit for each group type.*