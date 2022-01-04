# 0x0B. SSH 

## Resource

- [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
- [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
- [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [SSH Config File](https://www.ssh.com/academy/ssh/config)
- [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
- [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
- [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc) (*(Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.*)

### For reference:

- [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
- [Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
- [IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)
- [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)
- [Request for Comments (RFCs)](https://en.wikipedia.org/wiki/Request_for_Comments)

## Tasks

<details>
<summary><a href="./0-use_a_private_key">0. Use a private key</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/yW4gBSpM/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-create_ssh_key_pair">1. Create an SSH key pair</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/pXPbpdbx/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-ssh_config">2. Client configuration file</a></summary><br>
<a href='https://postimg.cc/Hjb2CMHK' target='_blank'><img src='https://i.postimg.cc/y6brchGV/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary>3. Let me in!</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/3N2k9F3k/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./100-puppet_ssh_config.pp">4. Client configuration file (w/ Puppet)</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/ryBvRXzV/image.png' border='0' alt='image'/></a><br>
<ul><li>Install puppet stdlib module;</li></ul>
<pre>sudo puppet module install puppetlabs-stdlib</pre>
</details>

