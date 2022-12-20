#!/usr/bin/env bash
# Install Nginx
package { 'nginx':
  ensure => present,
}

# Create a custom configuration file for Nginx
file { '/etc/nginx/conf.d/custom_http_response_header.conf':
  ensure  => file,
  content => 'server {
    listen 80;
    server_name _;

    add_header X-Served-By $hostname;
}',
  notify  => Service['nginx'],
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure => running,
  enable => true,
}
