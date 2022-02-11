#-*- coding: utf8 -*-


#Initial permut matrix for the datas
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#Initial permut made on the key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permut applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#SBOX
S_BOX = [
[
[2, 10, 14, 6, 4, 12, 8, 0, 7, 15, 11, 3, 1, 9, 13, 5] ,
[2, 0, 5, 7, 11, 9, 12, 14, 3, 1, 4, 6, 10, 8, 13, 15] ,
[9, 11, 4, 6, 0, 2, 13, 15, 3, 1, 14, 12, 10, 8, 7, 5] ,
[6, 11, 12, 1, 10, 7, 0, 13, 3, 14, 9, 4, 15, 2, 5, 8] ,
],
[
[13, 14, 5, 6, 0, 3, 8, 11, 1, 2, 9, 10, 12, 15, 4, 7] ,
[10, 15, 5, 0, 2, 7, 13, 8, 6, 3, 9, 12, 14, 11, 1, 4] ,
[7, 0, 1, 6, 5, 2, 3, 4, 11, 12, 13, 10, 9, 14, 15, 8] ,
[13, 9, 11, 15, 1, 5, 7, 3, 8, 12, 14, 10, 4, 0, 2, 6] ,
],
[
[2, 11, 8, 1, 0, 9, 10, 3, 14, 7, 4, 13, 12, 5, 6, 15] ,
[10, 15, 6, 3, 2, 7, 14, 11, 5, 0, 9, 12, 13, 8, 1, 4] ,
[11, 10, 3, 2, 5, 4, 13, 12, 8, 9, 0, 1, 6, 7, 14, 15] ,
[5, 13, 6, 14, 8, 0, 11, 3, 10, 2, 9, 1, 7, 15, 4, 12] ,
],
[
[4, 0, 9, 13, 8, 12, 5, 1, 7, 3, 10, 14, 11, 15, 6, 2] ,
[13, 9, 11, 15, 8, 12, 14, 10, 5, 1, 3, 7, 0, 4, 6, 2] ,
[15, 7, 3, 11, 10, 2, 6, 14, 5, 13, 9, 1, 0, 8, 12, 4] ,
[2, 12, 15, 1, 8, 6, 5, 11, 14, 0, 3, 13, 4, 10, 9, 7] ,
],
[
[13, 7, 4, 14, 10, 0, 3, 9, 11, 1, 2, 8, 12, 6, 5, 15] ,
[3, 6, 1, 4, 0, 5, 2, 7, 12, 9, 14, 11, 15, 10, 13, 8] ,
[12, 11, 10, 13, 0, 7, 6, 1, 8, 15, 14, 9, 4, 3, 2, 5] ,
[2, 11, 13, 4, 9, 0, 6, 15, 7, 14, 8, 1, 12, 5, 3, 10] ,
],
[
[3, 12, 13, 2, 0, 15, 14, 1, 11, 4, 5, 10, 8, 7, 6, 9] ,
[6, 12, 14, 4, 7, 13, 15, 5, 0, 10, 8, 2, 1, 11, 9, 3] ,
[15, 9, 2, 4, 10, 12, 7, 1, 5, 3, 8, 14, 0, 6, 13, 11] ,
[3, 9, 4, 14, 8, 2, 15, 5, 7, 13, 0, 10, 12, 6, 11, 1] ,
],
[
[3, 8, 4, 15, 5, 14, 2, 9, 11, 0, 12, 7, 13, 6, 10, 1] ,
[6, 2, 1, 5, 13, 9, 10, 14, 12, 8, 11, 15, 7, 3, 0, 4] ,
[11, 13, 7, 1, 10, 12, 6, 0, 5, 3, 9, 15, 4, 2, 8, 14] ,
[8, 10, 3, 1, 6, 4, 13, 15, 0, 2, 11, 9, 14, 12, 5, 7] ,
],
[
[7, 3, 4, 0, 15, 11, 12, 8, 14, 10, 13, 9, 6, 2, 5, 1] ,
[1, 6, 0, 7, 14, 9, 15, 8, 10, 13, 11, 12, 5, 2, 4, 3] ,
[6, 9, 1, 14, 12, 3, 11, 4, 13, 2, 10, 5, 7, 8, 0, 15] ,
[14, 6, 2, 10, 0, 8, 12, 4, 9, 1, 5, 13, 7, 15, 11, 3] ,
]
]

