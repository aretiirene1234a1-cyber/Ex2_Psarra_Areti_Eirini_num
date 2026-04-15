#Ex2 Number calculation
#Create a function for arithmetic operations
def calc(a,b):
    sum_rslt=a+b
    diff_rslt=a-b
    mult_rslt= a*b
    if b!=0:
        div_rslt= a/b
    else:
        div_rslt=None
    return sum_rslt,diff_rslt,mult_rslt,div_rslt

#Create a function in order to find the maximun value
def maximum(k,l,m,n):
    max_list=[k,l,m,n]
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(max_list)-1): 
            if max_list[i]>max_list[i+1]:
                a=max_list[i+1]
                max_list[i+1]=max_list[i]
                max_list[i]=a
                swapped=True

        
    return max_list[-1]

        
#Ask user if the number is Integer 
question_num=(input("Is the number integer;(Yes or No)"))
if question_num =="Yes" :
    num_1=int(input("Give first integer number"))
    num_2=int(input("Give second integer number"))
    #Call function for integer arithmetic operations 
    sum_rslt, diff_rslt, mult_rslt, div_rslt=calc(num_1,num_2)
    #Print results
    print(f"Sum: {sum_rslt}\nDifference: {diff_rslt}\nMultiplication: {mult_rslt}\nDivision: {div_rslt}")
    #Print integer results in one formatted sentence and round all results to 2 decimals
    print(f"Sum: {sum_rslt:.2f} Difference: {diff_rslt:.2f} Multiplication: {mult_rslt:.2f} Division: {div_rslt:.2f}")
    #Print the largest integer maximun result and round all results to 2 decimals
    print(f"Max: {maximum(sum_rslt, diff_rslt, mult_rslt, div_rslt):.2f}")
if question_num =="No" :  
    num_fl1=float(input("Give first float number"))
    num_fl2=float(input("Give second float number"))
    #Call function for float arithmetic operations 
    sum_rslt_float, diff_rslt_float, mult_rslt_float, div_rslt_float=calc(num_fl1,num_fl2)
    #Print float results in one formatted sentence and round all results to 2 decimals
    print(f"Sum: {sum_rslt_float:.2f} Difference: {diff_rslt_float:.2f} Multiplication: {mult_rslt_float:.2f} Division: {div_rslt_float:.2f}")
    #Print the largest float maximun result and round all results to 2 decimals
    print(f"Max: {maximum(sum_rslt_float, diff_rslt_float, mult_rslt_float, div_rslt_float):.2f}")
