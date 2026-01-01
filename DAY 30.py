# DAy 30
#🧪 TASK 1: Number Stream Monitor (System-Level)

Total_entered=0
postive_count=0
nagative_count=0
zero_count=0
sum_positive=0
count_3=0
count_5=0


while True:
    num=int(input("Enter your number here :\n"))
    if num>=999:
        print("SYSTEM OVERRIDE")
        break
 
    if num==-1:
        break

    Total_entered+=1

    if num>0:
        postive_count+=1
        sum_positive+=num
    elif num==0:
        zero_count+=1
    elif num <(-1):
        nagative_count+=1
        
    if num>0 and num%3==0:
        count_3+=1
        
    if num> 0 and num%5==0:
        count_5+=1
        
print("\n--- REPORT ---")
print("Total number enteered ==>",Total_entered)
print("Posive count ==>",postive_count)
print("Zero count ==>",zero_count)
print("Negative count ==>",nagative_count)
print("sun of all positives ==>",sum_positive)
print("count of multipal of 3 ==>",count_3)
print("count of multipal of 5 ==>",count_5)


#🧪 TASK 2: Transaction Validator (Rule-Driven Logic)
total_valid_transactin=0
approved_transaction=0
rejected_transaction=0
approved_amount=0
while True:
    amount=int(input("Enter your amount here : \n"))
    if amount==-1:
        break
    elif amount>50000:
        print("LIMIT EXCEEDED")
        rejected_transaction+=1
    elif amount>0:
        approved_transaction+=1
        approved_amount+=amount
    else:
        rejected_transaction+=1


    total_valid_transactin+=1

print("--- TRANSACTION REPORT ---")
print("total valid transation :",total_valid_transactin)
print("Approved transaction :",approved_transaction)
print("Rejected transactions :",rejected_transaction)
print("Total approved amount :",approved_amount)
    
#🧪 TASK 3: Fraud Pattern Detector (Real-World System Logic)

count_fraud=0
rejected_transaction2=0
total_approvde_amount=0
approved_transaction2=0
total_transation=0
while True:
    number=int(input("Enter number one by one ==> "))
    
    if number==-1:
        break

    total_transation+=1

    if number>100000:
        print("Fraud tranction")
        count_fraud+=1
    elif number<=0:
        print("INVALID Transaction")
        rejected_transaction2+=1
    else:
        print("APPROVED")
        total_approvde_amount+=number
        approved_transaction2+=1

if approved_transaction2>0:
    avg=total_approvde_amount/approved_transaction2
else:
    avg=0
    
print("--- FRAUD REPORT ---")
print("TOtal transation ==>",total_transation)
print("Approved transation ==>",approved_transaction2)
print("Rejected transaction ==>",rejected_transaction2)
print("Fraud transaction ==>",count_fraud)
print("Total appoved amount ==>",total_approvde_amount)    
print("average approved amount ==>",avg)



#🧪 Task 4  Trend Analyzer (Pattern + State Logic)

Increases=0
Decreases=0
no_change=0
spikes =0

prev=None

while True:
    value=int(input("Enter your number here ==>"))
    
    if value==-1:
        break

    if prev is None:
        prev=value
        continue

    if value > prev:
        Increases+=1
    elif value <prev:
        Decreases+=1
    else:
        no_change+=1
    
    if abs(value)>=10:
        spikes+=1

        prev =value

print("--- TREAD REPORT ---")
print("INCREASES ==>",Increases)
print("Decreases ==>",Decreases)
print("NO change ==>",no_change)
print("Spikes ==>",spikes)

#💀🔥 TASK 5 — FINAL BOSS (Day 30)
#🧪 Task 5: System Health Monitor

total_input=0
valid_input=0
invalid_input=0
warning_input=0
spikes2=0

prev=None
current_stable=0
max_stable=0
while True:
    input_n=int(input("Enter your numbers ==>"))
    
    if input_n==-1:
        break
    if input_n>=1000:
        print("critical falure")
        break

    total_input+=1

    if input_n>0:
        valid_input+=1
    elif input_n<=0:
        invalid_input+=1
    elif 500<=input_n<=999:
        warning_input+=1


    if prev is  not None:
        if input_n==prev:
            current_stable+=1
            if current_stable>max_stable:
                max_stable=current_stable
        else:
            current_stable=1

    prev=input_n

print("\n--- SYSTEM HEALTH REPORT ---")
print("Total inputs :", total_input)
print("Valid        :", valid_input)
print("Invalid      :", invalid_input)
print("Warnings     :", warning_input)
print("Spikes       :", spikes2)
print("Max Stable Run:", max_stable)