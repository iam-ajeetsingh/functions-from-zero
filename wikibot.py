import wikipedia

result = wikipedia.summary("Facbook", sentences = 1)

print(result)



def scrape(name = "Microsoft", length =1):
    result = wikipedia.summary(name, sentences = length)
    return result

reply = scrape()

print(reply)