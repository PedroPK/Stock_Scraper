from lxml import html
from enum import Enum

import requests

class FII:
  ticker:                       str
  nome:                         str
  cnpj:                         str
  p_pv:                         str
  vp_por_cota:                  str
  segment:                      str
  ultimo_dividendo_real:        str
  ultimo_dividendo_percentual:  str
  proximo_dividend_real:        str
  proximo_dividend_percentual:  str

def loadFII_data(dictionary, tickers):
  for ticker in tickers:
    # Search the HTML from desired page
    page = requests.get('https://statusinvest.com.br/fundos-imobiliarios/' + ticker)

    # Get the HTML Tree of Content
    tree = html.fromstring(page.content)

    # Find the Content by the xPath, appending the '/text()' to get its Text
    cnpj_value                  = tree.xpath('//*[@id="fund-section"]/div/div/div[2]/div/div[1]/div/div/strong/text()')
    name_value                  = tree.xpath('//*[@id="fund-section"]/div/div/div[2]/div/div[2]/div/div/div/strong/text()')
    patrimonialValue_per_share  = tree.xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[1]/div/div[1]/strong/text()')
    price_over_patrimonialValue = tree.xpath('//*[@id="main-2"]/div[2]/div[5]/div/div[2]/div/div[1]/strong/text()')
    segment_anbima              = tree.xpath('//*[@id="fund-section"]/div/div/div[2]/div/div[6]/div/div/strong/text()')
    last_dividend_brl           = tree.xpath('//*[@id="dy-info"]/div/div[1]/strong/text()')
    last_dividend_percentual    = tree.xpath('//*[@id="dy-info"]/div/div[2]/div[1]/div[1]/div/span/text()')
    next_dividend_brl           = tree.xpath('//*[@id="main-2"]/div[2]/div[7]/div[3]/div/div[1]/strong/text()')
    next_dividend_percentual    = tree.xpath('//*[@id="main-2"]/div[2]/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/b/text()')

    # Fill a FII class
    fii = FII()
    fii.ticker                        = str(ticker)
    fii.nome                          = str(name_value)[2:-2]
    fii.cnpj                          = str(cnpj_value)[2:-2]
    fii.vp_por_cota                   = str(patrimonialValue_per_share)[2:-2]
    fii.p_vp                          = str(price_over_patrimonialValue)[2:-2]
    fii.segment                       = str(segment_anbima)[2:-2]
    fii.ultimo_dividendo_real         = 'R$ ' + str(last_dividend_brl)[2:-2]
    fii.ultimo_dividendo_percentual   = str(last_dividend_brl)[2:-2] + '%'
    fii.proximo_dividend_real         = 'R$ ' + str(next_dividend_brl)[2:-2]
    fii.proximo_dividend_percentual   = str(next_dividend_brl)[2:-2] + '%'

    # Print the Ticker as the Key ans the CNPJ as the Value
    ##print(ticker, str(cnpj_value) + " - " + str(name_value))

    # Add the pair Ticker and CNPJ in the Dictionary
    dictionary[ticker] = fii

  # Return the Dictionary at the end of the Iterations
  return dictionary

def print_fii_dictionary(dictionary):
  for fii in dictionary:
    print( fii )
    ##print( dictionary[fii].ticker )
    print( '\t' + 'Nome: \t\t\t\t'                + str(dictionary[fii].nome)) 
    print( '\t' + 'CNPJ: \t\t\t\t'                + str(dictionary[fii].cnpj)) 
    print( '\t' + 'VP por Cota: \t\t\t'           + str(dictionary[fii].vp_por_cota)) 
    print( '\t' + 'P/VP: \t\t\t\t'                + str(dictionary[fii].p_vp)) 
    print( '\t' + 'Segmento: \t\t\t'              + str(dictionary[fii].segment)) 
    print( '\t' + 'último Rendimento (R$): \t'    + str(dictionary[fii].ultimo_dividendo_real)) 
    print( '\t' + 'último Rendimento (%): \t\t'   + str(dictionary[fii].ultimo_dividendo_percentual)) 
    print( '\t' + 'Próximo Rendimento (R$): \t'   + str(dictionary[fii].proximo_dividend_real)) 
    print( '\t' + 'Próximo Rendimento (%): \t'    + str(dictionary[fii].proximo_dividend_percentual)) 
    print( '\n') 

# Initializes the Dictionary
dicty = {}

# All the Tickers that we need to Scrap the CNPJ
tickers = ['AFHI11', 'ARCT11', 'ARRI11', 'BARI11', 'BBPO11', 'BCFF11', 'BCRI11', 'BLMG11', 'BRCO11', 'BRCR11', 'BTAL11', 'BTCR11', 'BTLG11', 'BTRA11', 'CPTS11', 'CVBI11', 'DEVA11', 'FEXC11', 'FLCR11', 'GALG11', 'GGRC11', 'HABT11', 'HCTR11', 'HGLG11', 'HGRU11', 'HSAF11', 'HSML11', 'IRDM11', 'JSRE11', 'KISU11', 'KNCR11', 'KNSC11', 'MALL11', 'MCCI11', 'MFII11', 'MGCR11', 'MXRF11', 'NCHB11', 'PORD11', 'QAGR11', 'RBRF11', 'RBRP11', 'RBRR11', 'RBRY11', 'RBVA11', 'RECR11', 'RECT11', 'RZAK11', 'RZTR11', 'SARE11', 'SDIL11', 'SNCI11', 'SNFF11', 'TGAR11', 'TRXF11', 'URPR11', 'VCJR11', 'VGHF11', 'VGIP11', 'VILG11', 'VINO11', 'VISC11', 'VRTA11', 'VSLH11', 'XPCI11', 'XPIN11', 'XPLG11', 'XPML11', 'XPPR11']
#tickers = ['HABT11', 'PORD11']
#tickers = ['PORD11']

# Invoke que Function to do the job
loadFII_data(dicty, tickers)

# Print the final result
print_fii_dictionary(dicty)
