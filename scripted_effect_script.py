#!/bin/python3
# Script to generate the scripted effects boilerplate

template = """
if = {
    limit = { var:logistics_center_level = zzz }
    create_building = { 
        building = $BUILDING$ 
        add_ownership={
            country={
                country = $COUNTRY$
                levels = zzz
            }
        }
        level = zzz
        activate_production_methods = { $METHOD$ } 
        reserves = 1
    }
}
"""

for i in range(20):
	print(template.replace("zzz", str(i+1)))