from lxml import html
import requests

def getFII_CNPJ(dictionary, tickers):
  for ticker in tickers:
    # Search the HTML from desired page
    page = requests.get('https://statusinvest.com.br/fundos-imobiliarios/' + ticker)

    # Get the HTML Tree of Content
    tree = html.fromstring(page.content)

    # Find the Content by the xPath, appending the '/text()' to get its Text
    cnpj_value = tree.xpath('//*[@id="fund-section"]/div/div/div[2]/div/div[1]/div/div/strong/text()')
    name_value = tree.xpath('//*[@id="fund-section"]/div/div/div[2]/div/div[2]/div/div/div/strong/text()')
    
    # Print the Ticker as the Key ans the CNPJ as the Value
    print(ticker, str(cnpj_value) + " - " + str(name_value))

    # Add the pair Ticker and CNPJ in the Dictionary
    dictionary[ticker] = cnpj_value

  # Return the Dictionary at the end of the Iterations
  return dictionary

# Initializes the Dictionary
dicty = {}

# All the Tickers that we need to Scrap the CNPJ
#tickers = ['ABCP11', 'BARI11', 'BBFI11B', 'BBPO11', 'BCIA11', 'BCRI11', 'BPFF11', 'CPTS11', 'CVBI11', 'DEVA11', 'FAMB11B', 'FVPQ11', 'GGRC11', 'HABT11', 'HCTR11', 'HFOF11', 'IRDM11', 'KISU11', 'KNHY11', 'KNSC11', 'MFII11', 'MXRF11', 'NSLU11', 'OULG11', 'PORD11', 'RBFF11', 'RBRF11', 'RBVA11', 'RECR11', 'RECT11', 'SNFF11', 'SPTW11', 'TAEE11', 'TGAR11', 'TORD11', 'VILG11', 'VINO11', 'VRTA11', 'XPCM11', 'XPPR11']
tickers = ['CTXT11']

# Invoke que Function to do the job
getFII_CNPJ(dicty, tickers)

# Print the final result
print(dicty)