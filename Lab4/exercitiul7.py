"""
Exercitiul 7 - Calcul putere zgomot

Date:
- Puterea semnalului: Psemnal = 90 dB
- Raport semnal-zgomot: SNR = 80 dB

Formula SNR in dB:
SNRdB = 10 * log10(Psemnal / Pzgomot)

Sau echivalent:
SNRdB = PsemnaldB - PzgomotdB

Rezolvare:
PzgomotdB = PsemnaldB - SNRdB
PzgomotdB = 90 - 80
PzgomotdB = 10 dB

Raspuns: Puterea zgomotului este 10 dB
"""

# calcul programatic
Psemnal_dB = 90
SNR_dB = 80

Pzgomot_dB = Psemnal_dB - SNR_dB

print("Exercitiul 7 - Calcul putere zgomot")
print("=" * 40)
print(f"Putere semnal: {Psemnal_dB} dB")
print(f"SNR: {SNR_dB} dB")
print(f"\nFormula: Pzgomot = Psemnal - SNR")
print(f"Pzgomot = {Psemnal_dB} - {SNR_dB}")
print(f"Pzgomot = {Pzgomot_dB} dB")
