echo '[+] Downloading the GeoIp database'
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
gunzip GeoLiteCity.dat.gz
mkdir /opt/GeoIP
mv GeoLiteCity.dat /opt/GeoIP/Geo.dat
echo '[+] Installing pygeoip'
pip install pygeoip
