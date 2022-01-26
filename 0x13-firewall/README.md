# 0x13. Firewall 

<p align="center" />
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png" />
</p>

### Your servers without a firewall...

<p align="center" />
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif" />
</p>


## Resource

- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29) 
- [Port forwarding with iptables](https://www.cogini.com/blog/port-forwarding-with-iptables/)

## Tasks

<details>
<summary><a href="./0-block_all_incoming_traffic_but">0. Block all incoming traffic but</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/qq0ZGZVq/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./100-port_forwarding">1. Port forwarding</a></summary><br>

Firewalls can not only filter requests, they can also forward them.

Requirements:

	- Configure web-01 so that its firewall redirects port `8080/TCP` to port `80/TCP`.
	- Your answer file should be a copy of the `ufw` configuration file that you modified to make this happen
Terminal in `web-01`:

```sh
root@03-web-01:~# netstat -lpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2473/nginx
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      978/sshd
tcp6       0      0 :::80                   :::*                    LISTEN      2473/nginx
tcp6       0      0 :::22                   :::*                    LISTEN      978/sshd
udp        0      0 0.0.0.0:68              0.0.0.0:*                           594/dhclient
udp        0      0 0.0.0.0:54432           0.0.0.0:*                           594/dhclient
udp6       0      0 :::32563                :::*                                594/dhclient
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     SEQPACKET  LISTENING     7175     433/systemd-udevd   /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     6505     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8048     741/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     8419     987/acpid           /var/run/acpid.socket
root@03-web-01:~#
root@03-web-01:~# grep listen /etc/nginx/sites-enabled/default
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#   listen 8000;
#   listen somename:8080;
#   listen 443;
root@03-web-01:~#
```

- My web server `nginx` is only listening on port `80`
- `netstat` shows that nothing is listening on `8080`
Terminal in `web-02`:

```sh
ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:80
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:41 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
Accept-Ranges: bytes

ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:8080
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:43 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
Accept-Ranges: bytes

ubuntu@03-web-02:~$
```
I use curl to query `web-01.holberton.online`, and since my firewall is forwarding the ports, I get a `HTTP 200` response on port `80/TCP` and also on port `8080/TCP`.

</details>
