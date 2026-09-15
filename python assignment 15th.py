shelly_length=22
shelly_breadth=15
shelly_area=shelly_breadth*shelly_length
rachel_length=21
rachel_area=rachel_length**2
print(shelly_area)
print(rachel_area)
if rachel_area>shelly_area:
    difference=rachel_area-shelly_area
    print("rachel_area is bigger:",difference)
else:
    difference=shelly_area-rachel_area
    print("shelly_area is bigger:",difference)    
    