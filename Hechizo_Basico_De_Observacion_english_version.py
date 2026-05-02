import psutil
from datetime import datetime

def system_state():
    print("🧙‍♂️ System State: \n")

    #datetime_now
    now = datetime.now()
    print(f"⏰Hora: {now.strftime('%Y-%m-%d %H:%M:%S:')}")

    #CPU
    cpu = psutil.cpu_percent(interval=1)
    print(f"⚙️ CAM used: {cpu}%")

    ram = psutil.virtual_memory()
    print(f"🧠 RAM used: {ram.percent}%")

    #warnings
    if cpu > 80:
        print("⚠️WARNING: CPU is almost full!")
    if ram.percent > 80:
        print("⚠️Warning: RAM is almost full!")

if __name__ == "__main__":
    system_state()