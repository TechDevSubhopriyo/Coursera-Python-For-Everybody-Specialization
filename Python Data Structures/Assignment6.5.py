text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':');
epos = text.find('5');
num = float(text[pos+1:epos+1].strip());
print(num);