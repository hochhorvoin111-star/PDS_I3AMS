# Time converter

"""
A video lasts total_seconds = 9875 seconds. Convert it into hours, minutes and seconds 
using only the operators // (floor division) and % (modulo). 
(a) Compute hours, minutes and seconds, then print the sentence shown below. 
(b) Check your answer: rebuild the total from 
the three parts and print whether it equals total_seconds. 
(c) Test your code with 3600, 59 and 86399 seconds. 

"""

total_second = 9875 
hours = total_second//3600
minutes = (total_second%3600)//60
seconds = total_second%60

print(f"\n{total_second} seconds = {hours} h {minutes} min {seconds} s" )


