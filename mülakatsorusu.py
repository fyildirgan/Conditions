# Uygulama - Mülakat Sorusu

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.
# before: "hi my name is john and i am learning pyhton"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

#len("miuul"): Boyut bilgisine ulaşır.
#range(len("miuul"):Range bize 2 değer arasında sayı üretme imkanı sağlar.
#range(0,5)
#for i in range(len("miull")):
#    print(i)
#print(4 % 2 == 0)
def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
         # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
            # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
        print(new_string)

alternating("miuul")