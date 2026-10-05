import matplotlib.pyplot as plt
x=['python','c','c++','java']
y=[85,70,60,82]
c=["r","g","pink","b"]
plt.title("language priority chart",fontsize=12)
plt.xlabel("language")
plt.ylabel("rating")
plt.barh(x,y,color=c)
plt.legend()
plt.show()
