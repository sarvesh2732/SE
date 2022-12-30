import send

class otpvalidetor:

    def validateotp(self,dic,number,otp):
        if dic[number] == str(otp):
            return 1
        else:
            return 0
