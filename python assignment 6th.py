first_side=10
second_side=9
perimiter=36
third_side=perimiter-(first_side+second_side)
s=perimiter/2
inside_value=(s*(s-first_side)*(s-second_side)*(s-third_side))
triangle_area=inside_value**0.5
print(triangle_area)
