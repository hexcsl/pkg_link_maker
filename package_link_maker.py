#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import glob
import socket
import subprocess
import urllib

def get_lan():
    """Gets the computer"s LAN IP"""
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        soc.connect(("10.255.255.255", 1))
        lan = str(soc.getsockname()[0])
        soc.close()
    except socket.error:
        soc.close()
        closer("ERROR: Unable to find LAN IP")

    return lan

def main():
    """The main logic"""
myip = get_lan()

def get_url(pkg_name):
    return "http://" + myip + "/" + pkg_name

def get_size(url):
    return urllib.urlopen(url).info().getheaders("Content-Length")[0]

content_id = []
pkgs = glob.glob("*.pkg")

for pkg in pkgs:
    os.rename(pkg, pkg.replace(" ","_"))

pkgs = glob.glob("*.pkg")

for pkg in pkgs:
    with open(pkg, "rb") as in_file:
        hfs = "hfs.exe " + pkg
        subprocess.Popen(hfs, shell = False)
        res = in_file.read(48)
        res = in_file.read(36)
        content_id.append(res)

pkgs_count = len(pkgs)

if not os.path.exists("to_usb"):
    os.makedirs("to_usb")

f = open(".\\to_usb\package_link.xml", "w")
f.write("<XMBML version=\"1.0\">\n"
        "    <View id=\"package_link\">\n"
        "        <Attributes>\n"
        "            <Table key=\"package_link_main\">\n"
        "                <Pair key=\"icon\"><String>/dev_usb000/download2.png</String></Pair>\n"
        "                <Pair key=\"title\"><String>Download and Install Package</String></Pair>\n"
        "                <Pair key=\"info\"><String>Download and Install Package from PC or PSNStuff</String></Pair>\n"
        "                <Pair key=\"ingame\"><String>disable</String></Pair>\n"
        "            </Table>\n"
        "        </Attributes>\n"
        "        <Items>\n"
        "            <Query\n"
        "                class=\"type:x-xmb/folder-pixmap\"\n"
        "                key=\"package_link_main\"\n"
        "                attr=\"package_link_main\"\n"
        "                src=\"#package_link_local_and_psnstuff\"\n"
        "            />\n"
        "        </Items>\n"
        "    </View>\n"
        "    <View id=\"package_link_local_and_psnstuff\">\n"
        "        <Attributes>\n"
        "            <Table key=\"package_link_local_main\">\n"
        "                <Pair key=\"icon\"><String>/dev_usb000/download2.png</String></Pair>\n"
        "                <Pair key=\"title\"><String>Download and Install Package from PC</String></Pair>\n"
        "                <Pair key=\"info\"><String></String></Pair>\n"
        "                <Pair key=\"ingame\"><String>disable</String></Pair>\n"
        "            </Table>\n"
        "            <Table key=\"package_link_psnstuff_main\">\n"
        "                <Pair key=\"icon\"><String>/dev_usb000/download2.png</String></Pair>\n"
        "                <Pair key=\"title\"><String>Download and Install Package from PSNStuff</String></Pair>\n"
        "                <Pair key=\"info\"><String></String></Pair>\n"
        "                <Pair key=\"ingame\"><String>disable</String></Pair>\n"
        "            </Table>\n"
        "        </Attributes>\n"
        "        <Items>\n"
        "            <Query\n"
        "                class=\"type:x-xmb/folder-pixmap\"\n"
        "                key=\"package_link_local_main\"\n"
        "                attr=\"package_link_local_main\"\n"
        "                src=\"xmb://localhost/dev_usb000/package_link_local.xml#package_link_local\"\n"
        "            />\n"
        "            <Query\n"
        "                class=\"type:x-xmb/folder-pixmap\"\n"
        "                key=\"package_link_psnstuff_main\"\n"
        "                attr=\"package_link_psnstuff_main\"\n"
        "                src=\"xmb://localhost/dev_usb000/package_link_psnstuff.xml#package_link_psnstuff\"\n"
        "            />\n"
        "        </Items>\n"
        "    </View>\n")
f.write("</XMBML>")
f.close()

f = open(".\\to_usb\package_link_local.xml", "w")
f.write("<XMBML version=\"1.0\">\n"
        "    <View id=\"package_link_local\">\n"
        "        <Attributes>\n")
for x in range(pkgs_count):
    url = get_url(pkgs[x])
    f.write("            <Table key=\"pkg_local_" + str(x) + "\">\n"
            "                <Pair key=\"icon\"><String>/dev_usb000/download.png</String></Pair>\n"
            "                <Pair key=\"title\"><String>" + pkgs[x] + "</String></Pair>\n"
            "                <Pair key=\"info\"><String>" + str(int(get_size(url))/1024) + " Mb</String></Pair>\n"
            "                <Pair key=\"ingame\"><String>disable</String></Pair>\n"
            "            </Table>\n")
f.write("        </Attributes>\n"
        "        <Items>\n")
for x in range(pkgs_count):
    f.write("            <Query\n"
            "                class=\"type:x-xmb/folder-pixmap\"\n"
            "                key=\"pkg_local_" + str(x) + "\"\n"
            "                attr=\"pkg_local_" + str(x) + "\"\n"
            "                src=\"#pkg_local_items_" + str(x) + "\"\n"
            "            />\n")
f.write("        </Items>\n"
        "    </View>\n\n")
for x in range(pkgs_count):
    url = get_url(pkgs[x])
    f.write("    <View id=\"pkg_local_items_" + str(x) + "\">\n"
            "        <Attributes>\n"
            "            <Table key=\"link" + str(x) + "\">\n"
            "                <Pair key=\"info\"><String>net_package_install</String></Pair>\n"
            "                <Pair key=\"pkg_src\"><String>" + url + "</String></Pair>\n"
            "                <Pair key=\"pkg_src_qa\"><String>" + url + "</String></Pair>\n"
            "                <Pair key=\"content_name\"><String>tool_pkg_install_pc</String></Pair>\n"
            "                <Pair key=\"content_id\"><String>" + content_id[x] + "</String></Pair>\n"
            "                <Pair key=\"prod_pict_path\"><String>/dev_usb000/download2.png</String></Pair>\n"
            "            </Table>\n"
            "        </Attributes>\n"
            "        <Items>\n"
            "            <Item class=\"type:x-xmb/xmlnpsignup\" key=\"link" + str(x) + "\" attr=\"link" + str(x) + "\"/>\n"
            "        </Items>\n"
            "    </View>\n\n")
f.write("</XMBML>")
f.close()

f = open(".\\to_usb\package_link_psnstuff.xml", "w")
f.write("<XMBML version=\"1.0\">\n"
        "    <View id=\"package_link_psnstuff\">\n"
        "        <Attributes>\n")
f.write("        </Attributes>\n"
        "        <Items>\n")
f.write("        </Items>\n"
        "    </View>\n\n")
f.write("</XMBML>")
f.close()

if __name__ == "__main__":
    main()