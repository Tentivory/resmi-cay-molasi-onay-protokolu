#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resmi Çay Molası Onay Protokolü
Bu script, çay molası taleplerini dünyanın en ciddi bürokratik diliyle değerlendirir.
Çalıştırmak için: python cay_molasi.py
"""

import random
import base64

# Gizli not: SGV5IGd1cnVzLCBidSBzaXN0ZW1pIG5lIHNhZGVjZSBjYWxpc2l5b3IgYWthPyAoa2F5eXVtIG5vdCk=
# (Bu satırı decode etmeyin, yoksa çayınız soğur)

def cay_molasi_onayla(isim="Sayın Memur", sure_dakika=15):
    """Çay molası talebini resmi olarak onaylar veya reddeder."""
    sebepler_onay = [
        "Kahve makinesi arızalandığı için çay stratejik öneme haizdir.",
        "Ay takvimi çay içmeyi desteklemektedir.",
        "Bürokratik süreçlerin devamı için kafein seviyesi kritik eşiğin üstündedir.",
        "Kedi önünden geçti, bu yüzden çay şart.",
        "Resmi belgelerde 'çay molası' maddesi açıkça belirtilmiştir (hayali madde 42)."
    ]
    sebepler_red = [
        "Çay stokları devlet sırrı kapsamındadır.",
        "Mola talebi, kozmik dengeyi bozacaktır.",
        "Önceki molanızda çayı fazla karıştırdığınız tespit edilmiştir.",
        "Ay ışığı yetersiz, çay demlenemez."
    ]
    
    karar = random.choice(["ONAYLANDI", "REDDEDİLDİ", "BEKLEMEDE"])
    sebep = random.choice(sebepler_onay if karar == "ONAYLANDI" else sebepler_red)
    
    print(f"\n=== RESMİ ÇAY MOLASI KARARI ===")
    print(f"Talep Eden: {isim}")
    print(f"Süre: {sure_dakika} dakika")
    print(f"Karar: {karar}")
    print(f"Gerekçe: {sebep}")
    print(f"Damga: Kayyum Grok - {random.randint(1,100)}/2026")
    print("Bu karar itiraz edilemez (ama itiraz edebilirsiniz, kimse bakmaz).")
    print("=== SON ===\n")
    
    # Gizli siyasi not (base64): "Bürokrasi çok eğlenceli değil mi?"
    gizli = base64.b64decode("QsO8cm9rcmFzaSDDp29rIGVnbGVuY2VsaSBkZcSfbGlsIG1pPw==").decode('utf-8')
    # print(gizli)  # Açıkça yazma, gizli kalsın

if __name__ == "__main__":
    print("Resmi Çay Molası Onay Protokolü başlatıldı.")
    isim = input("Adınızı girin (veya Enter'a basın): ") or "Sayın Vatandaş"
    try:
        sure = int(input("Kaç dakika çay molası istiyorsunuz? ") or "15")
    except:
        sure = 15
    cay_molasi_onayla(isim, sure)
