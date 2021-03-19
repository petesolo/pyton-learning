text = "X-DSPAM-Confidence:    0.8475"
sNum = text.find("0")
number = float(text[sNum:])
print(number)
