# Description: Install Flask version 2.1.0 using pip3

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0
exec { 'install_flask':
  command  => '/usr/bin/pip3 install flask==2.1.0',
  unless   => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require  => Package['python3-pip'],
}
