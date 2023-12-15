# Install puppet-lint
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem'
}
#!/usr/bin/env puppet
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
