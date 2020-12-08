import hashlib
import time
import pymysql


def make_new_password(which_service_voice_data):
	connection = pymysql.connect("185.224.138.49", "u799736401_for_Athena", "0MechTa8", "u799736401_for_Athena", charset="utf8", cursorclass=pymysql.cursors.DictCursor)
	pierwsze_słowo_w_haśle = bytes("123456789", encoding="utf-8")
	drugie_słowo_w_haśle = "Ograll_Serebroust"
	trzecie_słowo_w_haśle = "Athena"
	główno_słowo_jaki_serwis = str(which_service_voice_data)
	teraz = str("0")
	#time.time()
	pierwszy_poziom_szyfrowania = hashlib.sha512(pierwsze_słowo_w_haśle).hexdigest()
	poziom_między_pierwszym_i_drugim = hashlib.md5(bytes(drugie_słowo_w_haśle, encoding="utf-8")).hexdigest()
	drugi_poziom_szyfrowania = pierwszy_poziom_szyfrowania + poziom_między_pierwszym_i_drugim
	trzeci_poziom_szyfrowania = drugi_poziom_szyfrowania[:-7]
	poziom_między_trzecim_i_czwartym = trzeci_poziom_szyfrowania + trzecie_słowo_w_haśle
	czwarty_poziom_szyfrowania = hashlib.sha512(bytes(poziom_między_trzecim_i_czwartym, encoding="utf-8")).hexdigest()
	poziom_między_czwartym_i_piątym = hashlib.md5(bytes(teraz, encoding="utf-8")).hexdigest()
	piąty_poziom_szyfrowania = czwarty_poziom_szyfrowania + poziom_między_czwartym_i_piątym
	poziom_między_piątym_i_szóstym = piąty_poziom_szyfrowania + główno_słowo_jaki_serwis
	szósty_poziom_szyfrowania = hashlib.sha512(bytes(poziom_między_piątym_i_szóstym, encoding="utf-8")).hexdigest()
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO passwords_memory (password, place) VALUE (%s, %s)"
			cursor.execute(sql, (str(szósty_poziom_szyfrowania), str(which_service_voice_data)))
		connection.commit()
	finally:
		connection.close()
		return szósty_poziom_szyfrowania
