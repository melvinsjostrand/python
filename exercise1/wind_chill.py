t = float(input("Enter the air temperature in Celsius: "))
v = float(input("Enter the wind speed in kilometres per hour: "))
t_wc = 13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16


print ("The wind-chill temperature is:",round(t_wc, 2), "°C")