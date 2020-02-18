wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh

sleep 1

chmod +x shadowsocks.sh

sleep 1

sudo ./shadowsocks.sh 2>&1 | tee shadowsocks.log

sleep 1

rm /etc/shadowsocks.json

touch /etc/shadowsocks.json

echo '{
  "server":"0.0.0.0",
  "local_address":"127.0.0.1",
  "local_port":1080,
  "port_password":{
      "43340":"777777",
      "43341":"777777",
      "43342":"777777",
      "43343":"777777",
      "43344":"777777",
      "43345":"777777",
      "43346":"777777",
      "43347":"777777",
      "43348":"777777",
      "43349":"777777",
      "43350":"777777",
      "43351":"777777",
      "43352":"777777",
      "43353":"777777",
      "43354":"777777",
      "43355":"777777",
      "43356":"777777",
      "43357":"777777",
      "43358":"777777",
      "43359":"777777",
      "43360":"777777"
  },
    "timeout":300,
    "method":"rc4-md5",
    "fast_open":false
}' > /etc/shadowsocks.json

ssserver -c /etc/shadowsocks.json -d restart

sleep 1

modprobe tcp_bbr