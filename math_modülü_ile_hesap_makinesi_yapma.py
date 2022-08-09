import math
print("""
1. işlem:toplama
2. işlem:çıkarma
3. işlem:çarpma
4. işlem:bölme
5. işlem:cos alma
6. işlem:sin alma
7. işlem:faktöriyel alma
8. işlem:program sonlandı
 
""")
while True:
    islem=int(input("lütfen bır ıslem secınız"))
    if(islem==1):
        print("toplama işlemi yapılıyor")
        a=int(input("bir sayı giriniz"))
        b=int(input("bir sayı giriniz"))
        print("{} + {} = {}".format(a,b,a+b))
    elif (islem == 2):
        print("çıkarma işlemi yapılıyor")
        a = int(input("bir sayı giriniz"))
        b = int(input("bir sayı giriniz"))
        print("{} - {} = {}".format(a, b, a - b))
    elif (islem == 3):
        print("çarpma işlemi yapılıyor")
        a = int(input("bir sayı giriniz"))
        b = int(input("bir sayı giriniz"))
        print("{} * {} = {}".format(a, b, a * b))
    elif (islem == 4):
        print("bölme işlemi yapılıyor")
        a = int(input("bir sayı giriniz"))
        b = int(input("bir sayı giriniz"))
        print("{} / {} = {}".format(a, b, a / b))
    elif (islem == 5):
        print("cos alma işlemi yapılıyor")
        a = int(input("bir sayı giriniz"))
        print(math.cos(a))

    elif (islem == 6):
        print("sin alma işlemi yapılıyor")
        a = int(input("bir sayı giriniz"))
        print(math.sin(math.radians(a)))
    elif (islem == 7):
        print("faktöriyel alma işlemi yapılıyor")
        a = int(input("bir sayı giriniz"))
        print(math.factorial(a))
        break





