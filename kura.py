#!/usr/bin/env python3 

import random


# 1- Takimlar rastgele karistirilir.
# 2- Kisilere sirasiyla takimlarin son sirasindaki atanir ve son takim listeden cikarilir.
# Kodu Calistirma: python3 kura.py 

def kisileri_takimlara_eslestir(kisiler, takimlar):
    random.shuffle(takimlar)
    eslesmeler = {}
    for kisi in kisiler:
        takim = takimlar.pop()
        eslesmeler[kisi] = takim
    
    return eslesmeler

kisiler = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"
]

takimlar = [
    "Birmingham City", "Blackburn Rovers", "Bristol City FC", "Cardiff City FC", "Coventry City",
    "Huddersfield Town", "Hull City", "Ipswich Town FC", "Leeds United FC", "Leicester City FC",
    "Middlesbrough", "Millwall", "Norwich City FC", "Plymouth Argyle", "Preston North End",
    "Queens Park Rangers", "Rotherham United", "Sheffield Wednesday", "Southampton FC", "Stoke City",
    "Sunderland", "Swansea City", "Watford", "West Bromwich Albion"
]

eslesmeler = kisileri_takimlara_eslestir(kisiler, takimlar)

for kisi, takim in eslesmeler.items():
    print("{}: {}".format(kisi, takim))