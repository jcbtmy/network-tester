

from icmplib import traceroute, multiping, ping
import matplotlib.pyplot as plt
import netifaces
import json

def get_server_list():

    fs = open("serverlist.json")
    rawData = fs.read()

    return json.loads(rawData)


def get_default_gateway():
    
    gws = netifaces.gateways()

    return gws['default'][netifaces.AF_INET][0]


def do_test(ipAddrs, count):
    
    response = ping(ipAddrs, count=count, interval=0.1, payload_size=5024, privileged=False)

    if response.is_alive:
        return response.rtts
    else:
	    return None


def make_window(tests, count):
	
    x = [x*100 for x in range(0,count)]

    for test in tests:    
        if test["rtts"] != None:
            plt.plot(x, test["rtts"], label=test["display"])


    plt.legend()
    plt.ylabel("Round Trip Millisecond")
    plt.xlabel("Intervall Millisecond")
    plt.show()


def main():

    count = 10

    serverlist = get_server_list()
    gatewayaddr = get_default_gateway()

    serverlist.insert(0, { "host" : gatewayaddr , "display": "gateway"} )
	
    print("Running Tests...")

    for server in serverlist:
        server["rtts"] = do_test(server["host"], count)

    make_window(serverlist, count)






if __name__ == "__main__":
    main()
