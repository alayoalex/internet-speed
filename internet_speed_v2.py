import speedtest
import csv
import os
import time
import subprocess
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import psutil


def get_network_name():
    try:
        # Para Windows
        if os.name == 'nt':
            result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode('utf-8', 'ignore')
            lines = result.split('\n')
            for line in lines:
                if "SSID" in line:
                    return line.split(":")[1].strip()
        # Para Linux
        else:
            result = subprocess.check_output(["iwgetid"]).decode('utf-8').strip()
            return result.split('"')[1]
    except Exception as e:
        return 'Unknown'

def test_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    ping = st.results.ping
    download_speed = st.results.download / 1024 / 1024  # Convertir de bits a Mbits
    upload_speed = st.results.upload / 1024 / 1024  # Convertir de bits a Mbits

    return download_speed, upload_speed, ping

def write_to_csv(network_name, download, upload, ping):
    file_exists = os.path.isfile("internet_speed.csv")
    with open("internet_speed.csv", "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Network", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])
        writer.writerow([datetime.now(), network_name, download, upload, ping])

def generate_daily_graph():
    times, downloads, uploads, pings = [], [], [], []
    with open("internet_speed.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if "Timestamp" in row:
                continue
            else:
                time_str, network_name, download, upload, ping = row
                time_obj = datetime.fromisoformat(time_str)
                times.append(time_obj)
                downloads.append(float(download))
                uploads.append(float(upload))
                pings.append(float(ping))
    plt.figure(figsize=(10, 6))
    plt.plot(times, downloads, label='Download (Mbps)')
    plt.plot(times, uploads, label='Upload (Mbps)')
    plt.xlabel('Hora')
    plt.ylabel('Velocidad (Mbps)')
    plt.title('Velocidad de Internet durante el Día')
    plt.legend()
    plt.savefig(f"internet_speed_{str(date.today())}.png")
    plt.close()

# Intervalo de tiempo en segundos (por ejemplo, una hora = 3600 segundos)
interval = 360
last_day_checked = date.today()

print("Processing...")
print("Press Ctrl+C to stop the program")
while True:
    current_day = date.today()
    if not os.path.exists(f"internet_speed_{str(date.today())}.png"):
        generate_daily_graph()
        last_day_checked = current_day
    download_speed, upload_speed, ping = test_speed()
    network_name = get_network_name()
    write_to_csv(network_name, download_speed, upload_speed, ping)
    time.sleep(interval)