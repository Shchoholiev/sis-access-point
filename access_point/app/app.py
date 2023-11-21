import asyncio
from .logger import logger

async def main():
    stop_event = asyncio.Event()

    try:
        await asyncio.gather(
            stop_event.wait()  # Waiting for stop event
        )
    except:
        logger.info("Application stopping...")
    finally:
        logger.info("Application stopped.")

def run():
    logger.info("Starting shelves controller...")
    asyncio.run(main())

if __name__ == "__main__":
    run()
