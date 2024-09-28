
# ESP8266 Morse Code Buzzer

This project enables an ESP8266 microcontroller to function as a Morse code signal transmitter using sound (buzzer). By pressing a button connected to the ESP8266, you can transmit Morse code signals in the form of short beeps (dots) and long beeps (dashes). The duration of the button press determines whether a dot or dash is sent.

## Features

- **Morse Code Transmission**: The system converts button presses into audible Morse code signals.
- **Audible Feedback**: Each dot and dash is played through a buzzer connected to the ESP8266.
- **Button Control**: A single button is used to generate both dots and dashes, depending on how long the button is held.
- **PWM Buzzer Control**: The buzzer is controlled via PWM (Pulse Width Modulation), allowing for precise sound frequency generation.

## Hardware Requirements

- **ESP8266** microcontroller
- **Buzzer** connected to GPIO pin 15
- **Button** connected to GPIO pin 14 (with pull-up configuration)
- Breadboard and jumper wires for connections

## How It Works

1. **Short Press (Dot)**: If the button is pressed for less than 0.23 seconds, a dot signal (short beep) is generated.
2. **Long Press (Dash)**: If the button is pressed for 0.6 seconds or more, a dash signal (long beep) is generated.
3. **Button Timing**: The duration of the button press is measured to differentiate between dots and dashes.
4. **Buzzer Sound**: 660 Hz tone.

## Code Overview

The code uses the ESP8266's GPIO pins to interact with the button and control the buzzer. Key sections include:

- **PWM Initialization**: The buzzer is initialized using PWM for sound generation.
- **Button Press Detection**: The button is monitored, and press duration is measured to determine whether a dot or dash is generated.
- **Sound Output**: The buzzer plays a tone for each dot or dash, depending on the press duration.

## Setup and Installation

1. Connect the buzzer to GPIO pin 15 (D8 on most ESP8266 boards).
2. Connect the button to GPIO pin 14 (D5 on most ESP8266 boards).
3. Upload the code to your ESP8266.
4. Power the ESP8266 and press the button to start transmitting Morse code.
