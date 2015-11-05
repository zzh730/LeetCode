tens = {
                0:'Zero',
                1:'One',
                2:'Two',
                3:'Three',
                4:'Four',
                5:'Five',
                6:'Six',
                7:'Seven',
                8:'Eight',
                9:'Nine',
                10:'Ten',
                11:'Eleven',
                12:'Twelve',
                13:'Thirteen',
                14:'Fourteen',
                15:'Fifteen',
                16:'Sixteen',
                17:'Seventeen',
                18:'Eighteen',
                19:'Nineteen',
                20:'Twenty',
                30:'Thirty',
                40:'Forty',
                50:'Fifty',
                60:'Sixty',
                70:'Seventy',
                80:'Eighty',
                90:'Ninety',
                100:'Hundred',
                1000:'Thousand',
                1000000:'Million',
                1000000000:'Billion',
                1000000000000:'Trillion'
        }

class Solution(object):
    def search(self,num, mapping):
        lst = [i for i in mapping.keys()]
        lst.sort()
        for index,i in enumerate(lst[1:]):
            if num < i and num >= lst[index]:
                return mapping[lst[index]] + ' '


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
     
        res = ' '
        if num in tens:
            return tens[num] if num < 100 else 'One '+ tens[num]
        if num >= 1000000000000:
            temp = int(num/1000000000000)
            if temp in tens:
                res += tens[num] + ' ' if num < 100 else 'One '+ tens[num]
            else:
                if temp <= 20:
                    res += self.search(temp,tens)
                elif 20 < temp < 100: 
                    res += self.search(temp,tens) + self.search(temp%10, tens)
                else:
                    res = self.hundred(temp, res) + 'Trillion '
            res += self.search(num,tens)   
            num = num % 1000000000000
        if num >= 1000000000:
            temp = int(num/1000000000)
            if temp in tens:
                res += tens[temp]  + ' ' if temp < 100 else 'One '+ tens[temp]
            else:
                if temp <= 20:
                    res += self.search(temp,tens)
                elif 20 < temp < 100: 
                    res += self.search(temp,tens) + self.search(temp%10, tens)
                else:
                    res = self.hundred(temp, res) 
            res += self.search(num,tens)           
            num = num % 1000000000
        if num >= 1000000:
            temp = int(num/1000000)
            if temp in tens:
                res += tens[temp] + ' '  if temp < 100 else 'One '+ tens[temp]
            else:
                if temp <= 20:
                    res += self.search(temp,tens) 
                elif 20 < temp < 100: 
                    res += self.search(temp, tens) + self.search(temp%10,tens)
                else:
                    res = self.hundred(temp,res)
            res += self.search(num,tens)    
            num = num % 1000000 
       
        if num >= 1000:
            temp = int(num/1000)
            if temp in tens:
                res += tens[temp] + ' '  if temp < 100 else 'One '+ tens[temp]
            else:
                if temp <= 20:
                    res += self.search(temp,tens) 
                elif 20 < temp < 100:
                    res += self.search(temp, tens) + self.search(temp%10, tens) 
                else:
                    res = self.hundred(temp,res)
            res += self.search(num,tens)           
            num = num % 1000  
        res = self.hundred(num,res)
        res = res.strip()
        return res

    def hundred(self,num, res):        
        if num > 100:
            temp = int(num/100)
            if temp <= 20:
                res += self.search(temp,tens) + self.search(num,tens) 
            elif 20 < temp < 100:
                res += self.search(temp, tens)+ self.search(temp%10,tens)
            num = num % 100
        if num == 100:
            res += 'One Hundred '
            return res
        if num > 20:
            res += self.search(num,tens) + self.search(num%10,tens) if num not in tens else tens[num]+ ' '
        if 21> num >0:
            res += self.search(num, tens)

        return res



a = Solution()
print( a.numberToWords(790000000))