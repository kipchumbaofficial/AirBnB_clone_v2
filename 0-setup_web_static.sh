#!/usr/bin/env bash
# Prepare webserver for deployment

# installing nginx
if ! command -v nginx $ > /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")

for directory in "${directories[@]}"
do
    if [ ! -d "$directory" ]; then
        mkdir -p "$directory"
    fi
done
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHello World!\n\t</body>\n</html>\n" > /data/web_static/releases/test/index.html

target=/data/web_static/current
from=/data/web_static/releases/test/

if [ -L "$target" ]; then
    rm "$target"
fi
ln -s "$from" "$target"

sudo chown -R ubuntu:ubuntu /data/

location_block="location /hbnb_static {\n\talias /data/web_static/current/;\n}"
sed -i "/server_name _;/a $location_block" /etc/nginx/sites-available/default

sudo service nginx restart
