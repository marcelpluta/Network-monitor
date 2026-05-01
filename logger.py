from datetime import datetime

def save_log(rssi, snr, status):
    with open("data_log.txt", "a") as f:
        f.write(f"{datetime.now()} | RSSI:{rssi} | SNR:{snr} | {status}\n")
