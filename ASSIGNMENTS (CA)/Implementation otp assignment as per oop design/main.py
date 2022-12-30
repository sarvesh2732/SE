import send


if __name__ == "__main__":
    obj = send.otpSender()
    count = 0
    while True:
        if obj.sendOtp():
            print("you have successfully logged in")
            exit()
        else:
            count += 1
            print("u have entered wrong otp %s times and have left with %s more chances"%(count,3-count))
            if count == 3:
                print("u have entered wrong otp three times so ....")
                exit()




