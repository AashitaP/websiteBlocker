import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.twitter.com", "twitter.com", "www.gmail.com", "gmail.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        with open(hosts_path, 'r+') as file: #r+ can read and append (not write)
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file: #r+ can read and append (not write)
            content = file.readlines() #creates a list with all lines
            file.seek(0) #place the pointer at the start
            for line in content:
                if not any(website in line for website in website_list): #if no website is mentioned in the line, append the line
                    file.write(line) #so it basically copies all the lines except the website ones
            file.truncate() #after going through the file, it will delete whats below
    time.sleep(5)
