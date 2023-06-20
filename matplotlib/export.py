import pandas as pd
d=pd.read_excel("/home/prabhav/Downloads/newmarks2.xlsx")
df=pd.DataFrame(d)
# df['Total_Marks']=df['hindi'] +df['english'] +df['mathematics']
# df.to_excel("/home/prabhav/Downloads/newmarks.xlsx")
# df.to_excel("/home/prabhav/Downloads/newmarks2.xlsx" , index=False )
# df.to_csv("/home/prabhav/Downloads/newmarks1.csv" , index=True )
# df.to_csv("/home/prabhav/Downloads/newmarks1.txt" , index=False,sep="\t" )

