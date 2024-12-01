# Musical Instruments Design Patterns
# Why in english? Cuz I have to work in my productiooooon xd 

This repository contains several design patterns implemented with a musical instruments theme. Each pattern is demonstrated through Python code examples that simulate how instruments like guitars, pianos, and drums can be modeled with various software design patterns.

## Table of Contents
1. [Patterns Implemented](#patterns-implemented)
2. [Project Structure](#project-structure)
3. [How to Run](#how-to-run)
4. [Contact](#contact)

## Patterns Implemented

### 1. **Abstract Factory**
The **Abstract Factory** pattern allows the creation of families of related objects (in this case, musical instruments and their corresponding cases) without specifying their concrete classes.

- **InstrumentFactory**: Creates different types of musical instruments (Guitar, Piano, Drums).
- **InstrumentCaseFactory**: Creates corresponding cases for each instrument type.
  
  **Classes:**
  - `InstrumentFactory` (abstract)
  - `GuitarFactory`, `PianoFactory`, `DrumFactory` (concrete factories)
  - `Guitar`, `Piano`, `Drums` (concrete products)
  - `GuitarCase`, `PianoCase`, `DrumCase` (concrete cases)

### 2. **Singleton**
The **Singleton** pattern ensures that a class has only one instance and provides a global point of access to it. This example uses the **GuitarAmp** class to demonstrate this pattern, where only one amplifier instance exists regardless of how many times it is instantiated.

  **Classes:**
  - `GuitarAmp`: Singleton that manages the guitar amplifier instance.

### 3. **Prototype**
The **Prototype** pattern allows creating new objects by copying an existing object, known as a prototype. The example demonstrates cloning a guitar and a piano.

  **Classes:**
  - `Instrument`: Base class with a `clone()` method.
  - `Guitar`, `Piano`: Concrete classes with `clone()` method.

### 4. **Adapter**
The **Adapter** pattern allows incompatible interfaces to work together. In this example, the **GuitarAdapter** class makes an old guitar compatible with the music player interface.

  **Classes:**
  - `OldGuitar`: Incompatible old guitar interface.
  - `GuitarAdapter`: Adapter that makes `OldGuitar` compatible with `MusicPlayer`.

### 5. **Decorator**
The **Decorator** pattern allows adding functionality to an object dynamically. In this case, we add sound effects (like Reverb and Distortion) to a guitar.

  **Classes:**
  - `Instrument`: Base class for musical instruments.
  - `Guitar`: Concrete instrument.
  - `InstrumentDecorator`: Base decorator class.
  - `ReverbDecorator`, `DistortionDecorator`: Concrete decorators that add effects to the instrument.

### 6. **Observer**
The **Observer** pattern allows a subject (the instrument) to notify its observers (the musicians) about events. When an instrument plays, the observers are notified and can act accordingly.

  **Classes:**
  - `Observer`: Base observer interface.
  - `Musician`: Concrete observer.
  - `Instrument`: Subject class that notifies observers.
  - `Guitar`, `Piano`, `Drums`: Concrete instruments.

### 7. **State**
The **State** pattern allows an object to change its behavior when its internal state changes. This example demonstrates a music player that can change between "stopped" and "playing" states.

  **Classes:**
  - `PlayerState`: State interface.
  - `StoppedState`, `PlayingState`: Concrete states.
  - `MusicPlayer`: Context class that changes states.

### 8. **Strategy**
The **Strategy** pattern allows defining a family of algorithms and making them interchangeable. In this case, different play styles (Acoustic, Electric, Classical) can be applied to a musician.

  **Classes:**
  - `PlayStyle`: Strategy interface.
  - `AcousticStyle`, `ElectricStyle`, `ClassicalStyle`: Concrete strategies.
  - `Musician`: Context class that uses strategies.

### 9. **Template Method**
The **Template Method** pattern defines the structure of an algorithm, allowing subclasses to implement certain steps of it. This example involves a predefined process for a musical performance.

  **Classes:**
  - `MusicPerformance`: Abstract class defining the template method.
  - `GuitarPerformance`, `PianoPerformance`: Concrete classes implementing the `play_music()` step.

### 10. **Builder**
The **Builder** pattern allows constructing complex objects step by step. In this example, we build a complex guitar object using the builder pattern.

  **Classes:**
  - `Guitar`: Product class representing the guitar.
  - `GuitarBuilder`: Abstract builder class.
  - `ElectricGuitarBuilder`: Concrete builder class.
  - `GuitarDirector`: Director that constructs the guitar using the builder.

## Project Structure

