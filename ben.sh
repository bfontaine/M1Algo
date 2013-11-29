#! /bin/bash

# number of iterations
n=${1:-100}
prog=./src/wrapper

function _bench() {
    local algo=$1
    local width=$2
    local inp=$3

    local b=$(time (for i in $(seq 1 $n); do
        $prog --algo $algo -w $width < samples/${3}.txt > /dev/null
    done) 2>&1 1>/dev/null)
    echo "$b" | grep real | cut -f2
}

# lorem10 -- input=lorem.txt width=10
# lorem70 -- input=lorem.txt width=70

echo "Running $n iterations"
echo "                        lorem10   lorem70"
echo "                        -----------------"
for alg in `$prog --ls`; do
    printf "%-20s: " $alg
    printf "%10s" $(_bench $alg 10 lorem400)
    if [ "$alg" != "backtracking" ];then
    printf "%10s" $(_bench $alg 70 lorem400)
    printf "\n"
fi
done
