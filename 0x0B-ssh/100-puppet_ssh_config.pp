# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

include stdlib
file_line { 'SSH Config':
  path    => '/etc/ssh/ssh_config',
  line    => [
    '    IdentityFile ~/.ssh/school',
    '    PasswordAuthentication no'
  ],
  replace => true
}
