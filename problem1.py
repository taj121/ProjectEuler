import sys

def is_int_string( s ):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sum_all_mul_3_5( upTo ):
    total = 0
    for x in range(0, upTo):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total

    
if not( len( sys.argv) == 2):
    print "Error! Please enter a number as argument"
elif not( is_int_string(sys.argv[1]) ):
    print "Error! Please Enter a number!"
else:
    print sum_all_mul_3_5( int(sys.argv[1]) )


