import random


class otpGenrater:
    def __init__(self):
        self.numbericOtp = 0
        self.alphaNumericOtp = ""
        self.length = 0
        self.array = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']


class numericOtpGenrater(otpGenrater):

    def genrateFourDigitNumericOtp(self):
            self.numbericOtp = random.randrange(1,8999)
            self.numbericOtp = self.numbericOtp + 1000
            return self.numbericOtp

    def genrateSixDigitNumericOtp(self):
            self.numbericOtp = random.randrange(1,899999)
            self.numbericOtp = self.numbericOtp + 100000
            return self.numbericOtp

    def genrateRandomLengthNumericOtp(self):
            self.length = random.randrange(1,4)
            string = "8999" + ("9" * self.length)
            self.numbericOtp = random.randrange(8998,int(string))
            return self.numbericOtp


class alphaNumericOtpGenrater(otpGenrater):

    def genrateFourDigitAlphaNumericOtp(self):
        self.alphaNumericOtp = ""
        for i in range(4):
            index = random.randrange(0, 36)
            self.alphaNumericOtp = self.alphaNumericOtp + self.array[index]
        return self.alphaNumericOtp

    def genrateSixDigitAlphaNumericOtp(self):
        self.alphaNumericOtp = ""
        for i in range(6):
            index = random.randrange(0, 36)
            self.alphaNumericOtp = self.alphaNumericOtp + self.array[index]
        return self.alphaNumericOtp

    def genrateRandomLengthAlphaNumericOtp(self):
        self.alphaNumericOtp = ""
        self.length = random.randrange(4, 9)
        for i in range(self.length):
            index = random.randrange(0, 35)
            self.alphaNumericOtp = self.alphaNumericOtp + self.array[index]
        return self.alphaNumericOtp














