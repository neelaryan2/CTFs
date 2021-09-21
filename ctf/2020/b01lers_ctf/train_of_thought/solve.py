from Levenshtein import distance

s = 'dream dreams fantasticalities a neuropharmacologist neuropharmacy neuroharmacy psychopathologic oneirologic dichlorodiphenyltrichloroethane dichlorodiphenyltrichloroe chlorophenyltrichloroe chloromethanes fluorines cytodifferentiated differentiated'
s = s.split()
for i in range(len(s)-1):
	print(distance(s[i], s[i+1]))
