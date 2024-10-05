## Example 1 Of Functions

def Patient(Name,Age,Medical_condition,Test_results):
    print(f'P_Name={Name}')
    print(f'P_Age={Age}')
    print(f'P_Condition={Medical_condition}')
    print(f'P_Results={Test_results}')
    return'--Urgent'
print('---')
print(f'Patient_1{Patient('Alexa',22,'Cancer','Normal')}')
print('---')
print(f'Patient_2{Patient('Siri',44,'Typhoid','Abnormal')}')
print('---')

## Example 2 of Function

def InstagramAccount(id,IdType,Followers_count,Close_friends,Time_spent):
    print(f'InstaId={id}')
    print(f'Type_id ={IdType}')
    print(f'No_Of_Followers = {Followers_count}') 
    print(f'CloseFriends = {Close_friends}')
    print(f'Time_spent_on_Instagram = {Time_spent}')
    
    return{
        'InstaId':id,
        'Type_id':IdType,
        'No_Of_Followers':Followers_count,
        'CloseFriends':Close_friends,
        'Time_spent_on_Instagram':Time_spent
    }
print('---')
id1=InstagramAccount('Bahubali@unofficial','Public','100k',10,'4 Hours')
print('---')
id2=InstagramAccount('Kattapa@official','Private','2k',40,'6 Hours')
print('---')
