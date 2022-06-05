# PYTHON

## 1) TÜRLER
--------------------------------------
* Swap
```python
x,y = y,x
```
* İki yazım da aynıdır
```python
x = 100000
x = 100_000
```
* Değer atamak
```python
x,y,z = (1,2,3)         # Birden fazla değişkene değer atamak.

x, _ = (4,7)            # Sadece x'e değer atamak

x, y, *z = (1,2,3,4,5)	# x = 1 , y = 2 , z = [3, 4, 5]
```
* bool
```python
bool(0) ve bool("") hariç tüm değerler True döndürür.
```
* Veri türünü karşılaştırmak
```python
isinstance(i,list)      # i liste mi ?
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 2) STRING
--------------------------------------
* Alfabe
```python
import string
numbers = string.ascii_lowercase
```
* Karakter değiştirmek
```python
kardiz = "feyzi"
print(kardiz.replace("F","f"))  # = Feyzi
```
* Tırnak kullanımı
```python
print('Bugün Mecidiyeköy\'den Fatih\'e gittim.')
```
* Concatenation (Birleştirme)
```python
"feyzi" + " gorcin"     # feyzi gorcin
"feyzi " * 2            # feyzi feyzi
```
* Slicing (Dilimleme)
```python
a = "Feyzi"
print(a[1:])        # eyzi
print(a[1:4])       # eyz
print(a[::-1])      # izyef
```
### Fstring
```python
isim = "Feyzi"
yas = 26

print(f'Onun adı {isim} ve yaşı {yas}\'dir.')
```
### String Fonksiyonlar
#### Kontrol Func
```python
x.isalnum()	    # Harf ve sayı = True	    #,!,% = False
x.isalpha()	    # Harfler True
x.isdigit()	    # Sayılar True  ve isnumeric()
x.isdecimal()	# Decimal True
x.isspace()		# Boşluk True
x.islower()	    # Küçük harfler
x.isupper()	    # Büyük harfler


```
#### Kullanılan Func
```python
x = "Feyzi"

x.strip()           # boşlukları kırpar
x.strip("F")        # = eyzi
x.lstrip("F")       # sadece sol taraftaki F'yi siler

x.lower()           # tamamı küçük harf
x.upper()           # tamamı büyük harf
x.capitalize()      # str'nin ilk harfini büyük yapar
x.title()           # Tüm kelimelerin ilk harfini büyük yapar.
x.swapcase()        # büyükler küçük, küçükler büyük harf olur.
x.zfill(5)          # sol tarafa 5 adet 0 ekler.
x.partition("y")    # Karakter dizisini böler = ('fe', 'y', 'zi')       


```

||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 3) PRINT
--------------------------------------
* Sep ve End
```python
print("Benim","adım","Feyzi",sep=".")   # Benim.adım.Feyzi (Örnek olarak araya boşluk koyarak çıktıyı tek satırda yazdırabilirsin.)

print("Benim","adım","Feyzi",end=".")   # Benim adım Feyzi.
```
* Çıplak olarak ekrana yazdırmak
```python
a = [1,2,3,4,5]
print(*a)       	# 1 2 3 4 5

print(*range(1,6))	# 1 2 3 4 5
```
* Format ile Output düzenlemek
```python
print("Value 1= {} Value 2= {}".format(a, b))

