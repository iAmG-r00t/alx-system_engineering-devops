# 0x0A. Configuration management

## Resource

- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://puppet.com/docs/puppet/5.5/types/file.html) (*Check "Resource types" for all manifest types in the left menu*)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)
- [Puppet CookBook](https://www.puppetcookbook.com/)

## Installing `puppet` and `puppet-lint`

```sh
# installing puppet
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet

# installing puppet-lint
gem install puppet-lint
```

## Tasks

<details>
<summary><a href="./0-create_a_file.pp">0. Create a file</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/NM2k46hX/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-install_a_package.pp">1. Install a package</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/PqVvKj7c/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./">1. Execute a command</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/CxZFC13P/image.png' border='0' alt='image'/></a>
</details>
