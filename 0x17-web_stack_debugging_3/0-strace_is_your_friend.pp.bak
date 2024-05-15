# Fix apache 500 internal server error using strace

exec {'500 error fix':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/var/www/html/wp-settings.php',
}
