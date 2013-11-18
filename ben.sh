#! /bin/bash

# number of iterations
n=${1:-100}
prog=./src/wrapper

function _bench() {
    local algo=$1
    local width=$2
    local inp=$3

    local b=$(time (for i in $(seq 1 $n); do
        echo a >> q
        $prog --algo $algo -w $width < benchmarks/${3}.txt > /dev/null
    done) 2>&1 1>/dev/null)
    echo "$b" | grep real | cut -f2
}

# long25  -- input=long.txt width=25
# long45  -- input=long.txt width=45
# lorem10 -- input=lorem.txt width=10
# lorem70 -- input=lorem.txt width=70

echo "Running $n iterations"
echo "                        long25    long45    lorem10   lorem70"
echo "                        -------------------------------------"
for alg in `$prog --ls`; do
    printf "%-20s: " $alg
    printf "%10s" $(_bench $alg 25 long)
    printf "%10s" $(_bench $alg 45 long)
    printf "%10s" $(_bench $alg 10 lorem)
    printf "%10s" $(_bench $alg 70 lorem)
    printf "\n"
done
