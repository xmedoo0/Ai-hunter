import requests
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

with open("db.txt","r") as file:
    X_train=file.read().splitlines()
with open("db2.txt","r") as file2:
    y_train=file2.read().splitlines()

vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
model = RandomForestClassifier()
model.fit(X_train_vectors, y_train)
new_subdomain = [sys.argv[1]]  
new_subdomain_vector = vectorizer.transform(new_subdomain)  
prediction = model.predict(new_subdomain_vector)
if prediction[0] == '1':
    print("[+] subdomain takeover here")
else:
    print("[+] subdomain takeover not found")
