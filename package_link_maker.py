#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import glob
import socket
import subprocess

host = "http://" + socket.gethostbyname(socket.gethostname()) + "/"

content_id = []
pkgs = glob.glob("*.pkg")

for pkg in pkgs:
    os.rename(pkg, pkg.replace(" ","_"))

pkgs = glob.glob("*.pkg")

for pkg in pkgs:
    if not os.path.exists("./bin/icons/" + pkg.replace(".pkg", ".PNG")):
        pkg_ripper = ".\\bin\PS3P_PKG_Ripper_1.3.exe -o ./bin/icons -s ICON0.PNG " + pkg
        subprocess.Popen(pkg_ripper, shell = False).wait()
        try:
            os.rename("./bin/icons/ICON0.PNG", "./bin/icons/" + pkg.replace(".pkg", ".PNG"))
        except:
            print "File ICON0.PNG not found."
    with open(pkg, "rb") as in_file:
        res = in_file.read(48)
        res = in_file.read(36)
        content_id.append(res)

hfs = ".\\bin\hfs.exe .\\bin\index.html "
for i in os.listdir(".\\"):
    hfs += i + " "
subprocess.Popen(hfs, shell = False)
pkgs_count = len(pkgs)

f = open(".\\to_usb\package_link.xml", "w")
f.write("<XMBML version=\"1.0\">\n"
        "    <View id=\"package_link\">\n"
        "        <Attributes>\n"
        "            <Table key=\"pkg_main\">\n"
        "                <Pair key=\"icon\"><String>" + host + "bin/icons/download.png" +"</String></Pair>\n"
        "                <Pair key=\"title\"><String>Download and Install Package from PC</String></Pair>\n"
        "                <Pair key=\"info\"><String></String></Pair>\n"
        "                <Pair key=\"ingame\"><String>disable</String></Pair>\n"
        "            </Table>\n"
        "        </Attributes>\n"
        "        <Items>\n"
        "            <Query\n"
        "                class=\"type:x-xmb/folder-pixmap\"\n"
        "                key=\"pkg_main\"\n"
        "                attr=\"pkg_main\"\n"
        "                src=\"#pkg_items\"\n"
        "            />\n"
        "        </Items>\n"
        "    </View>\n"
        "    <View id=\"pkg_items\">\n"
        "        <Attributes>\n")
for x in range(pkgs_count):
    f.write("            <Table key=\"pkg_local_" + str(x) + "\">\n"
            "                <Pair key=\"icon\"><String>" + host)
    if os.path.exists("./bin/icons/" + pkgs[x].replace(".pkg", ".PNG")):
        f.write("bin/icons/" + pkgs[x].replace(".pkg", ".PNG"))
    else:
        f.write("bin/icons/download.png")
    f.write("</String></Pair>\n"
            "                <Pair key=\"title\"><String>" + pkgs[x] + "</String></Pair>\n"
            "                <Pair key=\"info\"><String>" + str(format(float(os.path.getsize(pkgs[x]))/1024/1024, '.2f')) + " Mb</String></Pair>\n"
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
    f.write("    <View id=\"pkg_local_items_" + str(x) + "\">\n"
            "        <Attributes>\n"
            "            <Table key=\"link_" + str(x) + "\">\n"
            "                <Pair key=\"info\"><String>net_package_install</String></Pair>\n"
            "                <Pair key=\"pkg_src\"><String>" + host + pkgs[x] + "</String></Pair>\n"
            "                <Pair key=\"pkg_src_qa\"><String>" + host + pkgs[x] + "</String></Pair>\n"
            "                <Pair key=\"content_name\"><String>tool_pkg_install_pc</String></Pair>\n"
            "                <Pair key=\"content_id\"><String>" + content_id[x] + "</String></Pair>\n"
            "                <Pair key=\"prod_pict_path\"><String>" + host + "bin/icons/download.png" +"</String></Pair>\n"
            "            </Table>\n"
            "        </Attributes>\n"
            "        <Items>\n"
            "            <Item class=\"type:x-xmb/xmlnpsignup\" key=\"link_" + str(x) + "\" attr=\"link_" + str(x) + "\"/>\n"
            "        </Items>\n"
            "    </View>\n\n")
f.write("</XMBML>")
f.close()