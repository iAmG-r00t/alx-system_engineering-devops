# 0x0D. Web stack debugging #0 

## Resource

### Concepts

<details>
<summary>Network basics</summary><br>
<ul>
  <li>Networking is a big part of what made computers so powerful and why the Internet exists. It allows machines to communicate with each other.
  <ul> <li><a href="https://www.techtarget.com/searchnetworking/definition/protocol">What is a protocol.</a></li> </ul>
  <ul> <li><a href="https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm">What is an IP address.</a></li> </ul>
  <ul> <li><a href="https://www.techtarget.com/searchnetworking/definition/TCP-IP">What is TCP/IP.</a></li> </ul>
  <ul> <li><a href="https://www.lifewire.com/port-numbers-on-computer-networks-817939">What is an Internet Protocol (IP) port?.</a></li> </ul>
  </li>
</ul>
</details>

<details>
<summary>Docker</summary><br>
<ul>
  <li>Readme
  <ul> <li><a href="https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/">What is Docker and why is it popular</a></li> </ul>
  </li>
</ul>

<details>
<summary>Let's first pull a Docker image and run a container:</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/13tHWGzc/image.png' border='0' alt='image'/></a>
</details>

Note that `docker` command will pull the Ubuntu docker container image from the Internet and run it. I let you look at the meaning of the flags using the command `docker run --help`, the main idea is that it keeps the container up and running.

<details>
<summary>To execute a command on the Docker container, use *docker exec*:</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/fLLDygWS/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary>If you want to connect to your Docker container and use Bash, you need to use *docker exec -ti*:</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/433xH3B3/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary>If you want to stop a container, use *docker stop*:</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/sxCzmf97/image.png' border='0' alt='image'/></a>
</details>

</details>

## Tasks

<details>
<summary><a href="./0-give_me_a_page">0. Give me a page!</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/yxybJXPm/image.png' border='0' alt='image'/></a>
</details>
