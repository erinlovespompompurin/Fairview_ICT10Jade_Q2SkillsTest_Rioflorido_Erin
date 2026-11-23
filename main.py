from pyscript import document, display

    non_metals = {
            "H" :  ("Hydrogen", 1, 1.008),
            "C" :  ("Carbon", 6, 12.011),
            "N" :  ("Nitrogen", 7, 14.007),
            "O" :  ("Oxygen", 8, 15.999),
            "F" :  ("Fluorine", 9, 18.998),
            "P" :  ("Phosphorus", 15, 30.974),
            "S" :  ("Sulfur", 16, 32.06),
            "Cl" : ("Chlorine", 17, 35.45),
            "Se" : ("Selenium", 34, 78.971),
            "Br" : ("Bromine", 35, 79.904),
            "I" :  ("Iodine", 53, 126.90),
            "He" : ("Helium", 2, 4.0026),
            "Ne" : ("Neon", 10, 20.180),
            "Ar" : ("Argon", 18, 39.948),
            "Kr" : ("Krypton", 36, 83.798),
            "Xe"  : ("Xenon", 54, 131.29),
            "Rn" : ("Radon", 86, 222.0)
        }
    
def checkElement(e) :
    document.getElementById("output1").value
    element_Name = 


    var2 = dict.get(element_Name, ("Element not found" , " - " , " - "))
    
    document.getElementById("div_name").innerHTML = f"""
     Symbol: {element_Name}
     Element: {var2[0]}
     Atomic Number: {var2[1]}
     Atomic Mass: {var2[2]}
 """