# Sıra belirtmek için
print('{1} \n{0} \n{toplam}'.format(a//b,a/b,toplam=a+b))

# Değişken ile:
print("{a} {b}".format(a="feyzi",b="gorcin"))
```
* % ve Format işlemleri
```python
# Boşluk bırakmak
print("|%10s|" %"feyzi")            # |     feyzi|
print("|%-10s|" %"feyzi")     		# |feyzi     |
print("|{:>10}|".format("feyzi"))   # |     feyzi|
print("|{:<10}|".format("feyzi"))	# |feyzi     |   
print("|{:10s}|".format("feyzi"))	# |feyzi     |
print("|{:^11}|".format("feyzi"))   # |   feyzi   |

# sol tarafı 0 ile doldurmak
print("%05d" %23)       # 00023
print("%.5d" %23)       # 00023
print("23".zfill(5))	# 00023

# Boşluk ve sıfır
print("|%10.5d|" %23)   # |     00023|
print("|%010.d|" %23)   # |0000000023|

# float
print("%.2f" %10)       # 10.00

# basamaklara ayırmak
print("{:,}".format(123456))    # 123,456
```
* Center, rjust, rleft
```python
val = "Feyzi"
print(val.center(15,'.'))	# .....Feyzi.....
print(val.rjust(15,'.'))	# ..........Feyzi
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 4) INPUT
--------------------------------------
* Birden fazla input almak
```python
# Tek satırda girmek
x,y,z = input("Enter three value: ").split()

# Her girişten sonra ENTER'a basmak
x,y,z = (int(input()) for _ in range(3))

# Tek değişken, birden fazla input
x = list(map(int, input("Enter multiple values: ").split()))
```
* Girdiğimiz her input bu listeye eklensin.
```python
input_list = []
input_list.append(input())
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 5) LOOPS and CONDITIONS
--------------------------------------
```python
range(0,11,2)       # 0 2 4 6 8 10
range(11,0,-2)	    # 11 9 7 5 3 1
```
```python
if (n<3 or n>20)        # kullanma
if n in range(3,21)     # kullan
```
```python
for i in s:     # s'i yazdırmak için range
    print(i)    # kullanmaya gerek yoktur.
```
* Ternary Condition
```python
a, b = 10, 20

min = a if a < b else b     # ikisi de aynı
min = a < b and a or b

sinif = "A" if rating > 100 else "B" if rating > 50 else "C"
```
* Comprehension (with List)
```python
# Kısa yazım
liste1 = [i for i in range(10) if i%2 == 0]

# Uzun yazım
liste2 = []

for i in range(10):
    if i%2 == 0:
        liste2 += [i]
```
* For loop with else
~~~
for ile listede bir arama yaptık diyelim. Arama sonucunda bir değer bulunmadı. For’u if gibi düşünerek else: “bulunamadı” şeklinde kullanabilirsin.
~~~
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 6) LIST
--------------------------------------
- Listler içsel yapı içerdikleri için non-scalar veri tipidir.
- Listler farklı veri tiplerini içerebilir
- Listler mutable veri tipleridir. Yani elemanlarını güncelleyebiliriz.

### Liste İşlemleri
* Liste oluşturmak
```python
asd = "Feyzi"
# karakter dizisini karakterlere ayırarak liste oluşturur
list(asd)	    # [‘F’,’e’,’y’,'z','i']

# listeyi 0'dan 10'a sayilar ile doldurur.
liste = list(range(10))
```
* liste kopyalamak
```python
liste1 = [1,2,3]

liste2 = liste1
liste3 = liste1[:]      # kopyalarken dilimleme yaptık
liste4 = list(liste1)
liste5 = liste1.copy()

liste1[0] = 10

print(liste1)   # [10, 2, 3]
print(liste2)   # [10, 2, 3]
print(liste3)   # [1, 2, 3]
print(liste4)   # [1, 2, 3]
print(liste5)   # [1, 2, 3]
```
* Eleman eklemek
```python
liste.append(6)         # listenin sonuna 1 eleman ekler
liste.extend([7,8])     # listenin sonuna 1'den fazla eleman ekler
liste.insert(0,15)      # (index 0'a 15 elemanını ekle)
```
* Eleman silmek
```python
liste.pop()         # son elemanı siler. ve bu elemanı tutar.
liste.pop(3) 		# index 3'ü siler.
liste.remove(10) 	# 10 elemanını listeden sil. eleman listede yok ise error verir. Listeden 10 elemanından birden fazla var ise ilk '10' elemanı silinir. Diğerleri listede kalır.
liste.clear() 		# listenin tamamını temizler.
```
* Hızlı bir sorgu yapmak
```python
liste = [1,2,3,4,5]
5 in liste		        # = True
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 7) TUPLE
--------------------------------------
- Farklı veri tiplerini içerebilir
- Listelerden farklı olarak tuple'lar immutabledır. Yani index’lerin değerlerini değiştiremeyiz.
- Değişmeyeceğini bildiğimiz değerleri birarada tutmak için kullanırız.
- Tanımlanırken parantez kullanılır. Kullanmasan da olur.	tuple_x = (1,2,3,4)

* Tekli bir tuple oluşturmak için sonuna virgül koy yoksa str oluşturur.
```python
tuple1 = ("feyzi")	    # string	
tuple2 = "feyzi",		# tuple
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 8) DICTIONARY
--------------------------------------
- Dictionary yapısının elemanlarına erişmek için belirli keyler kullanacağız ve o da bize value'lar verecek.
- Tanımlama : 	{key1:value1 , key2:value2 ...}
- Sözlüklerde referans olarak sadece değiştirilemez tipler kullanılabilir (sayılar, dizeler, çokuzlar). Listeler kullanılamaz.
```python
ogrenciler = {"Deniz": {"not":80, "ogrenci_no":703}, "Ege":{"not":82, "ogrenci_no":408},
"Gizem": {"not":95, "ogrenci_no":690}}

print(ogrenciler["Ege"]["not"])

ogrenciler["Ege"]["not"] = 100 			# Değişiklik yapmak
ogrenciler["Feyzi"] = 444 				# Key eklemek
del ogrenciler["Deniz"] 				# Key silmek
```
* Eleman eklemek
```python
a = {}
key = input("Name: ")
value = input("Num: ")
a[key] = value

VEYA

dictionary = dict([(1,'Feyzi'),(2,'Gorcin')])
```
```
BUNLARA BAK
    • Sadece anahtarı almak için : keys()
    • Sadece değeri almak için : values()
    • Anahtar ve değeri almak için : items()
    • Sözlükten istediğimiz değeri çekmek : get()
    • Değerleri güncellemek : update()
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 9) SET (Kümeler)
--------------------------------------
- Setler indexlenemez, elemanları değiştirilebilir.
- Setin içinde bir elemanı birden çok göremezsiniz.
- Set’ler sıralı değildir
- Tanımlama :	s = set()

