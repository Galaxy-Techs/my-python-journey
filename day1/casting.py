#casting means changing or specifying the data type of a variable


#casting from integer to float
num_value = 34
print(type(num_value))
#casting
cast_value = float(num_value)
print(type(cast_value))


# casting from float to integer
commission_amount = 50.68
print(type(commission_amount))
# casting
cast_commision = int(commission_amount)
print(type(cast_commision))
print(cast_commision)

#casting from integer to string
num_value2 = 3
print(str(num_value2))
print(type(str(num_value2)))

#casting from float to string
float2 = 9.88
print(float2)
print(type(float2))
cast_print = str(float2)
print(type(cast_print))
print( )

#casting from complex to string
complex_value1 = 8j
print(complex_value1)
print(type(complex_value1))
cast_complex = str(complex_value1)
print(type(cast_complex))

#casting from string to int
string_value = "25"
print(string_value)
print(type(string_value))
cast_str_int = int(string_value)
print(type(cast_str_int))

#ERROR!! a string of int, float only not characters.
#string_value2 = "string"
#print(string_value2)
#print(type(string_value2))
#cast_str_int = int(string_value2)
#print(type(cast_str_int))