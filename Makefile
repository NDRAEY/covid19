VER 	= 	1.1
REL 	= 	1
file 	=	main.py

all:
	echo "Making main.py executable"
	chmod +x main.py
	
build-debian:
	echo "Copying files..."
	cp $(file) debian/build/covid19_$(VER)-$(REL)/usr/local/bin/covid19
	chmod +x debian/build/covid19_$(VER)-$(REL)/usr/local/bin/covid19
	echo "\e[4mBuilding\e[0m debian package"
	dpkg-deb --build debian/build/covid19_$(VER)-$(REL)
	mv debian/build/covid19_$(VER)-$(REL).deb debian/
	echo "\e[32m\e[1mcovid19_$(VER)-$(REL).deb in debian/ folder\e[0m" 

install:
	echo "Installing main.py into /usr/local/lib/covid19"
	cp main.py /usr/local/bin/covid19
	chmod +x /usr/local/bin/covid19
	
uninstall:
	rm /usr/local/bin/covid19
