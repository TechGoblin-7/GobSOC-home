import psutil

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent


    net_stats = {
        iface: {
            "is_up": stats.isup,
            "speed": stats.speed,
            "mtu": stats.mtu
        }
        for iface, stats in psutil.net_if_stats().items()
    }

    return {
        "cpu_percent": cpu,
        "ram_percent": ram,
        "disk_percent": disk,
        "net_status" :net_stats
    }