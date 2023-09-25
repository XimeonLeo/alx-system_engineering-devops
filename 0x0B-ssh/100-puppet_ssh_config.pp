# Modifying the ssh/config file
include stdlib

file_line { 'Disabling Passwd Auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     PasswordAuthentication no',
  replace => true,
}

file_line { 'Setting identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     IdentityFile ~/.ssh/school',
  replace => true,
}
