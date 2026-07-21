# Functions Design Overview
by Mitch Naake

> Additional information on our Theta series of engine management systems can be found [here](/blog/theta/overview).

## What is a function?
In the context of engine management systems, a function is a part of the firmware that performs specific actions, such as limiting fuel/ignition outputs, based on how the user has configured the different settings for that specific function. 

Functions vary widely in complexity, ranging from simple functions that trigger an output based on configured inputs (e.g. no-lift-shift), to complex functions that implement complex algorithms and track the state of the engine over a number of combustion cycles (e.g. rolling antilag).

## The 'BaseFunction' class
The BaseFunction class serves as the singularity starting point of all the automotive functions that will be created for the Theta series of engine management systems.

Below is details of the methods, attributes and overall design idea of the `BaseFunction` class:

### Design/Requirements Overview
#### Event Ticking
List of TickEventType's:

| Name | Description |
| :--: | ----------- |
| `MainLoop` | Event fired from the background main loop each iteration. Runs at the lowest priority. Can be interrupted by IRQ and SoftIRQ tasks. | 
| `EngineTDC` | Event fired via SoftIRQ each time cylinder one (1) hits top-dead-center (TDC). Runs at second-highest priority, but can still be interrupted by IRQ. |
| `EngineCycle` | Event fired via SoftIRQ every 720 degrees of crankshaft rotation (one complete combustion cycle for a 4-stroke engine). Can still be interrupted by IRQ.

<br>

The BaseFunction class is required to be a concrete starting point for *any* function that is created for Theta. Diffrent functions are required to be 'ticked' during/after certain events. For example: a development function that prints a message to serial at configurable intervals isn't time-sensitive, and is safe to be ticked by



### Attributes
| Name | Type | Description |
| :--: | :--: | ----------- |
| `id` | int | Unique per-function class ID. |
| `attrs_` | AttrEntry* | Pointer to the first AttrEntry. Each editable parameter (variable) in a function has an AttrEntry instance for getter/setter context within the firmware, and also as a means of telling the tuning software what editable parameters exist. |

### Methods

| Name | Function Description |
| :--: | ----------- |
| `void tick(TickEventType t)` | Router function. There are a number of event tick types (table below) |
| `attrs_` |  |

<br>

```
struct AttrEntry {
        const char* name;
        const char* display_name;
        SerialAttrType type;
        void* ptr;       // points to storage or helper struct
        AttrSetFn set;   // optional override; if null uses defaultFor(type)
        AttrGetFn get;   // optional override; if null uses defaultFor(type)

        constexpr AttrEntry(
            const char* n = "",
            const char* dn = "",
            SerialAttrType t = SerialAttrType::String,
            void* p = nullptr,
            AttrSetFn s = nullptr,
            AttrGetFn g = nullptr
        )
            : name(n), display_name(dn), type(t), ptr(p), set(s), get(g) {}
    };
```
