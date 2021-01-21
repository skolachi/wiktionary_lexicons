split -l 1 $1 dict

for seg in `find . -name "dict*"`; do
        nohup bash $seg &> dict.log &
done

