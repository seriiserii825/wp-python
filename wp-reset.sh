#!/bin/bash

has_wp=$(which wp)
if [ -z "$has_wp" ]; then
  curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
  chmod +x wp-cli.phar
  sudo mv wp-cli.phar /usr/local/bin/wp
fi

if [[ ! -f style.css ]]; then
  echo "${tmagenta}Go to wp theme folder${treset}"
  exit 1
fi


theme_url=$(pwd)

rm .mysql_sock

cd ../../../../../

rm wp-cli*

echo "${tmagenta}Removed all wp settings${treset}"


