import yfinance as yf




Tesla       =  yf.Ticker("TSLA")
Ford        =  yf.Ticker("F")
GM          =  yf.Ticker("GM")
Toyota      =  yf.Ticker("TM")
Honda       =  yf.Ticker("HMC")
VW          =  yf.Ticker("VWAGY")


fordTrailPE = Ford.info["trailingPE"]
gmTrailPE = GM.info["trailingPE"]
toyotaTrailPE = Toyota.info["trailingPE"]
hondaTrailPE  = Honda.info["trailingPE"]
vwTrailPE     = VW.info["trailingPE"]

TeslatrailingPE = Tesla.info["trailingPE"]



totalNonTeslaPE = fordTrailPE + gmTrailPE + toyotaTrailPE + hondaTrailPE + vwTrailPE

avgPEnonTesla = totalNonTeslaPE / 5

earningsAboveReplacementTesla =  TeslatrailingPE - avgPEnonTesla

print(earningsAboveReplacementTesla)