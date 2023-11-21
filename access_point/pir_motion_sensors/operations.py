import asyncio
from urllib import request
import RPi.GPIO as GPIO
from cameras.operations import capture_image
from app.config import config
from app.logger import logger

SENSOR_PIN = 18

def setup_pir_motion_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SENSOR_PIN, GPIO.IN)

async def monitor_pir_motion_sensor(pin: int):
    while True:
        if GPIO.input(pin):
            logger.info(f"Motion detected by PIR sensor")

            # Wait to allow user to remove their hand from the image
            await asyncio.sleep(0.5)

            item_photo = capture_image()

            url = f"{config['apiUrl']}/access-points/{config['deviceId']}/items/identify-by-image"
            files = {'image': ('image.jpg', item_photo, 'multipart/form-data')}

            response = request.post(url, files=files)

            logger.info(f"POST request sent to {url}. Response status code: {response.status_code}")
                
        await asyncio.sleep(0.2)  # Sleep for a short period to prevent blocking