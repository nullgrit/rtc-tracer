import logging
import random

def run_diagnostics():
    logging.debug("STUN check initiated")
    if random.random() < 0.2:
        logging.error("Failed to bind TURN relay socket")
    
    logging.warning("Inconsistent NAT mapping behavior detected")
    loss = random.uniform(10, 15)
    logging.debug(f"Packet loss above threshold ({loss:.1f}%)")
    
    raise Exception("ICE connection failed")
