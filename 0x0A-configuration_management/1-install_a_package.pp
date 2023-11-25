#!/usr/bin/pup
# Ensure the 'python3-pip' package is installed
package { 'python3-pip':
  ensure => installed,
}
# Install an especific version of flask (2.1.0)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
  }
