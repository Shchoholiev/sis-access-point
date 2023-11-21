import io
import picamera
from app.logger import logger

def setup_camera():
    global camera
    camera = picamera.PiCamera()

def cleanup_camera():
    camera.close()

def capture_image():
    stream = io.BytesIO()

    try:
        camera.capture(stream, format='jpeg')
        image_bytes = stream.getvalue()

        return image_bytes
    except Exception as e:
        logger.error(f"Error capturing image: {e}")
        return None