import network
import time
import gc

#initial_memory = gc.mem_alloc()
#print(initial_memory)


def wifi(ssid_info,show=True , ap_ssid=None , ap_password=None):
    if not ssid_info:
        return print("no ssid to connect ")
    ap = network.WLAN(network.AP_IF)
    sta = network.WLAN(network.STA_IF)
    if not ap.active():
        print("Creating Access Point:", ap_ssid)
        ap.active(True)
        authmode = network.AUTH_WPA2_PSK
        if ap_password is not None:
           ap.config(essid=ap_ssid, password=ap_password, authmode=authmode)
        if ap_ssid is not None:
           ap.config(essid=ap_ssid)

    if not sta.active():
        sta.active(True)
        print("scan_for_networks")
        available_networks = [net[0].decode() for net in sta.scan()]
        for desired_ssid in ssid_info:
            if desired_ssid in available_networks:
                ssid = desired_ssid
                password = ssid_info[desired_ssid]

        print("connect_to_desired_network")
        sta.connect(ssid, password)
        b = []
        while not sta.isconnected():
            b.append("*")
            print("connecting to:","(",ssid,")", ''.join(b), end='\r')
            time.sleep(0.5)
        print("Connected to:", "(", ssid, ")")       
    
    if show:
        stored_ap_mac = ":".join("{:02x}".format(x) for x in ap.config('mac'))
        stored_sta_mac = ":".join("{:02x}".format(x) for x in sta.config('mac'))
        print("Station:", "ssid:", "(", sta.config('essid'), ")", "IP:", sta.ifconfig(), "STA MAC Address:", stored_sta_mac)
        print("Access Point:", "ssid:", "(", ap.config('essid'), ")", "IP:", ap.ifconfig(), "AP MAC Address:", stored_ap_mac)



ssid_info1 = {
    'Teknik_Ates_Ofis': 'Cevher.2023',
    'Antonio': 'aaaa1370'
}
wifi(ssid_info1 )
gc.collect()
#memory_after_gc = gc.mem_alloc()
#print(memory_after_gc)
#print(initial_memory-memory_after_gc)
