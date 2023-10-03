# Automating the configuration of Nginx on a new Ubuntu
#machine

# updating the ubuntu server
exec { 'update ubuntu':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# ensure that nginx is installed
package { 'nginx_server':
  ensure   => present,
  provider => 'apt',
}
->
# Adding a Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}
->
# start service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
