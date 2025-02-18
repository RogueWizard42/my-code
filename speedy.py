# internet speed test - zoom zoom

import speedtest as sp 

def speed_test():
    st = sp.Speedtest()
    
    download_speed = st.download()
    download = download_speed / 10**6
    print(f"Download speed: {download:.2f} Mbps")
    
    upload_speed = st.upload()
    upload = upload_speed / 10**6
    print(f"Upload speed: {upload:.2f} Mbps")
    
    
speed_test()
    
    
    
    