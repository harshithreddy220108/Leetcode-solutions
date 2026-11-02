class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        rem = 0
        for n in data:
            match rem:
                case 0:
                    match n:
                        case _ if n>>7 == 0b0: rem=0
                        case _ if n >> 5 == 0b110: rem = 1
                        case _ if n >> 4 == 0b1110: rem = 2
                        case _ if n >> 3 == 0b11110: rem = 3
                        case _: return False
                case _:
                    if n>>6!=0b10:
                        return False
                    rem-=1
        return rem==0