import io
import picamera
from PIL import Image
from app.logger import logger

def setup_camera():
    global camera
    camera = picamera.PiCamera()

def cleanup_camera():
    camera.close()

def capture_image():
    try:
        stream = io.BytesIO()

        camera.capture(stream, format='jpeg')

        # Flip the image horizontally
        stream.seek(0)  # Go to the start of the stream
        image = Image.open(stream)
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)

        # Save the flipped image to a new stream
        flipped_stream = io.BytesIO()
        flipped_image.save(flipped_stream, format='jpeg')
        flipped_image_bytes = flipped_stream.getvalue()

        logger.info(f"Image captured.")

        return flipped_image_bytes
    except Exception as e:
        logger.error(f"Error capturing image: {e}")
        return None