harfKarsiliklari={"A":"023U0","B":"G63F7","C":"A978F","D":"CXO*8","E":"5CV<Y","F":"AKJS2","G":"BM896","H":"PA298","İ":".89G5","J":"IUG98","K":"AS892","L":"A9XCA","M":"ÇY902","N":"SD092","O":"76USX","P":"AS09X","Q":"52ASV","R":"AS65C","S":"LK2093","T":"LALEE","U":"ÇÖZ87","V":"SAXL2","W":"ASXVC","X":"86UHS","Y":"JV892","Z":"*863J",
                  "a":"SAL52","b":"098XS","c":"ŞAS31","d":"XZ509","e":"DŞİ98","f":"BJ547","g":"GLE75","h":"XBC79","i":"85HDÖ","ı":"sxfd2","j":"KAS92","k":"JF074","l":"KQ027","m":"GF732","n":"AK984","o":"KSA98","ğ":"aslk8","p":"XC983","q":"HHD92","r":"CAK78","s":"ALX42","t":"CXM64","u":"52GFS","v":"66787","w":"AÇX97","x":"GDB97","y":"2ÖSAF","z":"HF974"," ":"GDF1Ç",".":"sdx58"}

#şifre oluşturma algoritmasını yaparken harfKarsiliklari diye bir değişken oluşturdum.Her harfe atadığım belirli 5 haneli farklı değerler atadım.
print("sifreleme algoritmasına hosgeldiniz")
sifrelenecekMetin=input("sifrelenecek metni giriniz: ")#metin alındı.

def sifrele( sifrelenecekMetin):#Şifreleme algoritması başlatıldı.
    sifre = ""#üzerine yazılacak
    for item in sifrelenecekMetin:#metin uzerınde harf harf donuyorum
        for item2 in harfKarsiliklari:#harfler ve karsılıgında bulunan sifrelerin tuıtuldugu sozluk uzerınde donuyorum.
            sifre=sifre+harfKarsiliklari[item]#sifrelenecek metnin her harfinin sifre karsılıklarını sıfre uzerine yazıyorum.
            break
    return sifre#en son sıfreyi gerı donduruyorum . Geri donulen yerde sıfre kullanıcıya yazdırılacak.
sifrelenmisMetin=sifrele(sifrelenecekMetin)#sifrele fonksıyonunu burada karsılıyorum.Sifrelenecek olan metini sifre fonksıyonuna gonderıp sifreliyorum
print(sifrelenmisMetin)#sifrelenen metni yazdırıyorum

sifresiCozulecekMetin=""#bos bir degısken tanımı bir islevi yok. hata verdiginden dolayı yazıldı.
def desifreEt(sifresiCozulecekMetin):#desifreEt fonksıyonu ve desifre edilecek olan metnin parametre olarak verilmesi
    sayac=0
    sayac2=5
    str=""
    """Burada harflerin sifre karsılıkları 5er karakterli oldugu icin sayac2 degıskeni kontrol amaclı 5 er 5er artırılacak.
    Ancak sayac degıskeniyle de buyuk sıfrenın uzerınde gezıp 1er 1er toplamda 5 parcaya tanımlanacak sekılde sifre elde edecez.
    Elde edılen bu her parcayı str uzerıne yazacaz. Bu degısken tanımları bunun icin yazıldı."""
    sifreParcalari=[]#parcaları tutmak ıcın bir dızı tanımı yapıldı.
    harfler=list(harfKarsiliklari.keys())#harfKarsılıkları sozlugundeki butun anahtar degerleri yani harfler, harfler listesi icerisine alındı.
    for item in sifresiCozulecekMetin:#Sifreli metin uzerınde donmeye baslıyorum. Karakter karakter item uzerınde gezınıyorum.
        str=str+item#elde edılen her sifreli karakteri str uzerıne yazıyorum.
        sayac+=1#bir sonrakı karakterekarsılık gelsin diye 1 artırıyorum. 5 oldugunda bir harfe karsılık gelen sifre str uzerıne yazılmıs olacak.
        if(sayac==sayac2):#sayac 5in ve katlarının degerınde oldugu zaman birer birer harfleri almısız demektir.
            """ornegın burada sayac 5 ise sayac2 ye esıt oldugu ıcın 1 harf elde etmis oldum. Daha sonra sayac2 nin degerini 10 yapıp sayac in 5 karakter daha gezmesine ızın verip 
            taa ki sayac 10 a esitlenince ikinci harfı str uzerıne yazmayı saglıyorum. Bu sekılde sayac2 5 er 5er, sayac 1er 1er artarak buradakı kntrolu saglıyorum. """
            sifreParcalari.append(str)#elde edilen her 5 lik kısmı şifreParcalarina atıyorum
            str=""#birinci sifre HGFDS olsa ve ikinci sifre YTREW olsa  HGFDS VE HGFDSYTREW seklınde yıgılma olmasın dıye her harf elde edıldıgınde str yi sıfırlıyorum.
            sayac2+=5#sayac in ikinci 5 karaktere yani bir harfe karsılık gelen sifreye kadar kontrol yapması ıcın sayac2 yi 5 arttırıyorum.
    cozulenSifre=""#GGASD,GDTER,KLKJHG, böyle bir kod şifreParçalarının içinde oluştu.
    #artık elımde ayrı ayrı harf sıfrelerınden olusan bir liste var. Burada sıfreleri cozup cozulenSıfre uzerıne yazacaz.
    for item in sifreParcalari:#her sifre parcasında douyoruz.(HGFDS gibi bu bir sifre parcasıdır ve bir harfe karsılık gelıyor olabilir.)
        for item2 in harfler:#harfler uzerınde donuyorum.
            if(harfKarsiliklari[item2]==item):
                """her harfin bir sifre karsılıgı var. Bu harflerin sifre karsılıkları elımdekı sıfrelerın bulundugu dızıdekı elemanlara esıt oldugunda 
                artık ben ılgılı sıfrenın harfını burada alabılırım. Daha once harflere gore sıfreleme yapmıstık. Sımdi de sifrelerden harflere ulasmak ıcın harflerinSifre karsılıklarındakı 
                sifrelerle kendı sıfrelerımı karsılastırıp dogru harfe item2 ile ulasıyorum."""
                cozulenSifre=cozulenSifre+item2#item2 artık benım sifreParcaları listyesindeki sifrelerime karsılık gelen harften olusuyor. Bunları cozulenSıfre uzerıne yazıyorum.
                break#Yıgılma olmasın dıye donguden cıkıyorum. Yoksa EMİR cıkısı icin  EEMEMİEMİR gibi cıkıslr verıyor.

    return cozulenSifre#cozulen sifreyi gerı donuyorum

input("devam etmek ıcın enter a basınız")
sifresiCozulecekMetin=input("Desifre edilecek metni giriniz: ")#Cozulmesı gereken metni burada alıyorum.
desifreEdilmisMetin=desifreEt(sifresiCozulecekMetin)#desifreEt fonksıyonunu burada karsılıyorum ve aldıgım sıfrelenecek metni fonksıyona parametre olarak verıyorum.
print(desifreEdilmisMetin)#geri donen degeri burada yazdırıyorum ve sıfremi elde etmis oluyorum.
input("Programı bitirmek icin enter a basınız")#enter ile programı bıtırıyoruz.






