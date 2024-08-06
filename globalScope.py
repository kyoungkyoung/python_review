enemies = 1 # Global Scope

def increase_enemies():
    global enemies # to modify global scope, you need to write this -> global ~~
    enemies += 2 #modifying global scope is impossible
    print(f"enemies inside function {enemies}") #enemies = 2   //  enemies = 3

increase_enemies()
print(f"enemies outside function {enemies}") #enemies = 1   //  enemies = 3

#Global Constants -> all Uppercase
PI = 3.141592
URL = "https://www.google.com"