install :
	cp G213Colors.py /usr/bin/G213Colors.py
	cp main.py /usr/bin/g213colors-gui
	cp default.conf /etc/G213Colors.conf
	chmod +x /usr/bin/G213Colors.py
	chmod +x /usr/bin/g213colors-gui
	cp icons/G213Colors-16.png /usr/share/icons/hicolor/16x16/apps/g213colors.png
	cp icons/G213Colors-24.png /usr/share/icons/hicolor/24x24/apps/g213colors.png
	cp icons/G213Colors-32.png /usr/share/icons/hicolor/32x32/apps/g213colors.png
	cp icons/G213Colors-48.png /usr/share/icons/hicolor/48x48/apps/g213colors.png
	cp icons/G213Colors-128.png /usr/share/icons/hicolor/128x128/apps/g213colors.png
	cp icons/G213Colors-192.png /usr/share/icons/hicolor/192x192/apps/g213colors.png
	cp G213Colors.desktop /usr/share/applications/g213colors.desktop
	cp be.jeroened.pkexec.g213colors.policy /usr/share/polkit-1/actions/
	gtk-update-icon-cache -q /usr/share/icons/hicolor/
	#### probe /sbin/openrc if exisits add boot/default  runner else.. 
    ifneq ("$(wildcard $(/sbin/openrc))","")
 	    rc-update add g213colors default
	    cp g213colors.openrc /etc/init.d/g213colors
	    # fix permisions +x g213colors openrc wont fix perms and enable otherwise. found out the hardway.. 
	    chmod +x /etc/init.d/g213colors
  	else
	    cp g213colors.service /etc/systemd/system/g213colors.service
	    systemctl daemon-reload
    endif

uninstall :
	rm /usr/bin/G213Colors.py
	rm /usr/bin/g213colors-gui
	rm /etc/G213Colors.conf
	rm /usr/share/icons/hicolor/16x16/apps/g213colors.png
	rm /usr/share/icons/hicolor/24x24/apps/g213colors.png
	rm /usr/share/icons/hicolor/32x32/apps/g213colors.png
	rm /usr/share/icons/hicolor/48x48/apps/g213colors.png
	rm /usr/share/icons/hicolor/128x128/apps/g213colors.png
	rm /usr/share/icons/hicolor/192x192/apps/g213colors.png
	rm /usr/share/applications/g213colors.desktop
	rm /usr/share/polkit-1/actions/be.jeroened.pkexec.g213colors.policy
	gtk-update-icon-cache -q /usr/share/icons/hicolor/
    ifneq ("$(wildcard $(/sbin/openrc))","")
	    rm /etc/init.d/g213colors
    else
	    rm /etc/systemd/system/g213colors.service
	    systemctl daemon-reload
    endif
