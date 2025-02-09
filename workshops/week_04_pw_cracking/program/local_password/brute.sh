#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m' # No Color

while read -r password; do
	echo "Testing password: '$password'"
	output=$(./target/hackme "$password")

	if [[ "$output" == *"Access Granted"* ]]; then
		echo -e "${GREEN} Password found: ${BOLD} $password${NC}"
		exit 0
	fi
done < list.txt

echo -e "${RED} No valid password found.${NC}"
