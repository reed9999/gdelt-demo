if [[ $# -eq 0 ]] ; then 
    exit "Requires exactly one parameter."
fi
echo "replace in file $1"

sed -f replace.sed < $1 > sed_ouput

