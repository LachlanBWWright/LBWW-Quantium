echo "Beginning Testing."
#Activate Virtual Environment
#Execute Test Suite
#Return 0 if test have passed, or else 1

pytest
echo "The program exited with code" $?