#Permut made after each SBox substitution for each round
P = [16,7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#Final permut for datas after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

#Matrix that determine the shift for each round of keys
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def bytes_to_bit_array(data):
    array = list()
    for char in data:
        binval = binvalue(char,8)#Get the char value on one byte
        array.extend([int(x) for x in list(binval)]) #Add the bits to the final list
    return array

def bit_array_to_bytes(array): #Recreate the string from the bit array
    res = b''.join([ int(y,2).to_bytes(1, byteorder='big') for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def nsplit(s, n):#Split a list into sublists of size "n"
    return [s[k:k+n] for k in range(0, len(s), n)]

class des():
    def __init__(self):
        self.key = None
        self.keys = list()
        
    def setkey(self, key):
        if len(key) < 8:
            raise "Key should be 8 bytes long"
        elif len(key) > 8:
            key = key[:8] #If key size is above 8 bytes, cut to be 8bytes long
        
        self.key = key
        self.generatekeys() #Generate all the keys
    
    def encrypt_block(self, input_block):

        if len(input_block) != 8:
            raise "Data should be 8 bytes long"

        block = bytes_to_bit_array(input_block)#Convert the block in bit array
        block = self.permut(block,PI)#Apply the initial permutation
        g, d = nsplit(block, 32) #g(LEFT), d(RIGHT)
        tmp = None
        for i in range(16): #Do the 16 rounds
            d_e = self.expand(d, E) #Expand d to match Ki size (48bits)
            tmp = self.xor(self.keys[i], d_e)#If encrypt use Ki
            tmp = self.substitute(tmp) #Method that will apply the SBOXes
            tmp = self.permut(tmp, P)
            tmp = self.xor(g, tmp)
            g = d                                    
            d = tmp
        result = self.permut(d+g, PI_1) #Do the last permut
        final_res = bit_array_to_bytes(result)
        return final_res #Return the final string of data ciphered/deciphered
       
    def substitute(self, d_e):#Substitute bytes using SBOX
        subblocks = nsplit(d_e, 6)#Split bit array into sublist of 6 bits
        result = list()
        for i in range(len(subblocks)): #For all the sublists
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2) | 3#Get the row with the first and last bit
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Column is the 2,3,4,5th bits
            val = S_BOX[i][row][column] #Take the value in the SBOX appropriated for the round (i)
            bin = binvalue(val, 4)#Convert the value to binary
            result += [int(x) for x in bin]#And append it to the resulting list
        return result
        
    def permut(self, block, table):#Permut the given block using the given table (so generic method)
        return [block[x-1] for x in table]
    
    def expand(self, block, table):#Do the exact same thing than permut but for more clarity has been renamed
        return [block[x-1] for x in table]
    
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x^y for x,y in zip(t1,t2)]
    
    def generatekeys(self):#Algorithm that generates all the keys
        self.keys = []
        key = bytes_to_bit_array(self.key)
        key = self.permut(key, CP_1) #Apply the initial permut on the key
        g, d = nsplit(key, 28) #Split it in to (g->LEFT),(d->RIGHT)
        for i in range(16):#Apply the 16 rounds
            g, d = self.shift(g, d, SHIFT[i]) #Apply the shift associated with the round (not always 1)
            tmp = g + d #Merge them
            self.keys.append(self.permut(tmp, CP_2)) #Apply the permut to get the Ki

    def shift(self, g, d, n): #Shift a list of the given value
        return g[n:] + g[:n], d[n:] + d[:n]
    

		
		
