#!/bin/bash
#return all methods in the server
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
