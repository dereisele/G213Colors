install :
	cp G213Colors.py /usr/bin/G213Colors.py
	cp main.py /usr/bin/g213colors-gui
	cp default.conf /etc/G213Colors.conf
	cp g213colors.service /etc/systemd/system/g213colors.service
	cp 99-g213colors.rules /etc/udev/rules.d/99-g213colors.rules
	chmod +x /usr/bin/G213Colors.py
	chmod +x /usr/bin/g213colors-gui
	cp icons/G213Colors-16.png /usr/share/icons/hicolor/16x16/apps/g213colors.png
	cp icons/G213Colors-24.png /usr/share/icons/hicolor/24x24/apps/g213colors.png
	cp icons/G213Colors-32.png /usr/share/icons/hicolor/32x32/apps/g213colors.png
	cp icons/G213Colors-48.png /usr/share/icons/hicolor/48x48/apps/g213colors.png
	cp icons/G213Colors-128.png /usr/share/icons/hicolor/128x128/apps/g213colors.png
	cp icons/G213Colors-192.png /usr/share/icons/hicolor/192x192/apps/g213colors.png
	cp G213Colors.desktop /usr/share/applications/g213colors.desktop
	gtk-update-icon-cache -q /usr/share/icons/hicolor/
	systemctl daemon-reload
uninstall :
	rm /usr/bin/G213Colors.py
	rm /usr/bin/g213colors-gui
	rm /etc/G213Colors.conf
	rm /etc/systemd/system/g213colors.service
	rm /usr/share/icons/hicolor/16x16/apps/g213colors.png
	rm /usr/share/icons/hicolor/24x24/apps/g213colors.png
	rm /usr/share/icons/hicolor/32x32/apps/g213colors.png
	rm /usr/share/icons/hicolor/48x48/apps/g213colors.png
	rm /usr/share/icons/hicolor/128x128/apps/g213colors.png
	rm /usr/share/icons/hicolor/192x192/apps/g213colors.png
	rm /usr/share/applications/g213colors.desktop
	gtk-update-icon-cache -q /usr/share/icons/hicolor/
	systemctl daemon-reload
