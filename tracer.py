import os
import logging
from utils.netdiag import run_diagnostics

logging.basicConfig(filename='error.log', level=logging.DEBUG)

def main():
    logging.info("Starting diagnostics session...")
    try:
        run_diagnostics()
    except Exception as e:
        logging.error(f"Unhandled exception: {e}")
        raise

if __name__ == "__main__":
    main()
