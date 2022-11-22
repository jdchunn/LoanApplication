
amount = float(input("Enter Loan Amount: "))
score = int(input("Enter Credit Score: "))
status = "Unapproved"
################ DO NOT EDIT ABOVE THIS LINE ########################
if score >= 800:
    status="Approved"
if score < 800 and score >= 700:
    monthlydebt=int(input("Enter monthly debt: "))
    monthlyincome=int(input("Enter monthly income before taxes: "))
    dir = (monthlydebt / monthlyincome) 
    if dir < .50 and score >= 750 or dir < .30 and score >= 700:
        status="Approved"
if score < 700:
    weeklyincome=int(input("Enter weekly income before taxes: "))
    if weeklyincome >= 1000 and score == 650 or weeklyincome >= 750 and score == 600:
        status="Approved"
################ DO NOT EDIT BELOW THIS LINE ########################
print(f'Application Status for ${amount:15.2f}: {status}')