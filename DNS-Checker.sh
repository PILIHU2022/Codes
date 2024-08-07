#! /usr/bin/bash
for dns in $(cat ./dns.list); do
    dig @${dns} github.com >> DNS-Checker.result
    echo $dns
    cat DNS-Checker.result | grep 'Query time' | sed 's/;; Query time://' | sed 's/^/Query time:/g'
done
