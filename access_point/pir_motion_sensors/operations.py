import asyncio
import requests
from gpiozero import MotionSensor
from cameras import capture_image
from app.config import config
from app.logger import logger

def setup_pir_motion_sensor(pin: int):
    global motion_sensor
    motion_sensor = MotionSensor(pin)

def cleanup_motion_sensor():
    motion_sensor.close()

async def monitor_pir_motion_sensor():
    is_item_present = False

    while True:
        motion_sensor.wait_for_motion()
        motion_sensor.wait_for_no_motion()
        # delay before capturing a photo
        await asyncio.sleep(0.3)

        if is_item_present:
            is_item_present = False
        else:
            item_photo = capture_image()

            url = f"{config['apiUrl']}/access-points/{config['deviceId']}/items/identify-by-image"
            files = {'image': ('image.jpg', item_photo, 'multipart/form-data')}

            response = requests.post(url, files=files)

            logger.info(f"POST request sent to {url}. Response status code: {response.status_code}")

            is_item_present = True
