import pyshorteners

url = input("Enter Here any URL")

s = pyshorteners.Shortener().tinyurl.short(url)

print("Your Shorten Link : " + s)
