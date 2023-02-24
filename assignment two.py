#list of cars available and their prices
cars={'Audi RS7': 110000, 'Range Rover Autobiography': 250000, 'Opel Kadett': 30000, 'Bentley Bentayga': 350000,\
      'Ferrari Roma': 265000, 'BMW M8': 176000, 'Porsche 911': 210000, 'Toyota Highlander': 92000, 'Hyundae i10': 17000,  \
      'Chevrolet Impala': 62000, 'Nissan Patrol': 95000, 'Infinity Q80': 65000, 'Ford Bronco': 87000, 'Mazda CX7':56000, \
      'Lamborghini Urus': 200000, 'Lexus Rx350': 57000, 'Acura Integra': 30080, 'Volkswagen Golf': 34050,'Kia Morning':23300,  
      'Rolls Royce Cullinan': 500000, 'Mercedes S500d':245000, 'Dodge Charger':95000, 'Suzuki Baleno': 44000, 'Honda Accord':55000,  \
      'McLaren P1': 280000, 'Bugatti Chiron': 850000, 'Jeep Wrangler': 76000, 'Tesla Model 3': 190000,'Genesis GV90' :195000, \
      'Mercury Mountaineer': 78000 }
#prompt user to input a car name
carName=input("Enter a car name: ")
#check if car name is available in list of cars available
if carName in cars:
    print('YES, the %s is available' % (carName))
    print('The Price is $',  cars[carName])
else:
    print('NO, Car is not available')
    
#https://github.com/PaaYaw4123/data-structures-/upload/main