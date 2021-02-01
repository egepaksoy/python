import json
import os


oyuncus = open('oyuncular.json', 'r')
oyuncular = json.load(oyuncus)


while True:

	kisi = input('Bulmak istediginiz kisinin bir ozelligini girin: ')
	os.system('clear')
	

	def Bul(deger):
		oyuncu = deger.capitalize()
		ret = []
		for player in oyuncular:
			if oyuncu in player['name']:
				ret.append(player)
			elif oyuncu in player['surname']:
				ret.append(player)
			elif oyuncu in player['country']:
				ret.append(player)
		if len(ret) > 0:
			return ret
		return 'undifined'

	def FotoGoster(kart):
		img = cv2.imread(kart["foto"])
		cv2.imshow(kart["name"],img)
		cv2.waitKey(0)

	sonuc = Bul(kisi)
	
	sonucLen = 0

	for s in sonuc:
		sonucLen += 1

	sonucLen-=1
	
	print(str(int(sonucLen)+1) + " kadar futbolcu bulundu")

	komut = input("\nYapmak istediğiniz islemi secin:\n\n1: Futbolcunun adını + soyadını göster\n2: Futbolcunun yaşını göster\n3: Futbolcunun memleketini göster\n4: Futbolcunun fotoğrafını göster\n5: Futbolcunun overall'ini göster\n\n0: Devam\n\n>>")
	komut = int(komut)
	os.system('clear')



	if komut == 1:
		kisi = int(input(str(sonucLen+1) + "'a kadar bir sayı girin (istediğiniz kişinin sırası): "))-1
		print(kisi)
		os.system('clear')
		print(str(sonuc[kisi]['name']+" ")+str(sonuc[kisi]['surname']))


	elif komut == 2:
		kisi = int(input(str(sonucLen+1) + "'a kadar bir sayı girin (istediğiniz kişinin sırası): "))-1
		os.system('clear')
		print(sonuc[kisi]['age'])


	elif komut == 3:
		kisi = int(input(str(sonucLen+1) + "'a kadar bir sayı girin (istediğiniz kişinin sırası): "))-1
		os.system('clear')
		print(sonuc[kisi]['country'])


	elif komut == 4:
		kisi = int(input(str(sonucLen+1) + "'a kadar bir sayı girin (istediğiniz kişinin sırası): "))-1
		os.system('clear')
		os.system('feh ' + sonuc[kisi]['foto'])
		continue


	elif komut == 5:
		kisi = int(input(str(sonucLen+1) + "'e kadar bir sayı girin (istediğiniz kişinin sırası): "))
		kisi-=1
		os.system('clear')
		print(sonuc[kisi]['overall'])


	else:
		continue

	print("\n\n")

