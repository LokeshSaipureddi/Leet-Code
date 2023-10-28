class Solution:
    def intToRoman(self, num: int) -> str:
        ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hunds=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thous=["","M","MM","MMM"]
        return thous[int(num/1000)]+hunds[int((num%1000)/100)]+tens[int((num%100)/10)]+ones[num%10]
        