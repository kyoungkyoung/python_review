# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)


# Modifying Global Scope

enemies = 0

# Bad
'''
def increase_enemies():
    # 함수 안에서 전역변수를 수정하고 싶다면 반드시 global 을 앞에 붙여줘야 함
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

'''

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

# 전역상수는 반드시 대문자로 사용
# 언더바로 표기
PI = 3.141592
GOOGLE_EMAIL = wkjang4@gmail.com

