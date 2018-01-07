#!/usr/bin/python

print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve  = 0b1100
print bin(12)
for i in range(2,6):
    print bin(i)

#Base 2 is binary
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
print int("1100",2) # prints 12
print int("11001001",2)

# Left Bit Shift (<<)
#0b000001 << 2 == 0b000100 (1 << 2 = 4)
#0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>)
#0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
#0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)


#shift right twice
shift_right = 0b1100
#shift left twice
shift_left = 0b1
shift_right = 0b1100 >> 2
shift_left = 0b1 << 2
print bin(shift_right)
print shift_right
print bin(shift_left)
print shift_left


# AND
#     a:   00101010   42
#     b:   00001111   15
#     ==================
# a & b:   00001010   10
print bin(0b101010 & 0b1111) # should be 0b1010

# OR
#     a:  00101010  42
#     b:  00001111  15
#     ================
# a | b:  00101111  47
print bin(0b101010 | 0b1111) # should be 0b101111

#XOR
#     a:  00101010   42
#     b:  00001111   15
#     =================
# a ^ b:  00100101   37
print bin(0b101010 | 0b1111) # should be 0b100101

print ~1
print ~2
print ~3
print ~42
print ~123

#Check if 4th bit is on usin AND
def check_bit4(input):
    mask = 0b1000
    if mask & input == 0:
        return "off"
    else:
        return "on"

#Turn on 4th bit usin OR
a = 0b10110111
mask = 0b1000
print bin(a | mask)

#Flip Out 8 bits using XOR
a = 0b11101110
mask = 0b11111111
print bin(mask ^ a)



#Slip and Slide using shifts
def flip_bit_old(number,n):
    mask = 0b1 << (n-1)
    if type(number) == int:
        result = number ^ mask
    else:
        result = int(number,2) ^ mask
    return bin(result)

#CodeAcademy code
def flip_bit(number, n):
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)

print flip_bit('0b111',2)
print flip_bit_old('0b111',2)
print flip_bit(2,2)
print flip_bit_old(2,2)