print("********WELCOME TO WHSMITH********")
def ece():
    flg=0
    item=input("enter item you want to purchase")
    import xlrd
    a=xlrd.open_workbook("EC.xls")
    b=a.sheet_by_index(0)
    for i in range(0,5):
        cb=b.cell_value(i,0)
        if(cb==item):
            flg=1
            val=b.cell_value(i,1)
            amt=int(input("enter amount :\n"))
            if(amt<val):
                import xlwt
                x=xlwt.Workbook("EC.xls")
                y=x.add_sheet("sheet1")
                val=val-amt
                for r in range(0,5):
                    ee=b.cell_value(r,0)
                    y.write(r,0,ee)
                for k in range(0,i):
                    yo=b.cell_value(k,1)
                    y.write(k,1,yo)
                y.write(i,1,val)
                for k in range(i+1,5):
                    yo=b.cell_value(k,1)
                    y.write(k,1,yo)
                x.save("EC.xls")
                print("your order is packed")
            else:
                 print("Sorry ! Out of stock")
    if(flg==0):
        print("not available in our store purchase somewhere else")



def auto():
    flg=0
    item=input("enter automobile you want to purchase")
    import xlrd
    a=xlrd.open_workbook("automobile.xls")
    b=a.sheet_by_index(0)
    for i in range(0,6):
        c=b.cell_value(i,0)
        if(c==item):
            flg=1
            val=b.cell_value(i,1)
            amt=int(input("enter number of vehivles u wanna purchase"))
            if(amt<val):
                import xlwt
                x=xlwt.Workbook("automobile.xls")
                y=x.add_sheet("sa1")
                val=val-amt
                for j in range(0,6):
                    ee=b.cell_value(j,0)
                    y.write(j,0,ee)
                for k in range(0,i):
                    ff=b.cell_value(k,1)
                    y.write(k,1,ff)
                y.write(i,1,val)
                for k in range(i+1,6):
                    ff=b.cell_value(k,1)
                    y.write(k,1,ff)
                x.save("automobile.xls")
                print("your oreder is packed")
            else:
                print("out of stock")
    if(flg==0):
            print("not available purchase somee=where else")


def cloth():
    flg=0
    print("trouser   shirt  belt  \nsocks tie shoes chappal towel")
    item=input("enter clothing you want to purchase")
    import xlrd
    a=xlrd.open_workbook("clothes.xls")
    b=a.sheet_by_index(0)
    for i in range(0,7):
        cc=b.cell_value(i,0)
        if(cc==item):
            flg=1
            val=b.cell_value(i,1)
            amt=int(input("enter number of items u wanna purchase"))
            if(amt<val):
                import xlwt
                x=xlwt.Workbook("clothes.xls")
                y=x.add_sheet("sa1")
                val=val-amt
                for j in range(0,7):
                    ee=b.cell_value(j,0)
                    y.write(j,0,ee)
                for k in range(0,i):
                    ff=b.cell_value(k,1)
                    y.write(k,1,ff)
                y.write(i,1,val)
                for k in range(i+1,7):
                    ff=b.cell_value(k,1)
                    y.write(k,1,ff)
                x.save("clothes.xls")
                print("your oreder is packed")
            else:
                print("out of stock")
    if(flg==0):
            print("not available purchase somee=where else")




def vegi():
    flg=0
    item=input("enter vegitable you want to purchase")
    import xlrd
    a=xlrd.open_workbook("vegitable.xls")
    b=a.sheet_by_index(0)
    for i in range(0,17):
        cz=b.cell_value(i,0)
        if(cz==item):
            flg=1
            val=b.cell_value(i,1)
            amt=int(input("enter quantity in killos of for vegitable u wanna purchase"))
            if(amt<val):
                import xlwt
                x=xlwt.Workbook("vegitable.xls")
                y=x.add_sheet("sa1")
                val=val-amt
                for j in range(0,17):
                    ee=b.cell_value(j,0)
                    y.write(j,0,ee)
                for k in range(0,i):
                    ff=b.cell_value(k,1)
                    y.write(k,1,ff)
                y.write(i,1,val)
                for k in range(i+1,17):
                    ff=b.cell_value(k,1)
                    y.write(k,1,ff)
                x.save("vegitable.xls")
                print("your oreder is packed")
            else:
                print("out of stock")
    if(flg==0):
            print("not available purchase somee=where else")
                        
                
            
print("what do u want to purchase")
sh=int(input("press \n 1 for electronics\n2 forautomobile\n3 for clothes\n 4 for vegitables"))
if(sh==1):
       print("you have choosed electronic section")
       ece()
elif(sh==2):
       print("you have choosed automobile section")
       auto()
elif(sh==3):
       print("you have choosed clothing section")
       cloth()
elif(sh==4):
       print("you have choosed vegitable section")
       vegi()
print("thankyou for visiting WhSMITH")
       
       
       


                    
                
            
