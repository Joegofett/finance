import yfinance as yf


Zoom        =  yf.Ticker("ZM")
Tesla       =  yf.Ticker("TSLA")
Roku        =  yf.Ticker("ROKU")
Block       =  yf.Ticker("SQ")
ExactSC     =  yf.Ticker("EXAS")
Crispr      =  yf.Ticker("CRSP")
Teladoc     =  yf.Ticker("TDOC")
Uipath      =  yf.Ticker("PATH")
Coinbase    =  yf.Ticker("COIN")
Twilio      =  yf.Ticker("TWLO")
Intellia    =  yf.Ticker("NTLA")
Unity       =  yf.Ticker("U")
BeamTh      =  yf.Ticker("BEAM")
Shopify     =  yf.Ticker("SHOP")
PagerDuty   =  yf.Ticker("PD")
Ginkgo      =  yf.Ticker("DNA")
Draftkings  =  yf.Ticker("DKNG UW")
Robinhood   =  yf.Ticker("HOOD")
Spotify     =  yf.Ticker("SPOT")
TenxG       =  yf.Ticker("TXG")
TwistBio    =  yf.Ticker("TWST")
Stratasys   =  yf.Ticker("SSYS")
Veracyte    =  yf.Ticker("VCYT")
Nvidia      =  yf.Ticker("NVDA")
Tusimple    =  yf.Ticker("TSP")
PacificBio  =  yf.Ticker("PACB")
Materialise =  yf.Ticker("MTLS")
TwoU        =  yf.Ticker("TWOU")
Cerus       =  yf.Ticker("CERS")
Invitae     =  yf.Ticker("NVTA")
BerkeleyLt  =  yf.Ticker("BLI")
Compugen    =  yf.Ticker("CGEN")
Sealtd      =  yf.Ticker("SE")




# algorthim to create. grab 


TeslatrailingPE = Tesla.info["trailingPE"]
ZoomtrailingPE  = Zoom.info["trailingPE"]
RokutrailingPE  = Roku.info["trailingPE"]
# BlocktrailingPE  = Block.info["trailingPE"] Neg Earn 
# ExactSCtrailingPE  = ExactSC.info["trailingPE"] Neg Earn 
CrisprtrailingPE  = Crispr.info["trailingPE"]
# TeladoctrailingPE  = Teladoc.info["trailingPE"] Neg Earn
# UipathtrailingPE  = Uipath.info["trailingPE"] Neg Earn
CoinbasetrailingPE  = Coinbase.info["trailingPE"]
#TwiliotrailingPE  = Twilio.info["trailingPE"] Neg Earn
#IntelliatrailingPE  = Intellia.info["trailingPE"] Neg Earn
#UnitytrailingPE  = Unity.info["trailingPE"] Neg Earn
#BeamthtrailingPE  = BeamTh.info["trailingPE"] Neg Earn
ShopifytrailingPE  = Shopify.info["trailingPE"]
#PDtrailingPE  = PagerDuty.info["trailingPE"] Neg Earn
#GinkgotrailingPE  = Ginkgo.info["trailingPE"] Neg Earn
#DraftkingstrailingPE  = Draftkings.info["trailingPE"] Neg Earn
#RobinhoodtrailingPE  = Robinhood.info["trailingPE"] Neg Earn
#SpotifytrailingPE  = Spotify.info["trailingPE"] Neg Earn
#TenxgtrailingPE  = TenxG.info["trailingPE"] Neg Earn
#TwistBiotrailingPE  = TwistBio.info["trailingPE"] Neg Earn
#StratasystrailingPE  = Stratasys.info["trailingPE"] Neg Earn
#VeracytetrailingPE  = Veracyte.info["trailingPE"] Neg Earn
NvidiatrailingPE  = Nvidia.info["trailingPE"]
#TuSimpletrailingPE  = Tusimple.info["trailingPE"] Neg Earn 
#PacificBiotrailingPE  = PacificBio.info["trailingPE"] Neg Earn
MaterialisetrailingPE = Materialise.info["trailingPE"]
#TwoUtrailingPE  = TwoU.info["trailingPE"] Neg Earn
#CerustrailingPE  = Cerus.info["trailingPE"] Neg Ear
#InvitaetrailingPE  = Invitae.info["trailingPE"] Neg Earn 
#BerkelylttrailingPE  = BerkeleyLt.info["trailingPE"] Neg Earn
#CompugentrailingPE  = Compugen.info["trailingPE"] Neg Earn 
#SealtdtrailingPE  = Sealtd.info["trailingPE"] Neg Earn




print("Tesla Trailing PE = " + str(TeslatrailingPE))
print("Zoom trailing PE = " + str(ZoomtrailingPE))
print("Roku Trailing PE = " + str(RokutrailingPE))
# print("Blocks Trailing PE = " + BlocktrailingPE) Neg Earn 
# print("Exact Sciences trailing PE = " + ExactSCtrailingPE) Neg Earn
print("Crispr Trailing PE = " + str(CrisprtrailingPE))
# print("Teladoc Trailing PE = "+ TeladoctrailingPE) Neg Earn
#print("UIPath Trailing PE = " + str(UipathtrailingPE)) Neg Earn
print("Coinbase Trailing PE = " + str(CoinbasetrailingPE))
#print("Twilio Trailing PE = " + str(TwiliotrailingPE)) Neg Earn
#print("Intellia Trailing PE = " + str(IntelliatrailingPE)) Neg Earn
#print("Beam theraputics Trailing PE = " + str(BeamthtrailingPE)) Neg Earn
print("Shopify Trailing PE = " + str(ShopifytrailingPE))
#print("Pager Duty Trailing PE = " + str(PDtrailingPE)) Neg Earn
#print("Ginkgo Trailing PE = " + str(GinkgotrailingPE) Neg Earn
#print("Spotify Trailing PE = " + str(SpotifytrailingPE)) Neg Earn
print("Nvidia Trailing PE = " + str(NvidiatrailingPE))
print("materialise Trailing PE = " + str(MaterialisetrailingPE))

