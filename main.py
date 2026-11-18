secret_code = 13
access_key = 9

def bits(number, width=4):
    return format(number & ((1 << width) - 1), f"0{width}n")

print("================================")
print("MY SECRET CODE SCANNER")
print("================================")

print("Scret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key:", access_key, "Binary:", bits(access_key))

print("PART 1: Bits and Binary")
print("Binary numbers are only 0 and 1.")
print("Secret code Binary:", bits(secret_code))
print("Access Key Binary:", bits(access_key))

and_result = secret_code & access_key
or_result = secret_code | access_key

print("AND Result:", and_result, "Binary:", bits(and_result))
print("OR Result:", or_result, "Binary:", bits(or_result))
print("AND keeps only position where both bits are 1.")
print("OR keeps postion where at least one bit is 1.")

NOT_result = (~secret_code) & access_key
XOR_result = secret_code ^ access_key

print("PART 3: NOT and XOR")
print("NOT secret within 4 bits:", NOT_result, "Binary:", bits(NOT_result))
print("XOR result:", XOR_result, "Binary:", bits(XOR_result))
print("XOR gives 1 when the bits are compared are different.")

left_shift = secret_code << 1
right_shift = secret_code >> 1

print("Left Shift Result:", left_shift, "Binary:", bits(left_shift))
print("Right Shift Result:", right_shift, "Binary:", bits(right_shift))
print("Left shift moves the bits to the left. Right shift moves bits to the right.")

xor_check = secret_code ^ 1

print("PART 5 - Odd or Even with XOR")
print("Secret code XOR 1:", xor_check)
if xor_check == secret_code - 1:
    print("Secret code is Odd because XOR with 1 reduced it by 1")
else:
    print("Secret code is Even because XOR with 1 increased it by 1")

bit_count = secret_code.bit_count()
print("PART 6: Coutning Bits")
print("Number of bits in Secret code:", bit_count)