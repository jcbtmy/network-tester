## Network Tester


### Introduction

This is a simple python application I'm using to test my home network and the ISP for the lag/RTT for certain game servers.
The program pings the default gateway and a list of game servers in serverlist.json to determine the rtts. This can be useful to determine whether the bottleneck is in your home LAN or from your internet connection.

### Requirements 

    python
    pip3
    icmplib
    matplotlib
    netifaces

### Install

    pip3 install -r requirements.txt

### Run

    python3 main.py

### Maintainers

jcbtmy@gmail.com -- Jacob Toomey

    