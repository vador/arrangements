
class Bit_Field:
    bitF = None
    length = None

    def __init__(self,n=0):
        if n != 0:
            self.bitF = self.buildBitField(n)
            self.length = n

    def __copy__(self):
        new_Bit_Field = Bit_Field()
        new_Bit_Field.bitF = self.bitF
        new_Bit_Field.length = self.length
        return new_Bit_Field


    def buildBitField(self,n):
        bitF = 0
        power = 1
        for i in range(n+1):
            bitF += power
            power = power * 2
        return bitF

    def isBitSet(self, n):
        p = pow(2, n+1)
        return (self.bitF & p == p)

    def setBit(self, n):
        p = pow(2, n+1)
        if (self.bitF & p == 0):
            self.bitF += p

    def unsetBit(self, n):
        p = pow(2, n+1)
        if (self.bitF & p == p):
            self.bitF -= p

def output_arrangements(bitField, radix, length, cnt):
    if  len(radix) == length:
        print(cnt, " : ", radix)
        cnt += 1
        return cnt
    for i in range(bitField.length):
        if bitField.isBitSet(i):
            # Here we assume the set contains numbers : could use a conversion function for symbols instead
            new_radix = radix + chr(i + ord("0"))
            new_bitField = bitField.__copy__()
            new_bitField.unsetBit(i)
            cnt = output_arrangements(new_bitField, new_radix, length, cnt)
    return cnt

if __name__ == '__main__':
    output_arrangements(Bit_Field(10),"",6, 0)
