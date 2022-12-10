# Installing flask
package { 'pip install flask':
  ensure   => '2.1.0',
  provider => 'gem',
}
