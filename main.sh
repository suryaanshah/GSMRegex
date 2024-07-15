#!/bin/bash

echo "Searching for : $@"



content = $(wget gsmarena\.com\/motorola_moto_g85-13144\.php -q -O -)
echo $content 



