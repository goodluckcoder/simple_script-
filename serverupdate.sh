#!/bin/bash 
function test() {
	sudo apt-get update
	sudo apt-get install apache2
	sudo systemctl start apache2
     }
test
