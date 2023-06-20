from matplotlib import pyplot as plt
student_performance=["Excellent","Good","Average","Poor"]
student_value=[15,25,12,8]
#plt.figure(figsize=(5,20))

plt.pie(student_value,labels=student_performance,startangle=0,explode=[0.2,0,0,0],shadow=True,colors=["green","blue","yellow","pink"] ,autopct="%2.1f%%")
plt.legend(title="Performance",loc="lower right",fontsize=5)
plt.show()
