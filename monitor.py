import random
from logger import save_log

def get_signal():
    rssi = random.randint(-120, -50)
    snr = random.randint(0, 35)
    return rssi, snr

def evaluate(rssi, snr):
    if rssi > -70 and snr > 25:
        return "GOOD"
    elif rssi > -90:
        return "MEDIUM"
    else:
        return "BAD"

for i in range(10):
    rssi, snr = get_signal()
    status = evaluate(rssi, snr)

    print(f"RSSI: {rssi} | SNR: {snr} | STATUS: {status}")
    save_log(rssi, snr, status)
