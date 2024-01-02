import speedtest

def speed_test():
    st = speedtest.Speedtest()

    download_speed = st.download() / 1_000_000
    print(f"Dowload: {download_speed:.2f} Mb/s")


speed_test()