import json
import serial
import RPi.GPIO as GPIO  # Corrected typo 'RP1' to 'RPi'

SEAT_PINS = [24, 27, 22, 23]
DATA_FILE = "/home/movsmart/bus_data.json"

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in SEAT_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def read_seats():
    return [GPIO.input(pin) == 0 for pin in SEAT_PINS]

try:
    while True:
        # lat, lon = get_gps()  # Uncomment if you want GPS data as well
        seats = read_seats()
        data = {
            "seats": seats,
        }
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)
        print(f"Updated Data: {data}")
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()