```python
asd = "adana ve ankara"
x = set(asd)    # {'v','n','d','a','r','e','k',' '}

# Eleman eklemek
x.add(6)            # set'de append yoktur.
s1.update(s2) 	    # Toplu eleman eklemek

# Eleman silmek
x.remove(5)     # eleman kümede yoksa hata verir
x.discard(5)    # eleman kümede yoksa hata vermez

# Karşılaştırma
s1.difference(s2)   # s1'in hangi elemanları s2'den farklı.
s1-s2 				# s1'in hangi elemanları s2'den farklı.
s1.intersection(s2) # Kesişimdeki elemanlar
s1 & s2 			# Kesişimdeki elemanlar
s1.union(s2) 		# Birleşimdeki elemanlar
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 10) FUNCTIONS
--------------------------------------
### Predefined Func.
```python
# predefined değer 2. parametrede olmalı yoksa hata alırsın.
def func(x,y=5):
    return x*y

x = func(int(input()))
print(x)

#----------------- Example
def f(x, y=True):
	if x%2==0:
		y=False
		return y
	return y
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 11) KULLANILAN FONKSİYONLAR
--------------------------------------
```python
# elemanın kaç adet olduğunu tutar.
x.count(5)

# 5 elemanının hangi index'te olduğunu tutar.
x.index(5)

# listeyi ters çevirir.
liste = [1,2,3,4,5]

print(list(reversed(liste)))    # [5,4,3,2,1]
print(liste[::-1])              # [5,4,3,2,1]

liste.reverse()     # bu şekilde kullanılır
print(liste)                    # [5,4,3,2,1]

# küçükten büyüğe sıralar. 
sorted(liste) 		# listeyi değiştirmez.
liste.sort() 		# listeyi günceller.
liste.sort(reverse = True) # Terste1n sıralar.
```
### SPLIT() : Karakter dizisini default olarak boşluk ile ayırarak liste oluşturur.
```python
asd = "mustafa feyzi gorcin"
asd.split()     # = [‘mustafa’,’feyzi’,’gorcin’]
```
### JOIN() : listenin elemanları arasına belirtilen yapıyı koyup string'e dönüştürür.
```python
s = ["elma","armut","kayısı"]
x = "-".join(s)		# = elma-armut-kayısı	
#\n ile kullan satır sonu için
```
### Operator Functions
```python
import operator

a,b = 20,10

print(operator.add(a,b)) 		# a + b
print(operator.sub(a,b)) 		# a - b
print(operator.mul(a,b)) 		# a * b
print(operator.truediv(a,b)) 	# a / b
print(operator.floordiv(a,b)) 	# a // b
print(operator.pow(a,b)) 		# a ** b
print(operator.pow(a,b,c)) 		# (a ** b) % c
print(operator.mod(a,b)) 		# a % b
print(operator.eq(a,b)) 		# a = b
```
### Round()
Yuvarlama
```python
print(round(2.5))		    # = 2
print(round(3.82,1))		# = 3.8
print(round(5.688,2))	    # = 5.69
print(round(5.689,1))	    # = 5.7
```
### Dynamic
Değer döndüren ifadeler eval() ile, ifade (expression) olmayan, yani değer döndürmeyen komutlar (func. tanımları, döngüler, atamalar vb.) için exec() func. kullanacağız.
```python
# -------------- eval()
eval("2*x+4",{"x":10})		# Değişkenleri dictionary ile verebiliriz.

while(True):		# Hesap makinesi örneği
	işlem = input("Bir işlem yazın: ")
	if işlem.strip().lower()=="dur": break
	print(eval(işlem))

# -------------- exec()
x = 0
exec("x=3.1415")
print(x)			# = 3.1415 değerini döndürür.
```
### Enumerate()
Yazdırıren * veya list kullan.
```python
asd = ["A","B","C","D","E"]
print(*enumerate(asd),sep="\n")

==
(0, 'feyzi')
(1, 'Gorcin')
(2, 'asd')
(3, 'asdsd')
(4, 'adqaf')
```
### ALL and ANY
```python
# all == and operator
print (all([True, True, True, True]))

# any == or operator
print (any([False, True, False, False]))
```
||||||||||||||||||||||||||||||||||||||

--------------------------------------
## 12) KISA YAZIMLAR
--------------------------------------
### LAMBDA değişkenler,dönüş değeri
Tek satırda func oluşturmak

```python
func = lambda x:x*x			# def kare(x):
            	            #   return x * x
print(func(5))
```
Birden fazla parametre var ise:
```python
func = lambda x,y:x*y
print(func(5,6))
```
### MAP (tanımlanan func adı, listenin her elemanı)
Parametre olarak aldığı fonksiyona, parametre olarak aldığı listenin her elemanını sırasıyla parametre olarak gönderir.
```python
kare = lambda x:x*x
sayilar = range(1,10)
x = map(kare,sayilar)
print(list(x))
```
Bu kodu tek satırda da yazabiliriz:
```python
print(list(map(lambda x:x*x,range(1,10))))
```


