from lxml import html
import requests

def getAcaoCNPJ(dictionary, tickers):
  for ticker in tickers:
    # Search the HTML from desired page
    page = requests.get('https://statusinvest.com.br/acoes/' + ticker)

    # Get the HTML Tree of Content
    tree = html.fromstring(page.content)

    # Find the Content by the xPath, appending the '/text()' to get its Text
    # //*[@id="company-section"]/div[1]/div/div[1]/div[2]/h4/small
    cnpj_value = tree.xpath('//*[@id="company-section"]/div[1]/div/div[1]/div[2]/h4/small/text()')
    name_value = tree.xpath('//*[@id="company-section"]/div[1]/div/div[1]/div[2]/h4/span/text()')

    # Print the Ticker as the Key ans the CNPJ as the Value
    print(ticker, str(cnpj_value) + " - " + str(name_value))

    # Add the pair Ticker and CNPJ in the Dictionary
    dictionary[ticker] = cnpj_value

  # Return the Dictionary at the end of the Iterations
  return dictionary

# Initializes the Dictionary
dicty = {}

# All the Tickers that we need to Scrap the CNPJ
#tickers = ['AESB3', 'TRPL4', 'TAEE11']
tickers = ['TAEE11']

# Invoke que Function to do the job
getAcaoCNPJ(dicty, tickers)

# Print the final result
print(dicty)