# System monitoring script

import psutil #this one to check system resources
import speedtest as sp #this one to check internet speed


def resources():
    cpu = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print(f"CPU: {cpu}%", f"Memory: {memory}%", f"Disk: {disk}%")
    
    return cpu, memory, disk

def speed_test():
    speed = sp.Speedtest()
    speed.get_best_server()
    
    download_speed = speed.download()
    download = download_speed / 10**6
    print(f"Download speed: {download:.2f} Mbps")
        
    upload_speed = speed.upload()
    upload = upload_speed / 10**6
    print(f"Upload speed: {upload:.2f} Mbps")
    
    return download, upload



resources()
speed_test()
    

