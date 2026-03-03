import speedtest as st 

### Creating the Function 

def speed_test():
    print("Displaying a result : Wait few minutes:: ")
    test = st.Speedtest()
    download = test.download() ### Measured the Download speed 
    download = round(download/10**6,2)
    print(download)### bps 
    upload = test.upload()
    upload = round(upload / 10**6,2)
    print(upload)
    ping = test.results.ping
    print(ping)
speed_test()