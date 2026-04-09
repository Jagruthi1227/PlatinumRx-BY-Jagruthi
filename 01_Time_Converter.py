#Given number of minutes, convert it into human readable form.

x=int(input())
hours=x//60 
minutes=x%60
print(str(hours)+" hrs "+str(minutes)+" minutes")
