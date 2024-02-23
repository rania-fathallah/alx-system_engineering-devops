# Puppet manifest to install Flask version 2.1.0 using pip3

package { 'flask':
  ensure         => installed,
  provider       => 'pip3',
  install_options => ['--version', '2.1.0'],
}

