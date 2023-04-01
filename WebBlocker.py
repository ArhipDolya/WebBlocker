import time
from datetime import datetime


start_hour = int(input("Write the hour from which you want to start blocking: \n"))
start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, start_hour)

finish_hour = int(input("Write the hour from which you want to finish blocking: \n"))
finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, finish_hour)


hosts = "C:\Windows\System32\drivers\etc\hosts"
redirect_url = '127.0.0.1'


#You can write in the list any site you want
blocked_websites = ["youtube.com", "www.youtube.com", 'leetcode.com']

while True:

    if start_time < datetime.now() < finish_time:
        print('Access restricted')

        # Resrict access to websites
        with open(hosts, 'r+') as file:
            data = file.read()

            for site in blocked_websites:
                if site in data:
                    pass
                else:
                    file.write(f'{redirect_url} {site}\n')

    else:

        # Allow access to websites
        with open(hosts, 'r+') as file:
            data = file.readlines()
            file.seek(0)

            for line in data:
                if not any(site in line for site in blocked_websites):
                    file.write(line)
            file.truncate()

        print('Access available')

    time.sleep(5)