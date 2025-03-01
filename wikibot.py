import wikipedia

result = wikipedia.summary("Facbook", sentences = 1)

print(result)



def scrape(name = "Microsoft", length =1):
    result2 = wikipedia.summary(name, sentences = length)
    return result2

reply = scrape()

print(reply)