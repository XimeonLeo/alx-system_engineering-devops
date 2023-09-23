# creating a file /tmp/school using Puppet
file { '/tmp/school':
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
