d={1.32:2.33,3.12:4.00,5.3:10}
with open('output.txt','w') as f:
    for key,value in d.items():
        f.write(str(value)+'	 '+str(key))
        f.write('\n')
f.close()

