#Write a function to convert  USD to INR

amount = int(input("Enter the amount in doller: "))

def rupee_con(curr):
    usd = 80 #one usd means 80 rupees 
    ind_rupee = 80*curr
    print(ind_rupee,"Rupees")

rupee_con(amount)