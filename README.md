# G213Colors
A application to change the key colors on a Logitech G213 Prodigy Gaming Keyboard using [SebiTimeWaster](https://github.com/SebiTimeWaster)'s [G213Colors](https://github.com/SebiTimeWaster/G213Colors).

## Supported devices

* G213 keyboard
* G203 mouse

## Screenshots
![g213-colors-static](https://user-images.githubusercontent.com/15942848/30737264-4bab741c-9f86-11e7-893b-3ec0398c85b9.png)
![g213-colors-cycle](https://user-images.githubusercontent.com/15942848/30737260-49058a04-9f86-11e7-9682-94fd42b98881.png)
![g213-colors-breathe](https://user-images.githubusercontent.com/15942848/30737256-45c8ca18-9f86-11e7-9fbc-ff9caa317e14.png)
![g213-colors-segments](https://user-images.githubusercontent.com/15942848/30737263-4b84ca42-9f86-11e7-83e7-dd84e464b601.png)

## What it does
G213Colors lets you set the color(s) and certain effects of the illuminated keys on a G213 keyboard and G203 mouse under Linux.

Since Logitech is mostly ignoring the Linux market with their "Logitech Gaming Software" but i also wanted to use my expensive new keyboard also under linux without tolerating the color cycling animation all the time. So i searched on the internet and added a gui to [SebiTimeWaster's project](https://github.com/SebiTimeWaster/G213Colors) for comfortable usage.

G213Colors was built and tested under Linux for the G213 keyboard and G203 mouse specifically, but after some adaptation it could potentially be run under other OS'es and used for other Logitech devices as well.

If you have any Logitech keyboard or mouse that is not supported feel free to open an issue and/or contact me via Email: git(AT)eiselecloud(DOT)de

The "Wave" color effect that is available with the Logitech software could not be replicated since it is completely generated in the software by updating the colors every x ms (In contrast to the other effects which run on the keyboard itself). You could generate this effect with a script, but since G213Colors has to detach the kernel driver from one of the G213's interfaces to send data out the multimedia keys would most likely stop working. Unfortunately this is a side effect of the linux driver structure.

## Installation
Clone this project with git and run `sudo make install`

Remark: The PyUSB and PyGObject libraries can be installed with (Running Ubuntu) running the `fix.sh` file or by pasteing:

```
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
pip install pycairo PyGObject
sudo make install
sudo python main.py
```

The desktop entry didn't work for me.
In case your python is not found for sudo, check your python with `whereis python` using the normal user. For example I had to replace the last python command with 
`sudo /home/user/miniconda3/bin/python main.py`

### Prerequisites
* [Python](https://www.python.org/) 3.x (which is usually already installed)
* [PyUSB](https://github.com/walac/pyusb) (please see their instructions on how to install)
* [PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject)

Please ignore the pcap directory, [SebiTimeWaster](https://github.com/SebiTimeWaster) added the pcap files he used for reverse engineering just in case someone wants to work with them. They can be opened with [Wireshark](https://en.wikipedia.org/wiki/Wireshark).

## Usage

### Automatic
You can find the app in your menu after installation.

### Manually
You can call the `main.py` script like this:

```Bash
python main.py
```

G213Colors needs to be run as root as long as long as your user doesn't have access privileges for the USB device.
In order to run the program without root privileges you have to create a [udev rule](https://wiki.archlinux.org/index.php/udev#About_udev_rules) for your device and add your user to the plugdev group. See [how this is done on stackexchange](https://stackoverflow.com/a/48477830/7809404). `idVendor` is *046d* for Logitech. `idProduct` depends on your device. Use `lsusb | grep Logitech` to determine the Id.

### Restoring previous state
After rebooting your pc you can restore the pre-reboot state by running the app with parameter -t

```Bash
sudo g213colors-gui -t
```

You can also do this automatically at reboot by enabling the systemd service.

```Bash
sudo systemctl enable g213colors.service
```

## Known issues


## ToDo


## Changelog
Changelog v0.1:
* Initial checkin

Changelog v0.2:
* Added segments/field support
* removed color button events

Changelog v0.3:
* Added more intergration with linux systems (by [JeroenED](https://github.com/JeroenED))

Changelog v0.4:
* Added support for G203 mouse

Changelog v0.5:
* Finally fixed incontrollable segments bug (with the help of [Oncecreated](https://github.com/oncecreated))
