#! /usr/bin/bash
for dns in $(cat ./DNS.list); do
    rm ./DNS-Checker.result
    touch ./DNS-Checker.result
    chmod 777 ./DNS-Checker.result
    dig @${dns} github.com >> DNS-Checker.result
    echo $dns
    cat DNS-Checker.result | grep 'Query time' | sed 's/;; Query time://' | sed 's/^/ -&/g'
done
