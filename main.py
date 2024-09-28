from machine import Pin, PWM
import time

# GPIO settings
buzzer_pin = Pin(15, Pin.OUT)  # Pin to which the buzzer is connected (output)
button_pin = Pin(
    14, Pin.IN, Pin.PULL_UP
)  # Pin to which the button is connected (input with pull-up)

# Sound settings
frequency = 660  # Buzzer sound frequency in Hz
duty_cycle = 128  # Duty cycle 10%

# Setting PWM for the buzzer
buzzer = PWM(buzzer_pin)  # Initializing PWM on the buzzer pin
buzzer.deinit()  # The buzzer is off at the start

# Definitions for Morse signal durations
dot_duration = 0.2  # Duration of a dot in seconds
dash_duration = 0.6  # Duration of a dash in seconds
threshold_time = 0.23  # Threshold time between dot and dash


def start_beep():
    """Function to turn on the buzzer sound."""
    buzzer.init(
        freq=frequency, duty=duty_cycle
    )  # Initialize buzzer with the specified frequency and duty cycle


def stop_beep():
    """Function to stop the buzzer sound."""
    buzzer.deinit()  # Deactivate PWM, which turns off the buzzer


def main():
    """Main function responsible for button handling and sending Morse code signals."""
    print("Device ready for Morse transmission.")  # Inform about the device's readiness

    button_pressed = False  # Flag to track button state
    start_time = 0  # Variable to store the button press start time

    while True:  # Main program loop
        if (
            button_pin.value() == 0 and not button_pressed
        ):  # Check if the button has been pressed
            button_pressed = True  # Mark button as pressed
            start_time = time.ticks_ms()  # Save press start time
            start_beep()  # Start buzzer sound

        elif button_pressed:  # If the button is pressed
            press_duration = (
                time.ticks_diff(time.ticks_ms(), start_time) / 1000
            )  # Calculate press duration in seconds

            # Check if press duration is less than the threshold
            if (
                press_duration >= dot_duration
                and press_duration <= threshold_time
                and button_pin.value() == 1
            ):
                print("Dot [ . ]")  # Dot signal information
                stop_beep()  # Stop the sound
                button_pressed = False  # Reset button press flag

                while button_pin.value() == 0:  # Wait for button release
                    pass

                time.sleep(dot_duration)  # Pause corresponding to dot duration

            # Check if press duration is longer than the dash duration
            elif press_duration >= dash_duration:
                print("Dash [ - ]")  # Dash signal information
                stop_beep()  # Stop the sound
                button_pressed = False  # Reset button press flag

                while button_pin.value() == 0:  # Wait for button release
                    pass

                time.sleep(dot_duration)  # Pause corresponding to dot duration


# Run the program
main()
