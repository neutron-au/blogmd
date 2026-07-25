# Theta Protocol
A comprehensive overview of the serial communication protocol for the Theta series of engine management systems.



### General Overview
All serial packets begin with a "command" id, telling the tuning software or ECU what kind of command has been received. 
The data that follows the command id byte is generally a class type id and then a instance id followed by some other data.

*Example "Fetch Function Attributes" packet:*

| Byte | Data        | Example           | Representation (byte) |
| :--: |  :--------: | :---------------: | :-------------------: |     
|   1  | Command     | GetMeta           | 0x04                  |
|   2  | Class ID    | Function          | 0x04                  |
|   3  | Function ID | DeveloperFunction | 0x01                  |
 