#!/bin/bash

read -p "Enter the page ID to ignore: " page_id
line=$(awk '/\$ids/{print NR; exit}' inc/func.php)
sed -i  "${line} s/];/,${page_id}];/" inc/func.php
