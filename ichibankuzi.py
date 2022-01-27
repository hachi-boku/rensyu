import random

print("何回引きますか⁇")
num = int(input())


class Keihin:
    def __init__(self,name,tanka,rank):
        self.name = name
        self.tanka = tanka
        self.rank = rank

    #景品があたったときの表示
    def printname(self):
        print ("単価が",self.tanka,"円の",self.rank,"賞",self.name,"が当たりました！　やったね！")
    


# keihin = Keihin("くりまんじゅう",200,"C賞コースター")

# keihin.printname()
# listA = [Keihin("ちいかわ",3000,"A"),
#         Keihin("ハチワレ",3500,"A"),
#         Keihin("うさぎ",3000,"A"),]
listA = [Keihin("ちいかわ",3000,"A"),
        Keihin("ハチワレ",3500,"A"),
        Keihin("うさぎ",3000,"A"),]

listB = [Keihin("タンブラー",2000,"B"),
        Keihin("さすまたフォーク",700,"B"),
        Keihin("３匹の皿",800,"B")]

listC = [Keihin("鎧さん",100,"C"),
         Keihin("くりまんじゅう",400,"C"),
         Keihin("ハリネズミ",100,"C")]
nedan = 650
total = 0
kosuA = 0
kosuB = 0
kosuC = 0

# print(num*keihin.nedan,"円")
for i in range(num):
    risult01 = random.randrange((100)+1)
    # print(risult)
    if risult01 < 5:
        # print("A賞","ぬいぐるみ", end="")
        risultA = random.randrange(3)
        # print(risultA)
        # if risultA == 0:
        #     print("ちいかわ")
        # elif risultA == 1:SS
        #     print("ハチワレ")
        # else:
        #     print("うさぎ")

        # Keihin = Keihin(listA[risultA],3000,nedan)
        listA[risultA].printname()
        total += listA[risultA].tanka
        kosuA += 1
        # print(listA[risultA])

    elif risult01 < 25:
        # print("B賞","食器", )
        risultB = random.randrange(3)
        # if risultB == 0:
        #     print("タンブラー")
        # elif risultB == 1:
        #     print("さすまたフォーク")
        # else:
        #     print("３匹のおさら")
        # print(listB[risultB])
        listB[risultB].printname()
        total += listB[risultB].tanka
        kosuB += 1
    else:
        # print("C賞","コースター", end="")
        risultC = random.randrange(3)
        # if risultC == 0:
        #     print("ハリネズミ")
        # elif risultC == 1:
        #     print("くりまんじゅう")
        # else:
        #     print("よろいさん")
        # print(listC[risultC])
        listC[risultC].printname()
        total += listC[risultC].tanka
        kosuC += 1

print(num*nedan,"円","のお支払い！！")
print("A賞",kosuA,"個")
print("B賞",kosuB,"個")
print("C賞",kosuC,"個")
print(total,"円分の景品が手に入った！！")
if (total - num*nedan) > 0:
    print(total - num*nedan,"円得した‼")
else:
    print((total - num*nedan)*(-1),"円損した！！")