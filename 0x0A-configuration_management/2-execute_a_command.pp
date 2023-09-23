# a manifest that kils a process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
