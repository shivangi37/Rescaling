#!/bin/bash
# $1: Space-separated list of input files
# $2: Output file for merged content
# $3: Output file for frequency distribution

{
    echo "$1" | tr ' ' '\n' | while read -r input_file; do
        cat "$input_file"
    done
} > "$2"


awk '{diff = $3 - $2; print diff}' "$2" | sort -n | uniq -c | awk '{print $2, $1}' | tr ' ' '\t' > "$3"
