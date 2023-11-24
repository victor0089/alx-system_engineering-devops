#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
  # Installs puppet-lint
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => gem,
}
