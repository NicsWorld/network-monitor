import nmap
import socket
from flask import Flask, render_template

app = Flask(__name__)

# Update this range to match your network
deviceRange = '192.168.86.2-255'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/range")
def range():
    return str(deviceRange)

@app.route("/api/devices")
def devices():
    nm = nmap.PortScanner()
    nm.scan(hosts=f'{deviceRange}', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    devices = []
    for host, status in hosts_list:
        print(host, status)
        try:
            hostThing = socket.gethostbyaddr(host)
            if (hostThing):
                devices.append(hostThing)
        except:
            # putting this in an array to match the format from hostThing
            unnamedDevice = ["Unnamed device", [], [host]]
            devices.append(unnamedDevice)

    return devices

@app.route("/api/length")
def lengthOfDevices():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.86.2-255', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    return str(len(hosts_list))