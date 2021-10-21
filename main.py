

from icmplib import traceroute, multiping, ping
import matplotlib
import netifaces
import json

def getServerList():

    fs = open("serverlist.json")
    rawData = fs.read()

    return json.loads(rawData)


def getDefaultGateway():
    
    gws = netifaces.gateways()

    return gws['default'][netifaces.AF_INET][0]


def doTest(ipAddrs):
    
    response = ping(ipAddrs, count=5, interval=0.1, payload_size=5024, privileged=False)

    if response.is_alive:
        return response.rtts
    else:
        return None

def main():

    serverlist = getServerList()
    gatewayaddr = getDefaultGateway()

    serverlist.insert(0, { "host" : gatewayaddr } )

    for server in serverlist:
        server["rtts"] = doTest(server["host"])

    print(serverlist)






if __name__ == "__main__":
    main()
