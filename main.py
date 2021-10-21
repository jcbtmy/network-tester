

from icmplib import traceroute, multiping, ping
import matplotlib
import netifaces
import json

def get_server_list():

    fs = open("serverlist.json")
    rawData = fs.read()

    return json.loads(rawData)


def get_default_gateway():
    
    gws = netifaces.gateways()

    return gws['default'][netifaces.AF_INET][0]


def do_test(ipAddrs):
    
    response = ping(ipAddrs, count=5, interval=0.1, payload_size=5024, privileged=False)

    if response.is_alive:
        return response.rtts
    else:
        return None

def main():

    serverlist = get_server_list()
    gatewayaddr = get_default_gateway()

    serverlist.insert(0, { "host" : gatewayaddr } )
	
	print("Running Tests...")

    for server in serverlist:
        server["rtts"] = do_test(server["host"])

    print(serverlist)






if __name__ == "__main__":
    main()
