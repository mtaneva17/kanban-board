# Не успяхме да го накараме да работи чрез въвеждане на стойностите от файловете ://
# Ще трябва да се въвеждат собственоръчно при  height = []



import matplotlib.pyplot as plt
  

left = [1, 2, 3, 4, 5, 6, 7]
height = [1000, 2400, 3600, 1000, 2500, 4500, 3200] # Примерни стойности.
  
range = (0, 4000)
tick_label = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  

plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['#8cd1fe', '#000000'])
  

plt.xlabel('Days', fontsize = 12, font = 'Arial')
plt.ylabel('Milliliters', fontsize = 12, font = 'Arial')

plt.title('Amount of water each day:', fontsize = 20, font = 'Arial')


plt.show()