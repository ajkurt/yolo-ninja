# yolo-ninja
RaspMate + Flask + I2C
==

Install tools nededs:

	$ apt-get install python-requests python-pip python-smbus i2c-tools samba
	$ pip install flask

Don't start apache on boot:

	$ update-rc.d apache2 remove

 Edit /etc/samba/smb.conf:
 
	[RaspRoot]
	comment=Raspberry Pi Root
	browseable=yes
	path=/root
	public=yes
	writable=yes
	guest ok=yes
	read only=no
	create mask = 0777
	directory mask = 0777
	
Start Samba:

	$ update-rc.d samba defaults
	$ service samba start

Teste I2C:

	$ i2cdetect -y 1

Install Localepurge:

	$ apt-get install localepurge 
  
Install deborphan:

	$ apt-get install deborphan 
  
Clean and purge unused locales and orphans:

	$ localepurge
	$ apt-get remove --purge `deborphan --guess-all`
	$ apt-get clean
  
Pull Yolo-Ninja Project;
Conect RPI Pin 03 on Arduino 20, 05 on 21 and GND on GND.
