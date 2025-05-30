#!/bin/bash

if [[ ! -f style.css ]]; then
  echo "${tmagenta}Go to wp theme folder${treset}"
  exit 1
fi

theme_url=$(pwd)
echo "${tmagenta}Theme URL: ${theme_url}${treset}"

echo "${tmagenta}Go to wp root folder${treset}"
cd ../../plugins
pwd

# check if exists directory advanced-custom-fields-wpcli
if [[ ! -d advanced-custom-fields-wpcli ]]; then
  echo "${tgreen}Installing ACF plugin${treset}"
  git clone https://github.com/hoppinger/advanced-custom-fields-wpcli.git
  echo "${tgreen}Activating ACF plugin${treset}"
  sleep 2
  wp plugin activate advanced-custom-fields-wpcli
else
  echo "${tgreen}ACF plugin already installed${treset}"
  wp plugin activate advanced-custom-fields-wpcli
fi

echo "${tgreen}Go to theme folder${treset}"

cd "$theme_url"


if ! grep -Fq "acfwpcli_fieldgroup_paths" functions.php
then
  echo "${tgreen}Added filter to functions.php at the end${treset}"

  cat <<TEST >> "functions.php"
add_filter( 'acfwpcli_fieldgroup_paths', 'add_plugin_path' );
function add_plugin_path( \$paths ) {
    \$paths['my_plugin'] = get_template_directory() . '/acf/';
    return \$paths;
  }
TEST
fi
