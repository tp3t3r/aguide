#!/bin/bash

sudo mkdir /mnt/guider-temp
sudo mount -t tmpfs -o rw,size=1G tmpfs /mnt/guider-temp/
sudo chown peter:peter /mnt/guider-temp/
ln -s /mnt/guider-temp/evf.png evf.png

