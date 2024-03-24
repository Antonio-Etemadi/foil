import select
import sys
import time
import gc
import asyncio 


def update():
    
    try :
        from github_cloner import Git_cloner
    except :
        import urequests as requests
        url = "https://raw.githubusercontent.com/Antonio-Etemadi/github_cloner/main/github_cloner/github_cloner.py"
        response = requests.get(url)
        if response.status_code == 200:
            with open("github_cloner.py", "wb") as file:
                file.write(response.content)
            print("File downloaded successfully.")
        else:
            print("Failed to download the file.")

    from github_cloner import Git_cloner
    url="https://github.com/Antonio-Etemadi/foil"
    cloner = Git_cloner(url,console_log_level="DEBUG")
    gc.collect()
    cloner.run_cloner()

def main1():
    stdin = sys.stdin
    read_list = [stdin]
    start_time = time.time()
    max_wait_time = 3
    print("\033[33mAre you want update\033[0m")
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    b=0
    while time.time() - start_time < max_wait_time:
        readable, _, _ = select.select([sys.stdin], [], [],0.1)
        b = (b + 1) % len(symbols)
        print('\r%s \033[33mFor yes type "y" for no type "n" : \033[0m' % symbols[b], end='\r')
        if stdin in readable:
            user_input = stdin.read(1)
            if user_input.lower() == 'y':
                print("\nupdating...")
                update()
                
                break
            if user_input.lower() == 'n':
                print("\nExiting the updating...")
                break

    print("\nExiting updating.")
    
    
async def main():
    from main_f import read_loop, blink_loop
    tasks = [read_loop(), blink_loop()]
    await asyncio.gather(*tasks)
 

if __name__ == "__main__":
    main1()
    print("========================")
    gc.collect()
    asyncio.run(main())

