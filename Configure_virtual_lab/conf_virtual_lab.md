# Guide to configure a simple VM LAB

## Configure VMWare
With VMware workstation pro
  - edit
    - Virtual network editor 
    - You need to create a subnet and a range of available IP addressses:
      - ![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/Virtual_network_editor.PNG)
    - After open each VM and make sure they are connected to the propper vmnet:
      - ![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/virtual_machine_settings.PNG)


## Configure Windows machine (victim):
On the windows machine(In the example W10) disable windows firewall and enable file sharing 

### Configuring the netwrok adapter propieties
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/windows_netwrok_connection.PNG)

### Change connection propieties:
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_windows1.PNG)

### Private network:
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_windows2.PNG)

### Advanced sharing settings:
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_windows3.PNG)


## Configure Linux machine:
One the linux machine just make sure that the network configuration is like the following:
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/etc_network_interfaces.PNG)

```
auto eth1
allow-hotplug-eth1
iface eth1 inet dhcp
```

## Some tests:

### ping the linux machine
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/ping_windows_to_linux.PNG)

### ping the windows machine
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/ping_windows_from_linux.PNG)

### Wireshark test
![](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/wireshark_dns_server_test.PNG)
