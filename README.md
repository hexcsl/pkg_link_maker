# pkg_link_maker v.1.4
Package link maker make by [Alex_1985](http://www.pspx.ru/forum/member.php?u=458658) and In1975

This tool automaticaly scan lan, find pkgs in currentdir, extract content-id from pkgs, replace whitespaces in package's names (they are critical), automaticaly create package_link.xml with package's names and their content-id.
After tool run HFS.exe with list of packages.

Also Now it can download from PSNStuff *.pkg files (To Full Game need create fake pkg for *.rif file and act.dat)

### Request:
[Python](https://www.python.org/downloads/) (add path workdir python) or use [build](https://github.com/nikolaevich23/pkg_link_maker/tree/master/build)

### Prepare with Ps3Xploit:
* copy category_game.xml to PS3 
    - add file from dir "pett_mount_and_copy" to hfs.exe
    - copy file from dir "to usb" to usb000
    - on PS3 goto local server (ex. 192.168.1.1)
	- check USB (in PHOTO/VIDEO)
    - Run lite version of PETT:
		- Press "1. Mount...", if OK "Press after 1 and 2" - Flsh1 FAT mount to /dev/blind
		- After mounting run exploit again and press "2. Copy file" if OK "Press after 1 and 2".
		- Restart.
	```
	You need be careful because size of category_game.xml and right port are critical.
	Paths and size are written in file.js
	```
### Usage
* just put *.pkg or pkgs in directory
* run package_link_maker.py
* copy after package_link.xml in usb (01 or 00)
* put usb in PS3
* Install pkg
* enjoy 

### Использование:
* Делаете подготовку, копируете с помощью pett на пс3 (см. Prepare)
* Помещаете ваши pkg в директорию 
* Запускаете package_link_maker.py 
* Копируете package_link.xml на флешку. Флешку в PS3 (любой порт) 
* Запускаете HEN ( и устанавливаете pkg файлы. 
