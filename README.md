# Network monitor 

This application uses nmap to scan your network for devices, and then tries to lookup information about those devices.

To run this app you will need:
- python3: https://www.python.org/downloads/
- nmap: https://nmap.org
- flask: `pip install Flask` https://flask.palletsprojects.com/en/2.1.x/installation/

Once installed, run the command `flask run` and in a browser visit: `http://127.0.0.1:5000` (tested in Chrome only)

You can modify `deviceRange = '192.168.86.2-255'` in `app.py` to change the default range of IP's you want to scan

![Home network monitor](/netmon.png "Demo")    