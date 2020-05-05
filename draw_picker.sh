#!/bin/sh

# $1 is the id of the giveaway tweet. First arg.
echo Number of entries:
cat ../entries_$1.txt | wc -l

echo Winner:
cat ../entries_$1.txt | shuf -n 1