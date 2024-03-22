try :
    from ota_cloner import OTA
except :
    import urequests as requests

    url = "https://raw.githubusercontent.com/Antonio-Etemadi/foil/main/ota_cloner.py"
    response = requests.get(url)

    if response.status_code == 200:
        with open("ota_cloner.py", "wb") as file:
            file.write(response.content)
        print("File downloaded successfully.")
        from ota_cloner import OTA
    else:
        print("Failed to download the file.")

url = "github.com/repos/Antonio-Etemadi/foil"
ota_instance = OTA(url)
ota_instance.run_ota()
