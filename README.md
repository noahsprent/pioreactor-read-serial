## Pioreactor Read Serial Plugin 

This plugin takes a json coming in on serial and writes the individual key:value pairs out to MQTT so they can be accessed by different jobs. 
For example, one might want an aruduino to send a json with key:value pairs for voltages from different analogue pins over serial in order to e.g. read from vernier sensors.
You can set this job to run automatically on starting the pi and then whenever you start any jobs that need it it will be available.

## Installation

Install from the Pioreactor plugins web interface or the command line:

```
pio install-plugin pioreactor-read-serial # to install directly on the Pioreactor

# OR, on the leader's command line:

pios install-plugin pioreactor-read-serial # to install on all Pioreactors in a cluster
```

Or install through the web interface (_Plugins_ tab). This will install the plugin on all Pioreactors within the cluster.

## Usage

#### Run on startup

The script should start on boot, as it is added to systemctl by the install script. 
If you don't want this to happen, and would prefer to start it manually (perhaps because you're accessing serial directly for something else), first disable autorunning through systemctl and then you can control using the below.

#### Through the command line:
```
pio run pioreactor_read_serial
```

#### Through the UI:

Under _Manage_, there will be a new _Activities_ option called _pioreactor_read_serial_. 
Editable settings are the baud rate of the serial and the serial port.

## Plugin documentation

Documentation for plugins can be found on the [Pioreactor docs](https://docs.pioreactor.com/developer-guide/intro-plugins).
