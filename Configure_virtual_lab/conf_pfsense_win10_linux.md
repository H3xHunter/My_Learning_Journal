
# How to configure a simple pfsense network in VirtualBox

## pfsense machine VM
- 1 GB RAM
- 8 GB HDD
- 1 Core
- remove USB, Audio 
- two networks:
  - NAT ----------------------| <-----------Internet
  - Internal Network ---------| <----------- Every machine you want to add to the network
  
### Installation on the VM:
Just follow everything as standar, but at the end you should have:
- WAN        -> em0               -> v4/DHCP4: <ip>  | This one is the one connected to internet
- LAN        -> em1               -> v4: <ip>        | This is the internal network

### Web Configurator:
- Skip everything 
- Change the default credentials: admin/pfsense
- Install IDS Snort
  - edit 
    - register to snort free pkg 
    - click on the all the rest free pkg you find 
    - update the signatures
    
## Windows config: 
  - Network:
    - IPV4
      - set an IP address in the range of the IP addresses of the internal network range
      - set default gataway and DNS to the pfsense IP address. 
      - install guest edition

## On linux:
  - vim /etc/network/interfaces
  - ```auto eth1
       allow-hotplug eth1
       iface eth1 inet dhcp
       ```
   - restart
   - click on connect on the top right 
