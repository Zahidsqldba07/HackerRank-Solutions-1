for item in {1..99}
do
    if [[ $(($item % 2)) == 1 ]]; then
        echo $item
    fi
done

