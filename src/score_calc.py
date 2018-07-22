import scipy.sparse
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import math
import json
import numpy as np

''' tweets_geo.json'''
the_tweets_geo = [
    " \u2733\ufe0fMILLIE \u2733\ufe0f #A5188528 \u2733\ufe0f\n\ud83d\udd39Shiba Inu\ud83d\udd39AGE 7yrs\n\ud83d\udd39Female (S)\ud83d\udd39ARRIVED:6/11\n\ud83d\udc96 AVAILABLE:6/11\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 2\u2026",
    "#LA #JonathanGold \ud83d\udc94\u2764\ufe0f ",
    " \u2733\ufe0fRUBY \u2733\ufe0f #A5202286 \u2733\ufe0f\n\ud83d\udd39Am. Staffordshire\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female\ud83d\udd39ARRIVED:7/20\n\ud83d\udc96 AVAILABLE:7/24\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38\u2026",
    "Happy Sunday! Hot weather in CA allows few #monarch #monarchbutterfly to hatch sooner. #milkweed\u2026 ",
    "The latest Aromatherapy Tips! ",
    " \u2733\ufe0fSUMMER \u2733\ufe0f #A5201983 \u2733\ufe0f\n\ud83d\udd39St Bernard Smth\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female (S)\ud83d\udd39ARRIVED:7/19\n\ud83d\udc96 AVAILABLE:7/19\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #\u2026",
    " \ud83d\udd35\u201cCrearon una esponja para limpiar los vertidos de petr\u00f3leo en oc\u00e9anos\u201d ",
    "You are lucky \ud83c\udf40",
    " \u2733\ufe0fDANICA \u2733\ufe0f #A5202016 \u2733\ufe0f\n\ud83d\udd39Unknown\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female\ud83d\udd39ARRIVED:7/20\n\ud83d\udc96 AVAILABLE:7/24\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W V\u2026",
    " Like &amp; RT for more sexiness \nDMs open \ud83d\ude08\ud83e\udd11 #camslut #F4M #LA #dating #tinder #casual #nudes #pornhub #pornstar #kik #horny #\u2026",
    " \"Then you wander back in my heart like a bitter song\nAnd we\u2019re never done,\n\u2018Cause I need your love, I need your love\nStole my\u2026",
    "How will sensors be more impactful in different industries? \n\n\n\n#Sensors #Tech #AirPollution #Environment #California",
    "Only time will tell... #EOTW #LA ",
    " @DebAlwaystrump @realDonaldTrump This is San Diego my second home and don't think I'm going back. It use to be such a be\u2026",
    " Only time will tell... #EOTW #LA ",
    "Stud earrings | Vintage Design | 14K Rose Plated ",
    "Check out this informative #mining seminar series on doing business in #Africa with #AfricaGoldInsider - pick a dat\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "REMEMBER:  Another great tweet from 2016",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "Check our amazing but lifters (levantapompis) Colombian style collection. Gives you body curves you need!!! \ud83d\udc49\ud83d\udc49\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "#California Knowing is not enough we must apply! Willing is not enough we must do! -Bruce Lee ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "Los Angeles city view - United States \n\n#Travel #Holiday #Inspiration #SouthernCalifornia #USA #LA #LosAngles\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Way to go #California! The state hit its target for cutting greenhouse gas emissions four years ahead of schedule. ",
    "Getting busy!! Its 2daaaaaaaaaaaa #MH2da #MHpromotions #DJ #life #music #Chicago #hiphop  #la #newyork #fresh #dope\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "0:00\u30d4\u30c3\u30bf\u30ea\u306b\u6295\u7a3f\u3068\u306f\uff01\uff01\uff01",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "If YOU live in the 22nd District of #California and are ASHAMED of #Nunes being YOUR elected US House Rep? \n\nYOU ca\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "\u6df1\u702c\u304f\u3093\u306e\u5408\u6210\u611f\u534a\u7aef\u306a\u304f\u306d\u3001\uff1f",
    " Only time will tell... #EOTW #LA ",
    " WATCH: #US police heli flies circles round 'UFO' in #California sky ",
    " Red Sky at Night\n\nis a Sailors Delight!\n\n\u26f5\ufe0f\n\n#Catalina #California #Weather #Travel #MyDayInLA #Beach ",
    "\u5168\u7403\u6700\u5927\u4ea4\u53cb\u7ea6\u70ae\u5e73\u53f0\u52a0\u5fae\u4fe1mtlove890  #\u65e7\u91d1\u5c71 #\u6e7e\u533a #sanjose #sanfrancisco #\u4e09\u756a #\u5317\u7f8e\u7ea6\u70ae #\u5317\u7f8e\u4ea4\u53cb #\u6d1b\u6749\u77f6 #LA #losangeles #\u7ebd\u7ea6 #\u6cd5\u62c9\u76db #\u6e29\u54e5\u534e #\u8fc8\u963f\u5bc6\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "The #left are #vile #brainless #selfish people that really do wish to let anyone &amp; everyone into America UNVETTED!\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    "\u9060\u8fd1\u6cd5\uff1f\u306a\u304b\u3058\u3093\u304c\u5c0f\u3055\u304f\u898b\u3048\u308b\uff01\uff01",
    " Start your post recovery with @ocpharmcbd products \ud83d\udcaf\u2705 Use code: razor10 for exclusive savings. @razorob @ocpharms #ocpharm #c\u2026",
    " Only time will tell... #EOTW #LA ",
    " Los Angeles city view - United States \n\n#Travel #Holiday #Inspiration #SouthernCalifornia #USA #LA #LosAngles #LoveTravel\u2026",
    "Paramount Ranch: Where Movies are Made ",
    "The latest Visceral Travel! ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Tokyo Guitar Fight\ud83c\uddfa\ud83c\uddf8\ud83c\uddef\ud83c\uddf5\n\n\u6700\u9ad8\u306e\u30a4\u30d9\u30f3\u30c8\u3060\u3063\u305f\u305c\u3297\ufe0f\u3297\ufe0f\n \n\u307f\u3093\u306aLA\u30e1\u30bf\u30eb\u304c\u597d\u304d\u3067\u5b89\u5fc3\u3057\u305f\u3088\n\n\u3061\u306a\u307f\u306b\u4eca\u56de\u306eDokken\u306fLightning Strikes Again\u26a1\ufe0f\n\u76db\u308a\u4e0a\u304c\u3063\u305f\u306a\ud83d\udc95\n\n#TheBlueScrea\u2026",
    " Only time will tell... #EOTW #LA ",
    "Who here #smokes that #Cali #weed?\n\n\n#weed #weedtees #california #potleaf #green #tshirt\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "#feliz #de #la #vida ",
    " WATCH: #US police heli flies circles round 'UFO' in #California sky ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Find the best things to do in Orange County #California for first-time visitors with our 3-day guide compiled by Orang\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "\u5168\u7403\u6700\u5927\u4ea4\u53cb\u7ea6\u70ae\u5e73\u53f0\u52a0\u5fae\u4fe1mtlove890  #\u65e7\u91d1\u5c71 #\u6e7e\u533a #sanjose #sanfrancisco #\u4e09\u756a #\u5317\u7f8e\u7ea6\u70ae #\u5317\u7f8e\u4ea4\u53cb #\u6d1b\u6749\u77f6 #LA #losangeles #\u7ebd\u7ea6 #\u6cd5\u62c9\u76db #\u6e29\u54e5\u534e #\u8fc8\u963f\u5bc6\u2026 ",
    "And I get the impression the Humpback knew exactly what he was doing. \ud83d\ude07",
    " The UK's favourite #California snack is on @Twitter! Follow for #raisin recipes, #healthyeating tips and #foodie fun ",
    " Only time will tell... #EOTW #LA ",
    " \u6df1\u702c\u304f\u3093\u306e\u5408\u6210\u611f\u534a\u7aef\u306a\u304f\u306d\u3001\uff1f ",
    "\n#Alabama #Alaska #Arizona #Arkansas #California #Colorado #Connecticut #Delaware",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " \u2733\ufe0fARCHIE \u2733\ufe0f #A5202327 \u2733\ufe0f\n\ud83d\udd39Rottweiler\ud83d\udd39AGE 5yrs\n\ud83d\udd39Male\ud83d\udd39ARRIVED:7/21\n\ud83d\udc96 AVAILABLE:7/25\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "\u5168\u7403\u6700\u5927\u4ea4\u53cb\u7ea6\u70ae\u5e73\u53f0\u52a0\u5fae\u4fe1mtlove890  #\u65e7\u91d1\u5c71 #\u6e7e\u533a #sanjose #sanfrancisco #\u4e09\u756a #\u5317\u7f8e\u7ea6\u70ae #\u5317\u7f8e\u4ea4\u53cb #\u6d1b\u6749\u77f6 #LA #losangeles #\u7ebd\u7ea6 #\u6cd5\u62c9\u76db #\u6e29\u54e5\u534e #\u8fc8\u963f\u5bc6\u2026 ",
    " \u6df1\u702c\u304f\u3093\u306e\u5408\u6210\u611f\u534a\u7aef\u306a\u304f\u306d\u3001\uff1f ",
    "[DIRECT/ATMO] #La Rochelle indice fond : 26 (O3)",
    "($MRNJ)Relax\u2026the International financial watchdog, Financial Stability Board (FSB) Gives Thumbs up on Crypto! Downl\u2026 ",
    " \u2733\ufe0fSUMMER \u2733\ufe0f #A5201983 \u2733\ufe0f\n\ud83d\udd39St Bernard Smth\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female (S)\ud83d\udd39ARRIVED:7/19\n\ud83d\udc96 AVAILABLE:7/19\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " [N'-40] NCT VLOG #4 Lovely Night\n\n#NCT #NCT127 #LA\n#Nminute #\uc5d4\ubbf8\ub2db ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "//t.co/EugtlJbrV1",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "\u2728 Jungle Cruise \ud83d\udc18 \ud83d\udc2f\ud83c\udf3f\u2764\ufe0f\ud83d\ude00\ud83d\udcab\u2728 #Disney #dlr @disneyland #Disneylandtoday #Disneylandresort #anaheim #california ",
    " Personal del @MetroCDMX  rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Tra\u2026",
    " Only time will tell... #EOTW #LA ",
    "The average rate for a 30 year FHA mortgage in Bakersfield, California is 4.1%, down from 4.12% last week #LA ",
    " @DebAlwaystrump @realDonaldTrump This is San Diego my second home and don't think I'm going back. It use to be such a be\u2026",
    " Only time will tell... #EOTW #LA ",
    " Palmdale, #California @PalmdaleAmp rocked my world! You made my night, hope to see you all next #Summer! \ud83e\udd18\ud83c\udffb\ud83c\udfb8\u2620\ufe0f #SoCal #Pa\u2026",
    "Doris knows that tomatoes go better with fresh Spaniel steaks.\n\n#Tokerware #dinner #yum #foodie #cannabis #NYC #LA\u2026 ",
    " WATCH: #US police heli flies circles round 'UFO' in #California sky ",
    " Cars and trucks, my friends. The next big chapter in #California reducing climate pollution involves transportation . . . how\u2026",
    " Back to @kilowattbeer. I came back for the great beer. And it changes color! #california #beer #Craftbeer ",
    " Adivinemos: \nCon que platita se financia el documental de #SantiagoMaldonado? \nEspero que muestre #La Realidad ---&gt;\n#F\u2026",
    " Only time will tell... #EOTW #LA ",
    "\u306a\u3093\u3066\u66f8\u3044\u3066\u308b\u304b\u5206\u304b\u3089\u306a\u3044\ud83d\ude2d\n\u8ab0\u304b\u6559\u3048\u3066\uff01\uff01",
    " Only time will tell... #EOTW #LA ",
    "\u201cIt\u2019s so amazing.....love.\u201d #love #heart #view #parkbench #fortbragg #mendocino #california #visitcalifornia\u2026 ",
    "\u5168\u7403\u6700\u5927\u4ea4\u53cb\u7ea6\u70ae\u5e73\u53f0\u52a0\u5fae\u4fe1mtlove890  #\u65e7\u91d1\u5c71 #\u6e7e\u533a #sanjose #sanfrancisco #\u4e09\u756a #\u5317\u7f8e\u7ea6\u70ae #\u5317\u7f8e\u4ea4\u53cb #\u6d1b\u6749\u77f6 #LA #losangeles #\u7ebd\u7ea6 #\u6cd5\u62c9\u76db #\u6e29\u54e5\u534e #\u8fc8\u963f\u5bc6\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Personal del Sistema rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Transfere\u2026",
    " Only time will tell... #EOTW #LA ",
    "Cool photo #la",
    " Only time will tell... #EOTW #LA ",
    " If YOU live in the 22nd District of #California and are ASHAMED of #Nunes being YOUR elected US House Rep? \n\nYOU can ch\u2026",
    "#California\n#musicscene\n#live #music\n#acoustic #tour\n#southwest #westcoast #tourdates\n#alternative #rock\n#new\u2026 ",
    "\u201cHe really was the ambassador for our city.\u201d Nancy Silverton on Jonathan Gold #LA #RIP \ud83d\ude1e",
    "@theofficial_ebz #GatorGator #GatorSkin @REALIcePoseidon  #LA #Chicago #Oslo #London #Dallas\n\nCongrats on this song\u2026 ",
    " WATCH: #US police heli flies circles round 'UFO' in #California sky ",
    "#LA we saved the best for last!! The GRAND FINALE of the southernhospitalitydayparty 2018 national tour is coming y\u2026 ",
    "#love #california #newyork #newjersey #power #positivevibes #positivevibes #pool #nails #model #morning #church\u2026 ",
    "#la-wtf Au Zimbabwe, des femmes rangers luttent contre le braconnage ",
    "Rugby World Cup Sevens 2018 SF: USA vs England Vlog 1 ",
    "#California\n#musicscene\n#live #music\n#acoustic #tour\n#southwest #westcoast #tourdates\n#alternative #rock\n#new\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "H O C U S P O C U S\n:\n:\n:\n:\n#GMK #Gmkmovement #battleground #noremorse #chicago #hocuspocus #magic #southside\u2026 ",
    " Pls\ud83d\ude4fdo NOT miss your chance to STOP the evil #DMT\ud83e\udd1b\ud83e\udd1cnow it's the time to speak out forcefully against this ATROCITY\ud83d\ude4fDo som\u2026",
    "Today: clear and will feel like 70 degrees in #LA. Clear throughout the day. ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Ima @Lakers fan for LIFE but y\u2019all niggas getting out of hand with this vandalizing shit... @KingJames is here for the next 3\u2026",
    " Only time will tell... #EOTW #LA ",
    " \u2733\ufe0fARCHIE \u2733\ufe0f #A5202327 \u2733\ufe0f\n\ud83d\udd39Rottweiler\ud83d\udd39AGE 5yrs\n\ud83d\udd39Male\ud83d\udd39ARRIVED:7/21\n\ud83d\udc96 AVAILABLE:7/25\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W\u2026",
    " Only time will tell... #EOTW #LA ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Only time will tell... #EOTW #LA ",
    "\ud83c\uddeb\ud83c\uddf7 France\n\ud83c\udfc1 LA TESTE-DE-BUCH (RACE 1)\n\ud83d\udcc6 22/07/2018 \u23f0 15:10 GMT\n\ud83c\udfc7 EL SIERRO (1)\n\ud83d\udcb0 ODD 4.90\n#LA TESTE-DE-BUCH\n#HorseRacing\n#FreeTips",
    "\u30ab\u30ea\u30d5\u30a9\u30eb\u30cb\u30a2\u306e\u6642\u5dee\u306b\u3064\u3044\u3066\u3064\u3076\u3084\u304fbot\u3067\u3059\uff01\n \u65e5\u672c\u3068\u30ab\u30ea\u30d5\u30a9\u30eb\u30cb\u30a2\u5dde\u306e\u6642\u5dee\u306f-17\u6642\u9593\n\u30b5\u30de\u30fc\u30bf\u30a4\u30e0\u671f\u9593\u4e2d\u306e\u6642\u5dee\u306f-16\u6642\u9593\n \n # #California",
    " #California lawmakers to revive #Trump tax return bill ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Celebratory dinner with my new partners! So excited for this new venture! More meetings in LA tomorrow, but tonight we d\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "Lyft $50 rides Credit with Lyft Coupon Code enter the offer code ZOOT &gt;&gt; Key Route Inn  #california /swing by lucky's/",
    "nice",
    " Democrats Say Meeting With Russia's Putin Is Collusion And #Treason\n",
    " Only time will tell... #EOTW #LA ",
    "\u5de6\u304b\u30892\u756a\u76ee\u306e\u4eba\u304c\u304a\u3061\u3083\u3081\u3059\u304e\u3066\u3057\u3093\u3069\u3044\u3093\u3067\u3059\u304c(\uff3e\u03bd\uff3e)",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    "\ud83c\udf06 \ud83c\uddfa\ud83c\uddf8 Customer Quality Specialist - BEPC, Inc. ( Diamond Bar, CA, USA )  - [ \u27a1 ",
    "@Travaughn13 @rocio_ephotos @Jazmyn_Cray @MOFinancial @Rialisms @BrycePapenbrook @nmanderz @AllyWatson64 @SacAnime\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    "Never going there again!  Smelled soooo bad!",
    " Only time will tell... #EOTW #LA ",
    " Soaking in the California sun\u2600\ufe0f\ud83d\udd76\n#california \n#sun\n#santabarbara \n#\u30d3\u30fc\u30c1\u6700\u9ad8\n#\u4eca\u65e5\u3068\u660e\u65e5\u4e45\u3057\u3076\u308a\u306e\u4f11\u307f\ud83d\ude0e @ Santa Barbara, California htt\u2026",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    " Home to stars, Hollywood! Here we come!\n\n&lt;Location&gt;\n6922 Hollywood Blvd, Los Angeles, CA 90028 \n\n#BT21 #LA #HOLLYWOOD #COMINGSOO\u2026",
    "California dreaming. \nBowie and I having coffee. \u26a1\ufe0f\n#coffee #california #oceanside #lifeisgood #currentsituation\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " @DebAlwaystrump @realDonaldTrump This is San Diego my second home and don't think I'm going back. It use to be such a be\u2026",
    "#aboutlastnight it was #fun #lit . Thank you nogmo_music and @AllahsApprentic for being so #awesome and #fantastic\u2026 ",
    "Preview: Minnesota United vs. Los Angeles FC \u2013 ",
    " Only time will tell... #EOTW #LA ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "\u26a1\ufe0fIs there a new king of LA\u26a1\ufe0f? @MelvinIngram \ud83d\udc51 @LAChargers_AFC #LA #LosAngeles #SundayMorning #BoltUp ",
    " \u2733\ufe0fCHIPPY \u2733\ufe0f #A5199234 \u2733\ufe0f\n\ud83d\udd39Terrier\ud83d\udd39AGE 1yr\n\ud83d\udd39Male\ud83d\udd39ARRIVED:7/11\n\ud83d\udc96 AVAILABLE:7/15\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W Vict\u2026",
    "My City! #LA",
    " Only time will tell... #EOTW #LA ",
    " This is Callie the 9-month-old pug from #California. Isn\u2019t she the cutest?!\n#mydogiscutest ",
    "#texas #houston #dallas #sanantonio #california #cali #arizona #neworleans #louisiana #missouri WE CAN HELP YOU! DM\u2026 ",
    " WATCH: #US police heli flies circles round 'UFO' in #California sky ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Celebratory dinner with my new partners! So excited for this new venture! More meetings in LA tomorrow, but tonight we d\u2026",
    " @ArtsandClouds @JonAntoine #Jonathanantoine #Believe #Tenor #England #debut solo  performance in #USA #California @tocap #fred\u2026",
    "Can you recommend anyone for these 102 #Engineering #jobs in #California? ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " From NYC to LA!! Absolutely cannot believe my life right now! Let's see what happens whilst I'm here! #LA #hollywood ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " St.Ridah - Never Trust ",
    "Bartender - Ilocos in #balaoan #la-union #ilocos-region ",
    "Meanwhile, in #Liberal #ShitHole #SanFrancisco: The Mayor Won\u2019t Stop Public Defecation\n\n",
    "Carter Page is a Russian spy.\n\n#Republican puppet Devin #Nunes bent over backwards to keep this from being made pub\u2026 ",
    "#thug of the day : #LA teeshirt in #SF \ud83d\ude09 \u00e0 San Francisco, California ",
    " Only time will tell... #EOTW #LA ",
    "It's 69F in #LosAngeles with a haze &amp; winds at W 3.36mph #LA ",
    "The Brunson's are no strangers to urban #hunting... This week, Northern #California #muledeer are on the hit list.\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " WATCH: #US police heli flies circles round 'UFO' in #California sky ",
    "PAPA FRANCESCO CONTRO  NEOLIBERISMO #La Civilt\u00e0 Cattolica ",
    "What a beautifully written piece by @ruthreichl especially if you LOVE #LA  and LOVE #LOVE WOW \u2764\ufe0fJonathan Gold: He\u2026 ",
    "Check out our 9 latest #Insurance openings in #California. ",
    "#LongBeach #California Jul 22 07:53 Temperature 73\u00b0F cloudless Wind VRB 6 km/h  Humidity 75% .. ",
    " Only time will tell... #EOTW #LA ",
    "#Sacramento #California Jul 22 07:53 Temperature 64\u00b0F cloudless Wind S 13 km/h  Humidity 75% .. ",
    " Only time will tell... #EOTW #LA ",
    "#Oakland #California Jul 22 07:53 Temperature 62\u00b0F overcast Wind W 17 km/h  Humidity 80% .. ",
    "#Fresno #California Jul 22 07:53 Temperature 78\u00b0F few clouds Wind N 9 km/h  Humidity 30% .. ",
    "#SanDiego #California Jul 22 07:51 Temperature 73\u00b0F few clouds Wind N 9 km/h  Humidity 75% .. ",
    "Pirates of the Caribbean has been temporarily interrupted. #DLR #DCA #Disneyland #California",
    " \u2733\ufe0fJILLIAN \u2733\ufe0f #A5167888 \u2733\ufe0f\n\ud83d\udd39Am. Staffordshire\ud83d\udd39AGE 4yrs\n\ud83d\udd39Female (S)\ud83d\udd39ARRIVED:4/12\n\ud83d\udc96 AVAILABLE:4/16\n\ud83d\udea8RESCUE-ONLY\ud83d\udea8\n\n\ud83d\udd38310-523-9566\u2026",
    "#LosAngeles #California Jul 22 07:53 Temperature 71\u00b0F few clouds Humidity 80% .. ",
    "#Anaheim #California Jul 22 07:53 Temperature 73\u00b0F cloudless Wind VRB 6 km/h  Humidity 75% .. ",
    "#Berkeley #California Jul 22 07:53 Temperature 62\u00b0F overcast Wind W 17 km/h  Humidity 80% .. ",
    "#Bakersfield #California Jul 22 07:54 Temperature 82\u00b0F cloudless Humidity 35% .. ",
    "Check out our 2 latest #Pediatrics openings in #California. ",
    " A incontro annuale su #famiglia anche coppie dello stesso sesso, e #JamesMartin, gesuita pro #lgbt. A tal proposito...\n#\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "#whale #whales #dolphin #dolphins #whalewatching #fish  #ocean #sea #nature #sealife #beachlife #oceanlife\u2026 ",
    "10 Fun Things To Do TODAY in L.A. for July 22, 2018 ",
    " Only time will tell... #EOTW #LA ",
    "#FREE for a limited time from @slscottauthor ~ get your copy of SPARK today!!!",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Only time will tell... #EOTW #LA ",
    "",
    "Did you know: fresh vegetables are healthier for you than those bought from the store? Here are 8 vegetables to gro\u2026 ",
    "\u306a\u3093\u304b\u3053\u306e\u6df1\u702c\u3055\u3093\u3001\u5408\u6210\u611f\u3059\u3054\u3044w",
    " Good news from #California: A comprehensive suite of #climate policies helped the Golden State meet its 2020 target to\u2026",
    " Only time will tell... #EOTW #LA ",
    " #removeDevinNunes #California #Fresno #Tulare #Visalia ",
    " Only time will tell... #EOTW #LA ",
    "@HarleyRouda #CALIFORNIA PLEASE vote for HarleyRouda and put Roherbacher in the unemployment line. #CaliforniaLove",
    "It's Power In the Name JESUS.  Thank you @TPHDenver for supporting Vivian and Stage 4 Carcinoid Cancer. Plz read my\u2026 ",
    " El incendio Ferguson deja 2 bomberos heridos en #California\n",
    " #whale #whales #dolphin #dolphins #whalewatching #fish  #ocean #sea #nature #sealife #beachlife #oceanlife #marinelife\u2026",
    " Do you want to walk on a real life movie set?  Check out Paramount Ranch just outside LA!  ",
    "Summer. \n\u30fc\n#summer #restaurant #sushitomi #iphonephotography #iphonexphotography #snapshot #july2018 #\u590f #iphone\u5199\u771f\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "@Mikepet86794072 @buckamen @kathy_owrey @ReconRandy444 @bcolbert68 @awec98 @MeekChirps @Chiefdodd1 @Beg1Girl\u2026 ",
    "Our new ep w @earlskakel drops on #itunes tomorrow or get it anytime on demand at ",
    " Sun, surf and solitude: a quiet side of LA \n\n#LA #LosAngeles #California #CaliforniaLove ",
    " Only time will tell... #EOTW #LA ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Personal del Sistema rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Transfere\u2026",
    " #NMHfamily Isa Maguire \u201819 &amp; #NMH AC Camryn Crocker meet up at the #Pangos #CreamOfTheCrop tourney in #LA. #FundamentalU\u2026",
    "Can you recommend anyone for these 89 #SupplyChain #jobs in #California? ",
    " Happy weekend!! #actor #actorslife #nevergiveup #newyork #miami #miamibeach #london #losangeles #california \ud83d\ude0e ",
    "#California: Muslim boasted of plans to bomb gay nightclubs, set fires, and give homeless people explosive backpack\u2026 ",
    "#MyBunk #hostel #paloalto #cali #california #hostellife #hostelworld #bayarea #standford #mountainview\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Our new ep w @earlskakel drops on #itunes tomorrow or get it anytime on demand at ",
    "John Muir quotes are the best",
    "#Earthquake (#sismo) M2.4 strikes 27 km NE of #Soledad (#California) 2 min ago. More info: ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " I am in the US in August, looking for #realtime #sessions #cashmeets in #LosAngeles #la #SanDiego #LasVegas #lasvegasstr\u2026",
    "We have 4 #Obgyn #jobs open today in #California. ",
    "Now hiring for 38 #Purchasing #job opportunities in #California. ",
    "#LA dstith76 : Working out with my baby #fatguyworkout ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Our new ep w @earlskakel drops on #itunes tomorrow or get it anytime on demand at ",
    "Curlfest 2018 Royalty \ud83d\udc51 Model: @QueenVisionary \n|\n|\n|\n|\n#curlfest2018 #wwim16 #pursuitofportraits #curls #fuji\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " A juvenile Western #Bluebird (Sialia mexicana) seen in the yard this afternoon. Chihuahua Valley, California. #western\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " #SiliconValley #pennystock $ARYC @CNBC #ARYC is a biotech company @arrayit based in #Sunnyvale #California trading at a\u2026",
    "In #California Independents now outnumber @GOP &amp; they are a third party. \ud83d\ude0bAccording to @newsweek's report, \"Indepen\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " LA\u306eEcho Park\u30678\u670816\u65e5\u301c19\u65e5\u306b\u958b\u50ac\u3055\u308c\u308b\u5730\u5143\u30a2\u30fc\u30c6\u30a3\u30b9\u30c8\u304c\u30e1\u30a4\u30f3\u306e\u7121\u6599\u30b5\u30fc\u30ad\u30c3\u30c8\u30a4\u30d9\u30f3\u30c8\u300cEcho Park Rising\u300d\u306bPerfume\u306e\u540d\u524d\u304c\uff01\n\nPerfume\u304c\u666e\u6bb5\u51fa\u6f14\u3057\u306a\u3044\u3067\u3042\u308d\u3046\u898f\u6a21\u611f\u3060\u3057\u3001\nLA\u306b\u4f4f\u3093\u3067\u308b\u65e5\u2026",
    " Only time will tell... #EOTW #LA ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Only time will tell... #EOTW #LA ",
    " If you are looking for a sugar daddy RT this so I could notice you, no nudes needed if you want to give a picture by p\u2026",
    "#LA ROCK:Catanzaro Super Pana Summer Princess Mr Frosinone Ascender Reina de Espadas Tio Yako Mr Coconut My Racing\u2026 ",
    " \u2668\ufe0fBrasas del Sur\u2668\ufe0f\nJunt\u00e9monos a despedir estas vacaciones en #La\u00danicaParrillaDeQuilpu\u00e9 para disfrutar de #LaMejorTerrazaD\u2026",
    "Can you recommend anyone for these 14 #FamilyPractice #jobs in #California? ",
    "California has gotten so bad that they have their own Batman in Stockton. \n\n#darkknight #california #liberalism\n\n",
    " Only time will tell... #EOTW #LA ",
    "See a virtual tour of my listing on 121 Bobby Gene Drive #Scott #LA  #realestate ",
    " Our new ep w @earlskakel drops on #itunes tomorrow or get it anytime on demand at ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " A reward offered for information on who shot the arrow at the burro in Southern California's Reche Canyon. ",
    "Gotta give me that shit...",
    "We have 54 #Education #jobs open today in #California. ",
    "Check out our 14 latest #RealEstate openings in #California. ",
    " #la-wtf Au Zimbabwe, des femmes rangers luttent contre le braconnage ",
    " Good news from #California: A comprehensive suite of #climate policies helped the Golden State meet its 2020 target to\u2026",
    " \u2733\ufe0fENZO \u2733\ufe0f #A5201260 \u2733\ufe0f\n\ud83d\udd39Pit Bull\ud83d\udd39AGE 6 months\n\ud83d\udd39Male\ud83d\udd39ARRIVED:7/17\n\ud83d\udc96 AVAILABLE:7/17\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W\u2026",
    " Only time will tell... #EOTW #LA ",
    "Remembering my days of #traveling as a #model. Haven\u2019t been back to #LA or #sanDiego for awhile #memories #SoCal\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " If you are looking for a sugar daddy RT this so I could notice you, no nudes needed if you want to give a picture by p\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Personal del @MetroCDMX  rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Tra\u2026",
    " Only time will tell... #EOTW #LA ",
    "We have 1 #internship #jobs open today in #California. ",
    "#SantaMonica #california ",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    " \u2733\ufe0fJOSHUA \u2733\ufe0f #A4270626 \u2733\ufe0f\n\ud83d\udd39Rottweiler\ud83d\udd39AGE 8yrs\n\ud83d\udd39Male (N)\ud83d\udd39ARRIVED:6/2\n\ud83d\udc96 AVAILABLE:6/2\n\ud83d\udc9fSENIOR \ud83d\udc9f \n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter\u2026",
    " Another life just lost in #California. #POTUS, please end the suffering. #BackfireTrump ",
    " #FreeAhedTamimi , from Oakland, #California.\n#FreeAhed \n#Palestine ",
    "Unbelievable! #SanFrancisco: where stealing is legal! Waste of time to arrest them, cuz thieves won't be prosecuted\u2026 ",
    "#teamhoracitu @Horacitu\n#La academia ",
    "more #art hangs w the homie @nelsongeorge at this incredible exhibit in #LA called beyondthestreetsart.  If ur in t\u2026 ",
    " ",
    " I hope everybody is enjoying #Summer  hot air balloons fly in charming #SanDiego #California every evening #StorageWar\u2026",
    " @Mikepet86794072 @buckamen @kathy_owrey @ReconRandy444 @bcolbert68 @awec98 @MeekChirps @Chiefdodd1 @Beg1Girl @LuanneBlair @\u2026",
    "My aunt/uncle are here from #California Sure fun this AM listening to the girls asking 100 questions about his plan\u2026 ",
    "The #lasermazechallenge at @BelmontParkSD is no joke - you'll need to use your smarts *and* your speedy agility to\u2026 ",
    "#California goals ",
    "#La Louvi\u00e8re-Centrum: Vee in de nabijheid van de sporen. #NMBS",
    " Big congrats to @humbleventures @theHairCutApp! Stoked to see you join the @techstars family. #givefirst #growhumble in #L\u2026",
    " Only time will tell... #EOTW #LA ",
    "the #Left is so concerned about #electionmeddling  #RussiaCollusion , yet they continue to push for non US citizens\u2026 ",
    "We have 371 #FacilitiesMgmt #jobs open today in #California. ",
    " #LA ROCK:Catanzaro Super Pana Summer Princess Mr Frosinone Ascender Reina de Espadas Tio Yako Mr Coconut My Racing Mate\u2026",
    " @rgoodlaw @AshaRangappa_ @charlie_savage @RepAdamSchiff @Isikoff Pay attention California! Do whatever is needed to keep Dev\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Ima @Lakers fan for LIFE but y\u2019all niggas getting out of hand with this vandalizing shit... @KingJames is here for the next 3\u2026",
    " #PICTURED: #Gunman walks out of #LA #TraderJoes in handcuffs and surrounded by hostages at the end of a #terrifying siege\u2026",
    " ***Official audio for \"Keep That Same Energy\" by LABEL!!\n\n\n\n#KTSE #KeepThatSameEnergy #AllorNoth\u2026",
    " Only time will tell... #EOTW #LA ",
    "#throwback #springbreak #westcoast #travelgram #wanderlust #roadtrip #layover #ford #expedition #citylife\u2026 ",
    " UPDATE\u203c\ufe0fBEAUTIFUL *BETHANY* IS SAFE!\ud83d\ude4f\u2764\ufe0f\ud83d\ude0a\ud83d\udc3e\ud83d\udc4f ADOPTED PER FB NOTES! \ud83c\udf8a\ud83c\udf89\ud83c\udf89\ud83c\udf89\ud83c\udf8aTHIS IS WONDERFUL NEWS! SO LA #ACC  #CA THX FOR RTS!\u2026",
    "@GeeGeeAkili #CA22 will vote out @RepDevinNunes in Nov if he isn't in #Prison by then. All #California wants @JanzforCongress !",
    " UPDATE\u203c\ufe0fBEAUTIFUL *BETHANY* IS SAFE!\ud83d\ude4f\u2764\ufe0f\ud83d\ude0a\ud83d\udc3e\ud83d\udc4f ADOPTED PER FB NOTES! \ud83c\udf8a\ud83c\udf89\ud83c\udf89\ud83c\udf89\ud83c\udf8aTHIS IS WONDERFUL NEWS! SO LA #ACC  #CA THX FOR RTS!\u2026",
    "Check out our 8 latest #Legal openings in #California. ",
    "For Fate of SAT Writing Test, Watch California ",
    "Headshots Now! #headshot #headshots #actors #actorheadshots #actor #acting #actorslife #headshotphotographer #LA ",
    " ***Official audio for \"Keep That Same Energy\" by LABEL!!\n\n\n\n#KTSE #KeepThatSameEnergy #AllorNoth\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "Neon vibez\n\n#California #LA ",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    " Only time will tell... #EOTW #LA ",
    "Check out our 32 latest #Physician openings in #California. ",
    " The Museum of Futuresex: \u2018Pornhub Nation\u2019 Lands In LA (The NoPro Review by @JBRylah) \n\n#selfiefact\u2026",
    " .\n\u201cWE GOT NOW &amp; NEXT\u201d \n   by @TheDiirtyOGz \n\n      @KokaneOfficial @BigTrayDeee \n@Kurupt_Gotti @ThaChill @WeazelLoc\u2026",
    "We have 1 #Utilities #jobs open today in #California. ",
    " ***Official audio for \"Keep That Same Energy\" by LABEL!!\n\n\n\n#KTSE #KeepThatSameEnergy #AllorNoth\u2026",
    " Have any of you heard about this? \n\n#MAGA\n#California\n#VoteRED\n#Vote2018\n#VoteRed2018\n#VoteDemsOut ",
    " UPDATE\u203c\ufe0fBEAUTIFUL *BETHANY* IS SAFE!\ud83d\ude4f\u2764\ufe0f\ud83d\ude0a\ud83d\udc3e\ud83d\udc4f ADOPTED PER FB NOTES! \ud83c\udf8a\ud83c\udf89\ud83c\udf89\ud83c\udf89\ud83c\udf8aTHIS IS WONDERFUL NEWS! SO LA #ACC  #CA THX FOR RTS!\u2026",
    " We have 1 #Utilities #jobs open today in #California. ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "@ArtsandClouds @JonAntoine @tocap @TheFantoines @JonAntoineHQ @AussieFantoines @ptimofeyevsky\u2026 ",
    " In #California Independents now outnumber @GOP &amp; they are a third party. \ud83d\ude0bAccording to @newsweek's report, \"Independen\u2026",
    "Alessandro Nardone presenta Il Prede ",
    " Only time will tell... #EOTW #LA ",
    "Woman #killed in #LA Trader Joe's #hostage situation ID'd - Jul 22 @ 11:21 AM ET  ",
    "RIP.  \n#food #LA",
    "We have 10 #Hospitalist #jobs open today in #California. ",
    "Just Another Day of Sun #actors #california #beachday #love #lalaland #dreams #summer #nevergiveup ",
    " Only time will tell... #EOTW #LA ",
    " For Fate of SAT Writing Test, Watch California ",
    "We have 10 #psychiatry #jobs open today in #California. ",
    "Lock him up!! Lock him up!! #LockHimUp #nunes #california",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    " I know I\u2019ll see you again, whether far or soon..\n.\n.\n\ud83c\udf04\ud83d\uddfa\u270c\ud83c\udffe\n\ud83d\udcf8: @kittysteadman \n#roadsideattraction #roadsideattractiontour #n\u2026",
    " #California\n#musicscene\n#live #music\n#acoustic #tour\n#southwest #westcoast #tourdates\n#alternative #rock\n#new #indie #artist\n#s\u2026",
    " WATCH: #US police heli flies circles round 'UFO' in #California sky ",
    " Pink Ocean Sunset and Wild Flowers at Santa Barbara County #California\n\n#Nature #Travel #Photo #Sunset #Traveling #Flowers\u2026",
    "\ud83c\udf49WTRMLNWTR \u274c dj.shErOck*\ud83c\udfa7\n.\n#la #shErOckstheParty #djshErOck #wtrmlnwtr\n\ud83d\udcf7 @LovelyMalliha \ud83d\udcfd @ Equinox Sports Club Lo\u2026 ",
    " Lock him up!! Lock him up!! #LockHimUp #nunes #california ",
    "#Kifferlebuzz //t.co/p4PFvfGIFR On est ce que l'on mange # veggan #macron #tpmp #la vie",
    "Can you recommend anyone for these 35 #EmergencyMedicine #jobs in #California? ",
    " Only time will tell... #EOTW #LA ",
    "Watching the sun rise as we sailed between #LA and #SanFrancisco is one of our favourite family memories. The colou\u2026 ",
    " #La Corruption Syst\u00e9mique \u00e9rig\u00e9e par le plQ  ns appauvrie. \n#DehorsCouillard et les #Lib\u00e9rauxCorrompus #polQc ",
    "Lyft coupon code gets you $50 rides credit Lyft Credit Code: ZOOT &gt;&gt; Motel Inn of San Luis Obispo  #california /4ever developed/",
    " @ArtsandClouds @JonAntoine @tocap @TheFantoines @JonAntoineHQ @AussieFantoines @ptimofeyevsky ",
    " UPDATE\u203c\ufe0fTOFFIE IS SAFE\ud83d\ude0a\ud83d\ude4f7/18 BEST NEWS WOO HOO\ud83c\udf8a\ud83c\udf89\ud83c\udf89\ud83c\udf89\ud83c\udf8a  I'M SO HAPPY FOR THIS PRECIOUS ADORABLE DUMPED PUP! THX FOR RTS\ud83d\ude4fOUT O\u2026",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    "Now hiring for 100 #security #job opportunities in #California. ",
    " A reward offered for information on who shot the arrow at the burro in Southern California's Reche Canyon. ",
    " Only time will tell... #EOTW #LA ",
    " #US #businessman #ElliottBroidy has filed a lawsuit to a #California court in which he accused former #UN special envoy to\u2026",
    "365 Day Project, exploring colors and textures around us.\n\u2022\nShot on Google Pixel 2XL\n\u2022\n32/365\n\u2022\n\u2022\n#teampixel #vsco\u2026 ",
    "\ud83d\ude0d\ud83c\udf89\ud83c\udf1f\ud83d\udc3e\ud83d\udc4f\ud83c\udffcYAY!  Finally SAFE in the arms of RESCUE!  woof\ud83c\udf1f TYSM ALL!\u2764\ufe0f",
    " The Road To Change Tour spent this afternoon with young local activists from Orange County, California. #roadtochange #marc\u2026",
    " Tupac Reincarnated | Kid Looks Just Like Tupac #WestCoast #WestCoastBestCoast #westcoasthiphop #tupac #xxxtentation #twin\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "Check out our 1 latest #Oncology openings in #California. ",
    "The Atrocities of the Chinese Communists in #Tibet. ",
    " Only time will tell... #EOTW #LA ",
    "Nice work you Guys - thanks for the diligent effort to repair what a complete POS did - again.\n\nKarma is coming for\u2026 ",
    "Check out our 6 latest #Anesthesiology openings in #California. ",
    "This is a great one!  California 4 over the #sierranevada #mountains #dashcam #brinno #california #ebbettspass ",
    " Pink Ocean Sunset and Wild Flowers at Santa Barbara County #California\n\n#Nature #Travel #Photo #Sunset #Traveling #Flowers\u2026",
    " #OfficerMichaelCampbell, Feb 19th marked 9 years since Kody was struck down in a #HitandRun. #Cloverdale #California #Ju\u2026",
    "#goodmorning #instagram #tesla #california #taxcredits #limitedsupply #endingsoon  #taxadvisors #financialadvisors\u2026 ",
    " This poor girl looks as if her life has been a struggle...geez Danica, how the hell could no one do anything to help you...\u2026",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    "The Jonathon Gold list for #LA finest #restaurants I refer to it often. ",
    "It\u2019s just a crush. #LA ",
    " Lock him up!! Lock him up!! #LockHimUp #nunes #california ",
    "The latest Hari Kovi! ",
    "Can you recommend anyone for these 4 #InternalMedicine #jobs in #California? ",
    "Got Twitter? \n",
    " A bill in California has been proposed to ban the sale of bibles, and yet the Quran is not affected!?\n\n#MAGA\n#Californ\u2026",
    "Someone created a Wikipedia article about \"MacFarland House (Stanford, California)\". Help expand it! #California ",
    " Only time will tell... #EOTW #LA ",
    "Rooftop - Barcelona\n\n\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\n#photosbyamaryllis - link in bio\n\n#pigeons #barcelona #rooftop #catalonia\u2026 ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " #FreeAhedTamimi , from Oakland, #California.\n#FreeAhed \n#Palestine ",
    "Now hiring for 21 #Pharmaceutical #job opportunities in #California. ",
    "",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Only time will tell... #EOTW #LA ",
    " A bill in California has been proposed to ban the sale of bibles, and yet the Quran is not affected!?\n\n#MAGA\n#Californ\u2026",
    "Happy Birthday to my PiC allysondorsey ! \ud83c\udf89  here\u2019s to another year of adventures \ud83e\udd20\n.\nCool cloudy reflection at Moro\u2026 ",
    " Rooftop - Barcelona\n\n\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\u25aa\n#photosbyamaryllis - link in bio\n\n#pigeons #barcelona #rooftop #catalonia #spain\n#w\u2026",
    "Plz //t.co/QiLdVOhZWn #Anonymous #Occupy ",
    "The #UrgentCare Marketing Daily is out! ",
    " Planning a California Pacific Coast Highway Road Trip from San Francisco to Los Angeles ",
    "We have 85 #BusinessMgmt #jobs open today in #California. ",
    "Our Lyft code gets you 10 free rides Here's the coupon code: ZOOT &gt;&gt; Hotel Mac  #california /SUMMER of Love/",
    " If you are looking for a sugar daddy RT this so I could notice you, no nudes needed if you want to give a picture by p\u2026",
    " Only time will tell... #EOTW #LA ",
    "New song demo, \u201cHarder to Leave.\u201d\n\n#newsong #california #breakdown #chicago #forget #harder #to #leave #than #it\u2026 ",
    "Now hiring for 5 #WebDesign #job opportunities in #California. ",
    " A bill in California has been proposed to ban the sale of bibles, and yet the Quran is not affected!?\n\n#MAGA\n#Californ\u2026",
    " A bill in California has been proposed to ban the sale of bibles, and yet the Quran is not affected!?\n\n#MAGA\n#Californ\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Questions about getting a home loan? Try this: ",
    " Only time will tell... #EOTW #LA ",
    "Ice cream right now #costarey #costarei #costarei #sardegna #sardinia #muravera #miamibeach #usa #merica\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "Now hiring for 31 #HR #job opportunities in #California. ",
    " A bill in California has been proposed to ban the sale of bibles, and yet the Quran is not affected!?\n\n#MAGA\n#Californ\u2026",
    "Now hiring for 337 #Nursing #job opportunities in #California. ",
    "Check out our new article: Fun Matters \u2013 Catalyst West 2018 Live Blog With Jon Acuff ",
    " Only time will tell... #EOTW #LA ",
    "Honestly, it was hard to believe #BalboaIsland is still in #LosAngeles - so peaceful! ",
    " Plz //t.co/QiLdVOhZWn #Anonymous #Occupy ",
    "Diposit d'aigua o de cervesa? steelheadbreweryburlingame #sky #california #beer #craftedbeer #cielo #cel #cervesa\u2026 ",
    " \u2733\ufe0fLUCY \u2733\ufe0f #A5202466 \u2733\ufe0f\n\ud83d\udd39Terrier\ud83d\udd39AGE 7yrs\n\ud83d\udd39Female\ud83d\udd39ARRIVED:7/21\n\ud83d\udc96 AVAILABLE:7/21\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W Vic\u2026",
    "#phototherapy #photooftheday #followme #travel #nofilter #inspiration #photography #lifestyle #sonyCamera #sky\u2026 ",
    "Check out our 448 latest #Automotive openings in #California. ",
    " Check out our new article: Fun Matters \u2013 Catalyst West 2018 Live Blog With Jon Acuff ",
    "#Ecoutez la #WebRadio #radiocapitole #Unique #Music #Info #Actu #M\u00e9dias #Faitsdivers #Justice #Facebook RADIOCAPITO\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "Hitch-Hiker From Hell: Aileen Wuornos (Kindle Edition) ",
    "#socialismIgnorance veers it's ugly, lying head yet again. @Ocasio2018 stated that \u201cunemployment is so low because\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "Raw HipHop Beat Free Download ",
    "Dive deep - Live the dream - own a yacht ",
    " Only time will tell... #EOTW #LA ",
    "Author tells of kidnapping by pirates he\u2019d gone to interview\n\n+1 GoldenBot #CA #California",
    "Visita a la #envasadora de un productor y exportador de #palta en #California\u00a0\u25ba\u00a0",
    " UPDATE\u203c\ufe0f*JORY* IS SAFE!\ud83c\udf8a\ud83c\udf89\ud83c\udf89\ud83c\udf89\ud83c\udf8a RESCUED 7/11\ud83d\ude4f\ud83d\ude0a\u2764\ufe0f\ud83d\udc4f\ud83d\udc4f\ud83d\udc4d I'M SO HAPPY FOR THIS SWEET DEVASTATED SAD BOY! THX FOR RTS! HE'S OUT OF\u2026",
    "Only difference, loads faster!\u262e\ufe0f",
    " My New Single Easy Slay dropping Aug 4,2018 #destinymuzic #artist #singer #rapper #indie #independentartist #rnb #chicago\u2026",
    "#stevesilkhurley #chipe #filepe #sae #chicago #la #vegas #selfie #picoftheday #smile #glow #lasvegas #texas #studio\u2026 ",
    " @ArtsandClouds @JonAntoine @tocap @TheFantoines @JonAntoineHQ @AussieFantoines @ptimofeyevsky ",
    " A bill in California has been proposed to ban the sale of bibles, and yet the Quran is not affected!?\n\n#MAGA\n#Californ\u2026",
    " \u00a1\u00bfDe ac\u00e1 tambi\u00e9n se la llevaron?! \u00a0\ud83d\ude31\u00a0No quedan ni las Panam\u00e1 Light de los posts ajenos que hab\u00edamos publicado.\u00a0\ud83d\ude1f\u00a0\u00bfSe es\u2026",
    " A bill in California has been proposed to ban the sale of bibles, and yet the Quran is not affected!?\n\n#MAGA\n#Californ\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Plz //t.co/QiLdVOhZWn #Anonymous #Occupy ",
    " So excited to team up w/ @missee_uk &amp; become an ambassador\ud83d\udda4if u like my clothes, go to ",
    "@xiskya #miami #NYC #Nicaragua #Mexico #CNNSOTU #SundayRead #California #texas #Cnnsotu #CNNChile #Argentina",
    "1124 DESIGN, INC. - information about company from California you can found there ",
    " Only time will tell... #EOTW #LA ",
    "BiGG Ups to 98.2 The Beat and #djgreenguy for the support &amp; record spins much appreciated.. \ud83d\ude4f\ud83d\ude4f\ud83d\ude4f... #WestCoast\u2026 ",
    "Go on your way to Sportsmen's Lodge! The ride there is free with Lyft app, Use code CRIB #LA // Shine bright and sparkle w/ SparkleDealer //",
    " Let this sink in: An #EnergyStorage project rated at 567MWh of capacity \n\nThe volume translates into +11,000 #ElectricVehi\u2026",
    " Only time will tell... #EOTW #LA ",
    "Wow miren all\u00ed una ballena jorobada tir\u00e1ndose, disfrutando de su ambiente, mostr\u00e1ndose ante los visitantes.!\n\ud83d\udc0b\u2026 ",
    " #California #VoteThemOut\n",
    "\ud83d\ude0d\ud83d\ude0d",
    " \ud83d\ude43\ud83d\ude09\ud83d\ude02\ud83d\udcaa#actor #actorslife #beyourself #neverstopexploring #newyork #miamibeach #miami #losangeles #california ",
    "En 10 d\u00edas gira con tango_jazz_quartet pero antes un buen asado con @gonzalito77, #usa #newyork #california\u2026 ",
    " Only difference, loads faster!\u262e\ufe0f ",
    "I see you Sunday- have a beautiful day!\n\n#sunday #sundayfunday #weekend #fun #happy #relax #family #socal\u2026 ",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    " @tessandtiggs \ud83c\udd98SOS\ud83c\udd98 \nkitty MATRIX #a5190061\nat #BaldwinPark #CA #California\nC A L I F O R N I A ! \nCAT PEOPLE! THIS SWEET\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "Check out our 655 latest #Retail openings in #California. ",
    "Ummm don\u2019t disrespect Quentin rich like that, make his name bigger",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " Only time will tell... #EOTW #LA ",
    " Inland Empire residents: Update on wild burro shot by arrow! Donkeyland is still trying to find the burro. Also, $1,000\u2026",
    "\ud83d\udde3\ufe0f\ud83d\udde3\ufe0f\ud83d\udde3\ufe0f\ud83d\udde3\ufe0f\ud83d\udde3\ufe0f bdot 3-0",
    " \ud83d\ude0d\ud83c\udf89\ud83c\udf1f\ud83d\udc3e\ud83d\udc4f\ud83c\udffcYAY!  Finally SAFE in the arms of RESCUE!  woof\ud83c\udf1f TYSM ALL!\u2764\ufe0f ",
    " White girl shuffle 2X18\n#sos #tswift #LA ",
    "\u53cb\u9054\u304c\u5316\u7ca7\u54c1\u4f1a\u793e\u306e\u300c\u30ec\u30d6\u30ed\u30f3\u300d\u306b\u8ee2\u8077\u3057\u305f\u3089\u3057\u3044\u3002\n\u305d\u308c\u3092\u805e\u3044\u305f\u4ffa\u304c\u300c\u30ec\u30a4\u30ab\u30fc\u30ba\u306b\u79fb\u7c4d\u3057\u305f\u3088\u306d\u300d\u3063\u3066\u8a00\u3063\u305f\u3089\u6642\u304c\u6b62\u307e\u3063\u305f\n#\u30ec\u30d6\u30ed\u30f3\n#king\n#LA\n#Lakers",
    " Personal del Sistema rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Transfere\u2026",
    "You're in  New York the second worst state behind #California #Chicago.... @NYGovCuomo is an idiot fool screwing ta\u2026 ",
    " #LA DocHollywoodM : ABC7 #ReadStory Wells Fargo is getting ready to shell out tens of millions of dollars to customers. Acc\u2026",
    "** DAYS OF WINE AND ROSE' **\nValid #July 22, 2018, in-store only!\nMention this post to get 10% off\n#Hangar1 Rose' F\u2026 ",
    " \u2733\ufe0fDANICA \u2733\ufe0f #A5202016 \u2733\ufe0f\n\ud83d\udd39Unknown\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female\ud83d\udd39ARRIVED:7/20\n\ud83d\udc96 AVAILABLE:7/24\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W V\u2026",
    " A reward offered for information on who shot the arrow at the burro in Southern California's Reche Canyon. ",
    "Free Lyft rides! Ten rides total! $50 credit! Discount Code is: ZOOT &gt;&gt; Hollywood Melrose Hotel  #california /primetime promooffr justified/",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " \u2733\ufe0fSUMMER \u2733\ufe0f #A5201983 \u2733\ufe0f\n\ud83d\udd39St Bernard Smth\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female (S)\ud83d\udd39ARRIVED:7/19\n\ud83d\udc96 AVAILABLE:7/19\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #\u2026",
    "#ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " La Reina de las Reinas! \ud83d\ude0d\ud83d\udc96\ud83d\udc78\ud83d\udc51\ud83d\udc95 @katedelcastillo #LaMejor #La\u00danica #LaReina #LaMas #LaMeraMera #Repost @julioyosoy\n\u2022 \u2022 \u2022 \u2022 \u2022\u2026",
    "Available Now \n#art #ShopMyCloset #philly #Atlanta #newyork #California #Fashionista\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "Let us help you find the best #medicalmarijuana #dispensaries and doctors in #California. #wellness #cannabis ",
    " \u2728\ud83c\udf7ela maison du chocolat\ud83c\udf6b\u2728\n\n\u3044\u308d\u301c\u3093\u306a\u7a2e\u985e\u306e\u30c1\u30e7\u30b3\u30ec\u30fc\u30c8\u3084\u30de\u30ab\u30ed\u30f3\u304c\u3042\u308a\u3001\u30c6\u30f3\u30b7\u30e7\u30f3MAX\ud83d\ude0d\u2763\ufe0f\n\n\u5e97\u54e1\u3055\u3093\u304c\u4f55\u3088\u308a\u3082\u7d20\u6575\u3067\u3057\u305f\ud83d\udc95\n\n#la maison du chocolat\n#chocolate \n#\u30c1\u30e7\u2026",
    " Only time will tell... #EOTW #LA ",
    " #SelfDriving #Autonomous Truck Drives from #California to #Florda without relying on a #Human!!!\n#AI #IoT  #ArtificialI\u2026",
    " @Mikepet86794072 @buckamen @kathy_owrey @ReconRandy444 @bcolbert68 @awec98 @MeekChirps @Chiefdodd1 @Beg1Girl @LuanneBlair @\u2026",
    "This little dude makes me so proud to be his father. Thank you @silvertucker for producing such a blessing.\n.\n.\n.\n.\u2026 ",
    "#LA SENDA DE LOS ELEFANTES (ROBE//t.co/DeYBw7jHru v\u00eda\u2026 ",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    " Only time will tell... #EOTW #LA ",
    " I see you Sunday- have a beautiful day!\n\n#sunday #sundayfunday #weekend #fun #happy #relax #family #socal #losangeles #californi\u2026",
    "#gold #nugget #california ",
    " Scenes from #SouthParkWalkabout @absoluteskinSP   Thanks to all who came out and donated for @LnsTgersandBrs !!! #absol\u2026",
    "I\u2019ve missed you, my whole life.\n\n#california #noir \n#newrelease \n#neon #martini #losangeles #swimmingpool\u2026 ",
    "Long Beach, #CA - Ecotech Refrigeration and HVAC - HVAC Refrigeration Technician - Strong company solid top tier cu\u2026 ",
    " A new law is taking effect in #California -- the California Healthy Youth Act -- which forces children to attend pro-ab\u2026",
    "\u219f Torniamo con un po' di scatti da San Francisco - Lombard Street \u219f\n\u25b8\n\u25b8\n\u25b8\n\u25b8\n\u25b8\n#sanfrancisco #california\u2026 ",
    "avo got you, under my skin \ud83e\udd51 still living my best #avocadotoast life in #la \ud83c\udf7d: ch\u00e8vre \u2022 avo \u2022 mortadella \u2022 purslane\u2026 ",
    "Today's Office! #California #starsalign #tour #onstage #awoh ",
    " Sun, surf and solitude: a quiet side of LA \n\n#LA #LosAngeles #California #CaliforniaLove ",
    " Celebratory dinner with my new partners! So excited for this new venture! More meetings in LA tomorrow, but tonight we d\u2026",
    " Only time will tell... #EOTW #LA ",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    " Only time will tell... #EOTW #LA ",
    " if you don\u2019t respect lebron ATLEAST DONT FUCKN DISRESPECT THE A//t.co/WMUhyrlgK9",
    "All the local things in 93453 (Santa Margarita, CA) ",
    "",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "The land of opportunity. Be the visionary \n#sundayfunday #silenttunezproductions #sundaymorning #sanfrancisco\u2026 ",
    "#california #flattrackracing #flattrackfamily #ventura jackjones11j #happydogracing hanging out with kagetherage28\u2026 ",
    " El incendio Ferguson deja 2 bomberos heridos en #California\n",
    "Another beautiful sunset... one of my favorite things \n\n#california #sunset #night #sky ",
    "CBS 13 News at 10 p.m.He\u00e2\u0080\u0099s a father of two and a local business owner. The latest citizen\u00e2\u0080\u0099s arrest was caught o\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "I'm coming home to them hills them California hills! Coulterville California 5pm 7/22/18 #sunday #rootstomp\u2026 ",
    " #California is suffering today after fatal shooting. #POTUS, stop the bloodshed. #BackfireTrump ",
    " Only time will tell... #EOTW #LA ",
    "Kristina ID: 116088 from #Belarus\n23 y.o. \n\n#boxing #UsykGassiev #ABadDecisionIn4Words\u2026 ",
    " #LA ROCK:Catanzaro Super Pana Summer Princess Mr Frosinone Ascender Reina de Espadas Tio Yako Mr Coconut My Racing Mate\u2026",
    " AMEN! ",
    "#jcl #allaboutlastnight #losangeles #dinnerwithKonstantin #drawing #konstantinkakanias #fun #art #artist #spiritual\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Personal del @MetroCDMX  rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Tra\u2026",
    "\u30d7\u30fc\u30de \u5098\u306e\u30b9\u30b9\u30e1\n",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    " #GuitarHero #music #rhythm #games #harmonix #activision #lead #bass #rhythm #rock #playstation #xbox #wii #mac #ds #phone\u2026",
    " Poche strade fanno sognare tanto quanto quelle della #California  Allora ecco 4 itinerari per sbizzarrirvi a scorrazza\u2026",
    " amazing! ",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    " NO MIRES ATR\u00c1S, AMOR \n#crimen #m\u00fasica #literatura #amor #suspense #thriller #kindleUnlimited #PrimeReading #Mexico #US\u2026",
    "Valley is full of smoke! So just some sound of silence... #soundofsilance #yosemite #california #video #journey\u2026 ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    "New Orleans, #LA - Textron - Sr Welding Engineer - A Sr Welding Eng developsmanages recommends and coordinates the\u2026 ",
    "The best app to calculate the time differences! ",
    " El Presidente @evoespueblo ingresa a Palacio de Gobierno, para cumplir otra jornada de trabajo en este 16 de julio que\u2026",
    "Este d\u00eda tenemos la visita de nuestro hermano #Emanuel desde #California trayendo una palabra de Dios que est\u00e1 reta\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Home to stars, Hollywood! Here we come!\n\n&lt;Location&gt;\n6922 Hollywood Blvd, Los Angeles, CA 90028 \n\n#BT21 #LA #HOLLYWOOD #COMINGSOO\u2026",
    "California Ghost Town Sells For $1.4 Million\n#PictureOfTheDay #photooftheday #Photographychallenge  #California\u2026 ",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    "Can you recommend anyone for these 835 #Healthcare #jobs in #California? ",
    " Only time will tell... #EOTW #LA ",
    " If you are looking for a sugar daddy RT this so I could notice you, no nudes needed if you want to give a picture by p\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    "\n\nVERFASSUNGGEBENDE VERSAMMLUNG IN DEN #USA\n\n#Michigan #Alabama #Arizona #Alaska\u2026 ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Sun, surf and solitude: a quiet side of LA \n\n#LA #LosAngeles #California #CaliforniaLove ",
    "#miami #Peking #LA Its time to invest in Art Contemporary Art Biennale Basel ",
    " .\n           \u201cTHE RAP SHOW\u201d \nFRIDAY- August 24, 2018 - 8pm \n@ShrineLA - in #LosAngeles #CA \n\n\ud83c\udf9f \n\nFo\u2026",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    " Doris knows that tomatoes go better with fresh Spaniel steaks.\n\n#Tokerware #dinner #yum #foodie #cannabis #NYC #LA #NV\u2026",
    "Musically ?? \u09a8\u09be\u0995\u09bf \u0985\u09b6\u09cd\u09b2\u09c0\u09b2\u09a4\u09be?? Cancer of Musically | Dirty #Musical.ly in #Bangladesh 2018 #California...\u2026 ",
    "Cali sushi rolls \ud83d\ude09 \n\n#actor #actorslife #lifestyle #food #eat #sushi #cafe #delicious #california #enjoy @ Koreatown ",
    "One year since Billy Elliot. \n#LightingDesign #LA ",
    "Get up to $50 #Lyft Ride credit using the #Lyft app Use this code, PR99 #California changeable",
    "Digging the gold out of #nevadacity #california \n\n@YOGAMULTIMEDIA #travelphotographer \u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014-\u2026 ",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    "Never happen.\nBut,\nI like the way your mind works.",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "#seo\n#security\n#secret\n#unternehmen\n#fu\u00dfball\n#tourism\n#toys\n#top\n#modern\n#reis\n#reise\n#reisen\n#geld\n#banking\n#banks\u2026 ",
    " @Mikepet86794072 @buckamen @kathy_owrey @ReconRandy444 @bcolbert68 @awec98 @MeekChirps @Chiefdodd1 @Beg1Girl @LuanneBlair @\u2026",
    "Looking for a job in #credit? View open credit and A/R positions here: ",
    "\ud83c\udfbcI prefer to say nothing,\nI got a long way to go, I\u2019m getting further away\ud83c\udfb6 #XO #LA\n\n\ud83d\udcf8: theginocharles @ Solutions\u2026 ",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    " Only time will tell... #EOTW #LA ",
    " About a month prepping and filming in downtown Vallejo and on Mare Island. #vallejo #filmmareisland #solanocounty #bumblebe\u2026",
    " Only time will tell... #EOTW #LA ",
    " RT! #California #Election2018 #WinBlue\n\nSupport Sen. DIANNE FEINSTEIN #CAsen, &amp; @DemsWork4USA\n\ud83d\udc49\n\n#\u2026",
    " Only time will tell... #EOTW #LA ",
    "Assemblywoman Quirk-Silva Reacts to UC Regents Reducing Tuition, Calls for Continued Regent Accountability\u2026 ",
    " It's Taffy of Life is Just a Taffy Pull wearing my #daisydukes with #bikini on top cuz it's a #heatwave ..should I be singing\u2026",
    "S\u00edndrome de cotard zombies en la vida real draw my life ",
    "The religious are falling but the righteous are always rising because our God is the God of righteousness. Welcome\u2026 ",
    " #California #Beachs #Adventure #Travel #underwater #beaches #Tour #Holiday   \ud83c\udf3f",
    "Got my tickets...third row!!",
    " Mood ~ All smiles. \u2728\ud83d\ude0e\u26f5\ufe0f\nMet my editing deadline! We celebrated under sail with great wind, weather &amp; stories.\nWishing yo\u2026",
    " \u00a1\u00bfDe ac\u00e1 tambi\u00e9n se la llevaron?! \u00a0\ud83d\ude31\u00a0No quedan ni las Panam\u00e1 Light de los posts ajenos que hab\u00edamos publicado.\u00a0\ud83d\ude1f\u00a0\u00bfSe es\u2026",
    "Where\u2019s the #TheLogo? #MrClutch #44 #Lakers \ud83d\udc9c\ud83c\udfc0\ud83d\udc9b",
    " Another life was just lost in #California. #POTUS, it's time to do something. #BackfireTrump ",
    " \u2733\ufe0fENZO \u2733\ufe0f #A5201260 \u2733\ufe0f\n\ud83d\udd39Pit Bull\ud83d\udd39AGE 6 months\n\ud83d\udd39Male\ud83d\udd39ARRIVED:7/17\n\ud83d\udc96 AVAILABLE:7/17\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W\u2026",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "#relationships  In slavisticgirl",
    " Sun, surf and solitude: a quiet side of LA \n\n#LA #LosAngeles #California #CaliforniaLove ",
    "SUN 25. Some ______  goods\nelectronic, new\nnew, electronic\n(ANSWER - CLICK LINK)\n",
    " One more person was just killed in #California. #POTUS, it\u2019s your job to take action. #BackfireTrump ",
    " Only time will tell... #EOTW #LA ",
    "I would love to show you my #listing at Tbd Dusty Morgan Loop #Opelousas #LA  #realestate ",
    " California Bans Hemp-Derived CBD Oil\n@GodzWeedz \n\n",
    " I don't do this much, so here is your chance. I went crazy and put SPARK for FREE. But only for a few days. So grab it w\u2026",
    " Happy weekend!! #actor #actorslife #nevergiveup #newyork #miami #miamibeach #london #losangeles #california \ud83d\ude0e ",
    " The Jonathon Gold list for #LA finest #restaurants I refer to it often. ",
    " Omg I can\u2019t wait \ud83d\ude0a to go . I am SOO excited \ud83d\ude06 ",
    "New T-shirt, Hoodie and Tank top coming soon \ud83d\udc4a\ud83c\udffd\ud83e\udd85\ud83c\uddfa\ud83c\uddf8\n.\nUNDETECTED MOTORCLOTHING \u00a9\n.\n.\nTHE BRAND THAT STAYS ON THE ROA\u2026 ",
    "Ready to Invest in the US Rental Property Market 2018/2019? ",
    "NEW POST / JOUR 2 \u00e0 SAN FRANCISCO \ud83c\udf01\n&gt;&gt;&gt; \n\n#travel #blog #newpost #sanfrancisco San Francisco\u2026 ",
    " RT! #California CD7 #Election2018 #KeepItBlue #WinBlue\n\nSupport DR. AMI BERA #CA07,&amp; @DemsWork4USA\n\ud83d\udc49",
    "Family Freedom is yours at The Soba Recovery Center 24 HR Helpline 866 447 5298  ",
    " \"Of Days Gone By\". Check out this excellent photo by @LaurieSearch here: ",
    "It's lit #shortfilm #documentary #montage #SanFrancisco #California ",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    "Come out and rock with $afari Tribe 7.28 @7pm\n\n#BGOD #BENTLEYGANG #NYC #LA #ATLANTA #GEORGIA #Recordlabel #hiphop\u2026 ",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " Only time will tell... #EOTW #LA ",
    " \n\nVERFASSUNGGEBENDE VERSAMMLUNG IN DEN #USA\n\n#Michigan #Alabama #Arizona #Alaska #California #Colorado\u2026",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " What a beautifully written piece by @ruthreichl especially if you LOVE #LA  and LOVE #LOVE WOW \u2764\ufe0fJonathan Gold: He gave us th\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " Good morning #LA!!! I will be visiting for one night only 8/15-8/16. Book early!! #redhead #overnight #dinnerdate #flymetoyou #l\u2026",
    " One more person was just killed in #California. #POTUS, it\u2019s your job to take action. #BackfireTrump ",
    " Only time will tell... #EOTW #LA ",
    "Im taking a big risk in about 2 weeks but i know ill come out winning with faith and dedication. Im tired of waitin\u2026 ",
    "You will be missed, Jonathan Gold. #jonathangold #rip #ripjonathangold #la #lafoodcritic @ Los Angeles, California ",
    " Only time will tell... #EOTW #LA ",
    "#GodsNotDead #Jesus #LosAngeles #California #urbanlights #unitedstates #the6ix #YesHeIs #YesHeIsPH #Toronto #Ottawa\u2026 ",
    " Palmdale, #California @PalmdaleAmp rocked my world! You made my night, hope to see you all next #Summer! \ud83e\udd18\ud83c\udffb\ud83c\udfb8\u2620\ufe0f #SoCal #Pa\u2026",
    "Insta 3yrs ago: Minding his post. #elporto #neighborhood #detail #secretspot #telephonepole #manhattanbeach\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " @ArtsandClouds @JonAntoine #Jonathanantoine #Believe #Tenor #England #debut solo  performance in #USA #California @tocap #fred\u2026",
    "The Joy Of Painting...\n\u2022\n\u2022\n\u2022\n#bobross #deadpool #marvel #cosplay #sdcc #sdcc2018 #sandiego #comiccon #international\u2026 ",
    "\u5168\u7403\u534e\u4eba\u79c1\u5bc6\u7ea6\u70ae\u4ea4\u53cb\u5e73\u53f0\n\u7537\u751f\u2795\u5fae\u4fe1Yorkdm\n\u5973\u751f\u2795\u5fae\u4fe1Yorknb\n#\u8d39\u57ce #\u6d1b\u6749\u77f6 #\u7ebd\u7ea6 #\u6ce2\u58eb\u987f #\u7ea6\u70ae #\u591a\u4f26\u591a #\u65e7\u91d1\u5c71 #\u4e0a\u6d77 #\u829d\u52a0\u54e5 #\u534e\u76db\u987f #dc #\u897f\u96c5\u56fe #\u6e29\u54e5\u534e #la #nyc #\u6089\u5c3c #\u4f11\u65af\u987f\u2026 ",
    " \ud83d\udd16 ETIQUETA DE ORO.\n\n\ud83d\udc49 No te olvides hoy venir a la #NOVILLADA una hora antes .... y podras realizar un recorrido por #La#Mas#\u2026",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "The #hangover is very real \u270c\ud83c\udffb #sundayselfie #desert style \ud83d\ude0e\ud83d\udd25 #eastjesus #selfie #patagonia #sundayfunday #roadtrip\u2026 ",
    "20 essential breakfast burritos in Los Angeles ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " \u2733\ufe0fMILLIE \u2733\ufe0f #A5188528 \u2733\ufe0f\n\ud83d\udd39Shiba Inu\ud83d\udd39AGE 7yrs\n\ud83d\udd39Female (S)\ud83d\udd39ARRIVED:6/11\n\ud83d\udc96 AVAILABLE:6/11\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 2\u2026",
    "Beautiful #California style dry #warm #weather in #Chisinau, #Moldova where we visited the #church and #monastery t\u2026 ",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    "Sea of tomatoes! Our tomato plants are at their best production now. We are harvesting lots of cherry tomatoes and\u2026 ",
    " avo got you, under my skin \ud83e\udd51 still living my best #avocadotoast life in #la \ud83c\udf7d: ch\u00e8vre \u2022 avo \u2022 mortadella \u2022 purslane \u2022 tr\u2026",
    " \ud83d\ude43\ud83d\ude09\ud83d\ude02\ud83d\udcaa#actor #actorslife #beyourself #neverstopexploring #newyork #miamibeach #miami #losangeles #california ",
    "Vintage @DisneylandToday Photography Series \ud83d\udcf8 A moment in time from 2015, from #Disneyland's Diamond 60th Celebrati\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Im taking a big risk in about 2 weeks but i know ill come out winning with faith and dedication. Im tired of waitin...it\u2026",
    " .\nSummer 2018 \nFREE Outdoor #Movies \ud83c\udfa5 \n#OrangeCounty #CA area \n\n\ud83d\udc49\ud83c\udffc \n\n   \ud83c\udf7f \n#OC  #Brea \n#NewPortBeach\u2026",
    " California Bans Hemp-Derived CBD Oil\n@GodzWeedz \n\n",
    " wow\nBig shoot-out in E.Hollywood #LA- @TraderJoes\n\nA domestic\nturned into car chase\nTurned into a hostage situation \n#Cops ru\u2026",
    "Thicc Vic #thiccvic #bigvic #vicsofinsta #fordcrownvictoria #california #sanfran #baybridge #sanfrancisco #tunnel\u2026 ",
    "#California 4 over Ebbetts Pass, Westbound: Dashcam #YouTube #SierraNevada #Facebook #Artist...\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " #removeDevinNunes #California #Fresno #Tulare #Visalia ",
    " Have any of you heard about this? \n\n#MAGA\n#California\n#VoteRED\n#Vote2018\n#VoteRed2018\n#VoteDemsOut ",
    "Our first #happyhour of the day kicks off at 9AM! Come get those 5 1/8ths! #inglewood #california #marijuana #weed\u2026 ",
    " #removeDevinNunes #California #Fresno #Tulare #Visalia ",
    " Only time will tell... #EOTW #LA ",
    "Switzerland love! \ud83d\udc9a\ud83d\udc99\n.\n.\n.\n.\n#LA #WestLA  #SantaMonicaBeach  #MontanaAve #PCH  #RealTea #LifestyleBlogger #LAEats\u2026 ",
    " Personal del @MetroCDMX  rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Tra\u2026",
    " Only time will tell... #EOTW #LA ",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    "Supreme Court lets #California gun control laws stand - \n\nSee which politicians are/ aren\u2019t\u2026 ",
    "The best 14sec of your life #17 (like my post ) 100 new songs coming 2018 #seventeen #SoundCloud#music#missouri #fl\u2026 ",
    "#FelizDomingo \n#California ",
    "El Matador Beach #california #losangeles #grateful #malibu #happy #family #elmatadorbeach #actress #life #beach\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "3bd 3br @ 2906 11th 2-5PM #SantaMonica  #realtor #openhouse #realestate  #realestateagent #losangelesrealestate\u2026 ",
    "Vote @JanzforCongress Andrew Janz #California! Kick lying traitor conspirator Nunes to the curb!!",
    "#Wise #wiseWords #Lebron #LA #Mural #Fixed !! ",
    " Only time will tell... #EOTW #LA ",
    "Looking For The Perfect Home?\nWith the fastest listing alerts directly from the MLS, be the first to know when your\u2026 ",
    " Inland Empire residents: Update on wild burro shot by arrow! Donkeyland is still trying to find the burro. Also, $1,000\u2026",
    " Only time will tell... #EOTW #LA ",
    " What a beautifully written piece by @ruthreichl especially if you LOVE #LA  and LOVE #LOVE WOW \u2764\ufe0fJonathan Gold: He gave us th\u2026",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Personal del Sistema rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Transfere\u2026",
    " Only time will tell... #EOTW #LA ",
    " #PICTURED: #Gunman walks out of #LA #TraderJoes in handcuffs and surrounded by hostages at the end of a #terrifying siege\u2026",
    " RT! #California CD7 #Election2018 #KeepItBlue #WinBlue\n\nSupport DR. AMI BERA #CA07,&amp; @DemsWork4USA\n\ud83d\udc49",
    "#Hollywood #LA\nMental illness hearts! \n\nA suspenseful and gripping love story.\nGet your copy of THE LOVELOCK\n\n=&gt;\u2026 ",
    " Lock him up!! Lock him up!! #LockHimUp #nunes #california ",
    " Se il #cambiamento \u00e8 ormai una costante, occorre sostenere - all'interno delle nostre organizzazioni - #la cultura del\u2026",
    " Only time will tell... #EOTW #LA ",
    " RT! #California #Election2018 #WinBlue\n\nSupport Sen. DIANNE FEINSTEIN #CAsen, &amp; @DemsWork4USA\n\ud83d\udc49\n\n#\u2026",
    "Meet one of the Pacific Tugboat fleet, The J.M. Hidalgo. Because #hidalgoforcongress is from National City and he h\u2026 ",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    "We're grateful for your post!   El Matador Beach #california #losangeles #grateful #malibu\u2026 ",
    " \n\nVERFASSUNGGEBENDE VERSAMMLUNG IN DEN #USA\n\n#Michigan #Alabama #Arizona #Alaska #California #Colorado\u2026",
    " \ud83d\udd16 ETIQUETA DE ORO.\n\n\ud83d\udc49 No te olvides hoy venir a la #NOVILLADA una hora antes .... y podras realizar un recorrido por #La#Mas#\u2026",
    " #PICTURED: #Gunman walks out of #LA #TraderJoes in handcuffs and surrounded by hostages at the end of a #terrifying siege\u2026",
    " WOW! \n\n\u201cLiberal 9th Circuit surprises with a pro-2nd Amendment decision blocking California ammo\u201d \n\nA glimmer of hope for\u2026",
    " We're the No. 1 hospital in #California &amp; No. 5 in the nation! Follow us for the latest health news. #BestHospitals",
    " Only time will tell... #EOTW #LA ",
    "Laughter is timeless, imagination has no age, and dreams are forever. \n~Walt Disney~\n.\n.\n.\n.\n#disney #california\u2026 ",
    " Beautiful Summer Sunday for all you, my friends!\u2600\ufe0f\ud83c\udf43\ud83c\udf3b\n\n#BalboaPark #SanDiego #California ",
    " RT if you're in the mood for the party like this. \ud83c\udf7e\ud83c\udf7e\ud83c\udf7e #illustration #HIPHOP #rap #gangsta #SnoopDogg #drdre #IceCube #tupacs\u2026",
    " #Hollywood #LA\nMental illness hearts! \n\nA suspenseful and gripping love story.\nGet your copy of THE LOVELOCK\n\n=&gt; ",
    " Only time will tell... #EOTW #LA ",
    "#La #Marque #Store #Stylish &amp; #Comfortable #Cotton #Casual Slip-On #Shoes For #Women And\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " WOW! \n\n\u201cLiberal 9th Circuit surprises with a pro-2nd Amendment decision blocking California ammo\u201d \n\nA glimmer of hope for\u2026",
    " NO MIRES ATR\u00c1S, AMOR \n#crimen #m\u00fasica #literatura #amor #suspense #thriller #kindleUnlimited #PrimeReading #Mexico #US\u2026",
    " Only time will tell... #EOTW #LA ",
    "#Guin\u00e9e  #Solidarit\u00e9 #la\u00efque",
    "#california #californication #SouthernCalifornia #CuresNow #beautifulplaces #Beachfest2016 #beach #palmtreescfdj",
    "Late night #gumbo #LilAOnTheTrack shout out to the big homie @StanleyRandolph \n#studiovibe #westcoastin #memphis\u2026 ",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    " Personal del Sistema rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Transfere\u2026",
    " \ud83d\udd01#Election2018 CD48 #California #WinBlue\n\nSupport HARLEY ROUDA #CA48,&amp; @DemsWork4USA\n\ud83d\udc49\n\nStop Rohra\u2026",
    "#np on #SoundCloud #world #win\n#chikidddre #atlanta #chicago #minneapolis #minnesota #world #love #family #sun #sky\u2026 ",
    "At 2:45 in @tomgreenlive &amp; @bigjayoakerson w/ @iamToddyTickles they discuss @justforlaughs #JFLMTL, crowd work, #LA\u2026 ",
    "Hand selected with a wide variety of options to make your personal style shine bright! #WKodak #hoboken #Style\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Great value San Francisco hotel near Union Square and Chinatown! ",
    " Only time will tell... #EOTW #LA ",
    "When you choose freedom for yourself, you chose freedom for others. Be the hero of your own story!\u2026 ",
    " Only time will tell... #EOTW #LA ",
    "#I own the rights to this music#\nGutter Made Campaign\n#la#rnb#stage#preformance#musicnationradio#music#mix#single#n\u2026 ",
    " Looking for a job in #credit? View open credit and A/R positions here: ",
    " If you are looking for a sugar daddy RT this so I could notice you, no nudes needed if you want to give a picture by p\u2026",
    "Up close!\n#painting #museum #simon #norton #LA #near #sighted #looking #close #admiring #framed #what #people\u2026 ",
    " What a beautifully written piece by @ruthreichl especially if you LOVE #LA  and LOVE #LOVE WOW \u2764\ufe0fJonathan Gold: He gave us th\u2026",
    "Can you recommend anyone for this #job in #California, MD? ",
    "NEW POSTING! Great opportunity to be the next Interim or Permanent Head of School @BuckleySchool\u2026 ",
    " HEADSHOT PHOTOGRAPHER WANTED. Great exposure and Worldwide publicity. #headshots #photography #talent #actor #star #hol\u2026",
    "#aboutlastnight Entr\u00e9e: Thai Coconut Curry Snapper w/ Vegetables &amp; Jasmine Rice\n.\n.\n.\n#goodenuf2eat #cheflife\u2026 ",
    "Another #california political LOSER on the govt pay everything bandwagon",
    " \u0e0a\u0e37\u0e48\u0e2d\u0e20\u0e32\u0e1e : \u0e41\u0e17\u0e2d\u0e34\u0e25\u0e44\u0e21\u0e48\u0e40\u0e2b\u0e07\u0e32\u0e04\u0e23\u0e31\u0e1a By #Johntography #taeil #LA #NCT127 ",
    " Mood ~ All smiles. \u2728\ud83d\ude0e\u26f5\ufe0f\nMet my editing deadline! We celebrated under sail with great wind, weather &amp; stories.\nWishing yo\u2026",
    " Only time will tell... #EOTW #LA ",
    " #ABadDecisionIn4Words\n\n#California voting for Newsom\n\n#NoSocialistCA ",
    "Wisconsin Lake Front Living Realtor - Oleksiy Tsyapalo - \ud83d\udcbb\ud83d\udcf2\ud83c\udfe1\ud83c\udfd8\ud83c\udfda\ud83c\udfe0\ud83c\udfe1#LakeLife #Dream #Kitchen #LuxuryLexLiving\u2026 ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    " #Hollywood #LA\nMental illness hearts! \n\nA suspenseful and gripping love story.\nGet your copy of THE LOVELOCK\n\n=&gt; ",
    "Bird Patrol \n\n#california #californiaart #californiaartist #eastbayartist #eastbayart #bayareaart #bayareaartist\u2026 ",
    " A call out from @occupyicela to any #LA area folks that can get food/water to the encampment at the Federal Detention Cent\u2026",
    " Home to stars, Hollywood! Here we come!\n\n&lt;Location&gt;\n6922 Hollywood Blvd, Los Angeles, CA 90028 \n\n#BT21 #LA #HOLLYWOOD #COMINGSOO\u2026",
    " Home to stars, Hollywood! Here we come!\n\n&lt;Location&gt;\n6922 Hollywood Blvd, Los Angeles, CA 90028 \n\n#BT21 #LA #HOLLYWOOD #COMINGSOO\u2026",
    "@lilreik_gmb Shit Crankk Lil Bro Keep Workinn\ud83d\udcaf\ud83d\udd0b\ud83d\udcaa\ud83c\udffe",
    "Black Void 1\n\n#art by Mark\n\n\n#Painting #Modernart #contemporaryart #abstractart\u2026 ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    ".@POTUS @HouseGOP @SenateGOP \n\n#GunControl \n\n#NRA in bed with #RussianCollusion \nWe must help #NRA get back to it's\u2026 ",
    " #removeDevinNunes #California #Fresno #Tulare #Visalia ",
    "#Ocean #Beach #Clouds #BlueSky #Waves #PacificOcean #OrangeCounty #NewportBeach #CrystalCove #SoCal #Cali\u2026 ",
    "Escondido, #CA - Tradesmen International - Concrete Laborer - Concrete Laborer Posted Date 4 hours ago7/17/2018 207\u2026 ",
    "KPFF Consulting Engineers is looking for an Engineering-Civil Project Manager in #Irvine #California #UnitedStates\u2026 ",
    " Personal del Sistema rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Transfere\u2026",
    "@suzymusing Yes! Yay! #LA",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " Home to stars, Hollywood! Here we come!\n\n&lt;Location&gt;\n6922 Hollywood Blvd, Los Angeles, CA 90028 \n\n#BT21 #LA #HOLLYWOOD #COMINGSOO\u2026",
    " Let us help you find the best #medicalmarijuana #dispensaries and doctors in #California. #wellness #cannabis ",
    " NO MIRES ATR\u00c1S, AMOR \n#crimen #m\u00fasica #literatura #amor #suspense #thriller #kindleUnlimited #PrimeReading #Mexico #US\u2026",
    " Personal del @MetroCDMX  rescat\u00f3 a canino en interestaci\u00f3n #CanalDeSanJuan - #Tepalcates #LA. Se traslad\u00f3 al Centro de Tra\u2026",
    "BLOG: Shop 'til you drop with our list of the best boutiques in #LA! ",
    "Discover for yourself why Good Nite Inn is the best #California economy #hotel company to work for. We're hiring a\u2026 ",
    "I keep seeing #pancreaticcancer pop up too much in #California deaths. Is it past #airquality issues? #pollution in\u2026 ",
    "We have security doors with lock and frame, ready to install. Asked Questions: (818) 470-2378 #derasgaragedoors # 2\u2026 ",
    "#REALTORS Meet #Cash #Buyers #Investors at #FREE #RealEstate #EVENTS in #CHICAGO #NEWYORK #FLORIDA #CALIFORNIA #UTAH ",
    "good morning!! Don't forget to put on your SUNSCREEN before you start your day! Love, SHOW A LITTLE SKINcare\u2026 ",
    "Listen to The Focus - [Prod. Codeine Clique] by PESO #np on #SoundCloud| #NewMusic #HipHop #Rap #Musicians\u2026 ",
    "Swam a few laps - feeling pretty #blessed in #atherton #california .\n.\n.\n#wellness \n#nature \n#landscapearchitecture\u2026 ",
    "@LuisinJimenezc #La soledad del poder, cuando el panorama y  garant\u00eda d continuidad se expuman siempre desvela la t\u2026 ",
    "Wake up #LA!!!! Nothing comes to a sleeper but a dream. Miller Marketing &amp; Consulting wants to make your #DREAMS a reality!!!",
    "\ud83c\udfc5Careen always makes a splash on the ballroom floor ! Here she is with her teacher Slava !!! This is a great perfor\u2026 ",
    " Hey @tmorello @BradWilkdrummer @RATM would be a MASSIVE honor if you came to watch JAXON @jaxon_drums tomorrow (Sunday Ju\u2026",
    " \u2733\ufe0fSIGGI \u2733\ufe0f #A5182215 \u2733\ufe0f\n\ud83d\udd39Pit Bull\ud83d\udd39AGE 2yrs\n\ud83d\udd39Female\ud83d\udd39ARRIVED:5/24\n\ud83c\udf88\ud83c\udf88\ud83c\udf89RESCUED\ud83c\udf89\ud83c\udf88\ud83c\udf88\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W Vict\u2026",
    "What You Need to Know About California\u2019s New Data Privacy Law\n\n#TrainingDoyens #Compliance\u2026 ",
    "#Coinbase has formed a political action committee (PAC) to raise money to spend on U.S. elections.\u2026 ",
    "19 Experts Explain Why Your Website Isn't Bringing in Customers ",
    "#La Cheeserie",
    "Speedy was in a hurry when we spotted him @sixflagsdk #sixflags #california @ Six Flags Discovery Kingdom ",
    "Don't miss #Candytopia in #LA this year! \ud83c\udf6d\ud83c\udf6c\n\nToday is the last day, so grab a #BikeShareConnect bike and ride to ou\u2026 ",
    " Mood ~ All smiles. \u2728\ud83d\ude0e\u26f5\ufe0f\nMet my editing deadline! We celebrated under sail with great wind, weather &amp; stories.\nWishing yo\u2026",
    " Only time will tell... #EOTW #LA ",
    "",
    " Just got a call from #LA that could change my life forever wish me luck \ud83d\udc41",
    " #Hollywood #LA\nMental illness hearts! \n\nA suspenseful and gripping love story.\nGet your copy of THE LOVELOCK\n\n=&gt; ",
    " Right now my little rocker Jaxon @jaxon_drums is shredding RUSH @rushtheband YYZ in California !!! \n\n#Rush #California #y\u2026",
    " Only time will tell... #EOTW #LA ",
    "She was born to ride unicorns\ud83e\udd84\ud83c\udf08\n.\n.\n.\n\ud83d\udcf8 @lillian_cay &amp; lunar0ssa\n.\n.\n.\n#SunDazeTribe \n.\n.\n.\n#sundazefloats\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " Only time will tell... #EOTW #LA ",
    " Vintage @DisneylandToday Photography Series \ud83d\udcf8 A moment in time from 2015, from #Disneyland's Diamond 60th Celebration. Th\u2026",
    " \ud83d\udd01#California #Election2018 #WinBlue\n\nSupport Sen DIANNE FEINSTEIN #CAsen, &amp; @DemsWork4USA\n\ud83d\udc49\n\n#YesW\u2026",
    "The World Spoke #StopDogMeat @KoreaExpose @Haekoko @kwaakreports @TheJihyeLee\n@allyjung @AP @APklug @namsama_wsj\u2026 ",
    " Today's Office! #California #starsalign #tour #onstage #awoh ",
    " Today's Office! #California #starsalign #tour #onstage #awoh ",
    " Only time will tell... #EOTW #LA ",
    " Have any of you heard about this? \n\n#MAGA\n#California\n#VoteRED\n#Vote2018\n#VoteRed2018\n#VoteDemsOut ",
    "DM for Booking and Collabs #california #socal #park #outdoor #beauty #photo #photoshoot #model #park\u2026 ",
    " In #California Independents now outnumber @GOP &amp; they are a third party. \ud83d\ude0bAccording to @newsweek's report, \"Independen\u2026",
    " \ud83d\udea8\ud83d\udea8URGENT Please save this sweet girl! Needs to be adopted or rescued, please save a life \u2764\ud83d\udea8 ",
    " Oh look there\u2019s a\n\nHumpback Whale!\n\n\ud83d\udc0b \n\n#Ocean #Nature #California \n\n",
    "Gracias Maracaibo por el cari\u00f1o, un encuentro inolvidable #la m\u00fasica es pasi\u00f3n \ud83d\udc4f\ud83c\udffb\ud83d\udc4f\ud83c\udffb\ud83d\udc4f\ud83c\udffb\ud83d\ude0a\u263a\ufe0f\ud83c\uddfb\ud83c\uddea\ud83c\uddfb\ud83c\uddea oficialguaco\u2026 ",
    "STILL MISSING... Since 02.06.2013... Over FIVE years...\nCrishtian Hughes, 20 (age at disappearance). Tattoos on bot\u2026 ",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " Beautiful Summer Sunday for all you, my friends!\u2600\ufe0f\ud83c\udf43\ud83c\udf3b\n\n#BalboaPark #SanDiego #California ",
    " \ud83c\udf54\ud83c\udf54\ud83c\udf54\n\n#NCT127 #LA ",
    " \u2733\ufe0fBEAUTY \u2733\ufe0f #A5202204 \u2733\ufe0f\n\ud83d\udd39Pit Bull\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female\ud83d\udd39ARRIVED:7/20\n\ud83d\udc96 AVAILABLE:7/20\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #LA\n\ud83d\udd38 216 W\u2026",
    "Add me on kik for sext and nudes name : ONOMORA  #kermit #crazybitch #nyc #la ",
    "Adios #california. Until next time. \u2764\ufe0f @ Altamont Pass Wind Farm ",
    "Good morning from #BigBear #California #GrizzlyManor #BestBreakfastinBigBear ",
    " PCSing to Camp Pendleton? We got you. #Marine #California #Military ",
    " Our sibling program, the CCST Science Translators Showcase, is recruiting again! Open to master's, PhD, and postdoc resear\u2026",
    "My own private beach. Not a bad spot for karate practice. #PointArena #California #travel ",
    " Check out a #behindthescenes look at @SamSpiegelUni's \"Jihad Love Squad\" #musicvideo and his production process while at his h\u2026",
    " Stay @deanzaspringsresort for your next #clothingoptional #weekendgetaway #hikenaked #wine #bar #drinkwine #naked #nud\u2026",
    "#LA in #Sepia by Budapest-based photographer, Mate Steindl. Wow \ud83d\ude0d\n\n\n\nMore Los Angeles this w\u2026 ",
    " At Least 150 OC Jail Inmates on Hunger Strike to Protest Conditions and Treatment #OrangeCount #California ",
    " UPDATE\u203c\ufe0fBEAUTIFUL *BETHANY* IS SAFE!\ud83d\ude4f\u2764\ufe0f\ud83d\ude0a\ud83d\udc3e\ud83d\udc4f ADOPTED PER FB NOTES! \ud83c\udf8a\ud83c\udf89\ud83c\udf89\ud83c\udf89\ud83c\udf8aTHIS IS WONDERFUL NEWS! SO LA #ACC  #CA THX FOR RTS!\u2026",
    " Only time will tell... #EOTW #LA ",
    "@shethacoldest Download ThaAfterparty radio app and tune in to Hood Humor with @HUNED_P and @MRBRANDONBLACK  every\u2026 ",
    "Fresno, #CA - Emser Tile LLC - OUTSIDE SALES REPRESENTATIVETRADE - FRESNO CA - Responsible for building the brand a\u2026 ",
    " Beautiful Summer Sunday for all you, my friends!\u2600\ufe0f\ud83c\udf43\ud83c\udf3b\n\n#BalboaPark #SanDiego #California ",
    " \ud83d\ude43\ud83d\ude09\ud83d\ude02\ud83d\udcaa#actor #actorslife #beyourself #neverstopexploring #newyork #miamibeach #miami #losangeles #california ",
    "#SundayMorning #FelizDomingo #GermanGP #TheOpen #Holidays #Summer\n#TDF2018 #France #Barranquilla2018 #Colombia\u2026 ",
    " @shethacoldest Download ThaAfterparty radio app and tune in to Hood Humor with @HUNED_P and @MRBRANDONBLACK  every Sunday from\u2026",
    " Stealing from those that have nothing already..that's a whole new kind of low. #California #Governor #JerryBrown #Home\u2026",
    "#luxurylifestyle #california #model anastassija_m #retouching jeffwhitlockdigitalartist  #marinadelrey @ La Crescen\u2026 ",
    " Only time will tell... #EOTW #LA ",
    " My morning in Avalon Bay\n\non Santa Catalina Island \n\n\ud83c\udf34 \u26f5\ufe0f\n\n#SaturdayMorning #Sailing #Boating #amjoy #Travel #California #satu\u2026",
    " \u2733\ufe0fSUMMER \u2733\ufe0f #A5201983 \u2733\ufe0f\n\ud83d\udd39St Bernard Smth\ud83d\udd39AGE 3yrs\n\ud83d\udd39Female (S)\ud83d\udd39ARRIVED:7/19\n\ud83d\udc96 AVAILABLE:7/19\n\n\ud83d\udd38310-523-9566\ud83d\udd38#CarsonShelter #\u2026",
    "It\u2019s not even up for discussion at this point . Yor muh jes go sit dan smor ! #LIBTAKEOVER #ATL #DC #LA "
]

the_tweets_geo_extent = [
        {
            "primary_geo": "Stafford, UK"
        },
        {
            "primary_geo": "L.A."
        },
        {
            "primary_geo": "Orange County CA"
        },
        {
            "primary_geo": "Leicestershire, United Kingdom"
        },
        {
            "primary_geo": "\u30ab\u30cb\u30e3\u30ac\u30ef\u30df\u30ca\u30df\u30ce\u30db\u30a6 JAPAN"
        },
        {
            "primary_geo": "La Reina, Santiago"
        },
        {
            "primary_geo": "Palm Bay, FL"
        },
        {
            "primary_geo": "Finland"
        },
        {
            "primary_geo": "Detroit"
        },
        {
            "primary_geo": "Texas"
        },
        {
            "primary_geo": "\u65e5\u672c"
        },
        {
            "primary_geo": "US"
        },
        {
            "primary_geo": "Montr\u00e9al, Qu\u00e9bec"
        },
        {
            "primary_geo": "\u3053\u3053\u3067\u8ae6\u3081\u305f\u3089\u4eca\u307e\u3067\u306e\u81ea\u5206\u304c\u53ef\u54c0\u60f3\u3060\u3068\u541b\u306f\u6ce3\u3044\u305f"
        },
        {
            "primary_geo": " \u30aa\u30eb\u30b4\u30fc\u30eb\u30e9\u30a4\u30d631\u520653\u79d2Nakajin\u300c\u307e\u308a\u3082\u3055\u3093\u3063\u300d"
        },
        {
            "primary_geo": "WhereWeGoOneWeGoAll"
        },
        {
            "primary_geo": "\u3086\u304d\u3089\u3089"
        },
        {
            "primary_geo": "End Of The World"
        },
        {
            "primary_geo": "SEKAI NO OWARI\ud83c\udfb8"
        },
        {
            "primary_geo": "\u30bb\u30ab\u30aa\u30ef\u306b\u51fa\u9022\u3063\u3066\u4e16\u754c\u304c\u5909\u308f\u3063\u305f"
        },
        {
            "primary_geo": "\u30d6\u30ec\u30fc\u30e1\u30f3 10/19 \u53c2\u6226\u4e88\u5b9a\ud83d\udcaa"
        },
        {
            "primary_geo": "Twitter since 2015.08.13 \ud83c\udf96"
        },
        {
            "primary_geo": "\u307e\u308b\u3044"
        },
        {
            "primary_geo": "\u3053\u306e\u30c8\u30d7\u753b\u8f9e\u3081\u305f\u3044"
        },
        {
            "primary_geo": "\u5922\u306e\u4e16\u754c\u3078"
        },
        {
            "primary_geo": "INSOMNIA TRAIN"
        },
        {
            "primary_geo": "AAA\u3082\u5927\u597d\u304d\u3060\u3088"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "\u6c17\u306b\u306a\u3063\u305f\u4eba\u2728\u27af\u30d5\u30a9\u30ed\u30d0\ud83d\ude46\ud83c\udffb"
        },
        {
            "primary_geo": "\ud83d\udc97\ud83d\udc24\ud83d\udc26\ud83d\udc30\ud83d\udc34\ud83d\udd70\ud83d\udc3b\ud83e\udd21\ud83d\udc7c\ud83c\udffb\ud83d\udc97"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "\u6771\u4eac\u306b\u4f4f\u307f\u305f\u3044\u7530\u820e\u6c11"
        },
        {
            "primary_geo": "\u5927\u5b66\u751f\ud83c\udfb9\ud83c\udfa4\ud83c\udfb8\ud83e\udd21 "
        },
        {
            "primary_geo": "\u65e5\u672c \u57fc\u7389"
        },
        {
            "primary_geo": "\u3082\u3046\u4e00\u5ea6\u9023\u308c\u3066\u884c\u3063\u3066\u3042\u306e\u4e16\u754c\u3078"
        },
        {
            "primary_geo": "\u30b0\u30ea\u30fc\u30f3\u30e9\u30d9\u30eb\ud83d\udc9a\u5f53\u305f\u3063\u3066\u6b32\u3057\u3044"
        },
        {
            "primary_geo": "\u305d\u308c\u3067\u3082\u50d5\u306f\u6226\u3044\u7d9a\u3051\u308b\u3088\u52dd\u3064\u305f\u3081\u306b"
        },
        {
            "primary_geo": "INSOMNIA TRAIN"
        },
        {
            "primary_geo": "INSOMNIATRAIN\u5bcc\u58eb\u60255.27\ud83e\udd8b/6.02\ud83d\udc1e"
        },
        {
            "primary_geo": "\u304a\u5c3bJCT\u304b\u3089\u306e\u4e00\u822c\u9053\u3002"
        },
        {
            "primary_geo": "\u307f\u306a\u3064\u305f\u307e\u306b\u5b58\u5728\u3057\u3066\u3044\u308b\u770b\u8b77\u5b66\u751f\u3092\u3084\u3063\u3066\u3044\u308b\u30d0\u30ab\u3067\u3059"
        },
        {
            "primary_geo": "\u571f\u751f\u745e\u7a42~\u5c3e\u95a2\u68a8\u9999~\u5fd7\u7530\u611b\u4f73~"
        },
        {
            "primary_geo": "\u304a\u3046\u3061\u3002"
        },
        {
            "primary_geo": "\u4f50\u8cc0"
        },
        {
            "primary_geo": "\u3075\u304b\u305b\u3055\u304a\u308a\u3089\u3076\u306a\u304b\u3058\u3093\u2661\u2665"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "sekainoowari.jp"
        },
        {
            "primary_geo": "\u30d5\u30a9\u30ed\u30d0\u306f\u6c17\u307e\u3050\u308c"
        },
        {
            "primary_geo": "INSOMNIA TRAIN 6\u67083\u65e5\u4f59\u97fb\ud83d\udc95"
        },
        {
            "primary_geo": "\u751f\u304d\u3066\u308b\u3060\u3051\u3067\u8912\u3081\u3066\u304f\u308c\u308bFukase bot"
        },
        {
            "primary_geo": "Worldwide"
        },
        {
            "primary_geo": "Chicago"
        },
        {
            "primary_geo": "\u6625\u306e\u8cea\u554f\u30b3\u30fc\u30ca\u30fc~Fukase\u2765"
        },
        {
            "primary_geo": "\u57fc\u7389"
        },
        {
            "primary_geo": "\u304d\u3089 \u3063\u3066\u672c\u540d\u3060\u3088\uff1f\ud83d\ude43"
        },
        {
            "primary_geo": "MY HOME"
        },
        {
            "primary_geo": "SW Washington State, USA"
        },
        {
            "primary_geo": "\ud83d\ude82\ud83c\udfa4\ud83c\udfb9\ud83c\udfa9\ud83e\udd21INSOMNIA TRAIN\ud83c\udfaa\ud83e\udd82\ud83c\udf0c"
        },
        {
            "primary_geo": "nm206 \ud80c\udce0"
        },
        {
            "primary_geo": "\u7761\u7720\u6642\u9593\u3092\u304f\u308c"
        },
        {
            "primary_geo": "SoCal"
        },
        {
            "primary_geo": "Atlanta"
        },
        {
            "primary_geo": "\u30b8\u30e3\u30cb\u30ef"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "\u65e5\u672c"
        },
        {
            "primary_geo": "\ud83c\uddfa\ud83c\uddf8United States"
        },
        {
            "primary_geo": "Big Bear Lake, CA"
        },
        {
            "primary_geo": "Chez ta m\u00e8re"
        },
        {
            "primary_geo": "\u00dcT: -33.892311,18.511224"
        },
        {
            "primary_geo": "\u798f\u30e9\u30d7\ud83d\udc2c\u2665\ufe0f"
        },
        {
            "primary_geo": "\u4f1a\u3044\u305f\u3044\u4f1a\u3048\u306a\u3044\u306e\u306b \u611b\u3057\u3066\u3084\u307e\u306a\u3044 "
        },
        {
            "primary_geo": "\u6771\u4eac"
        },
        {
            "primary_geo": "\u5ca9\u624b"
        },
        {
            "primary_geo": "webstore"
        },
        {
            "primary_geo": "\u7d76\u671b\u3068\u5e0c\u671b\u304c\u4e00\u7dd2\u306b\u3042\u308b\u4e16\u754c"
        },
        {
            "primary_geo": " \u9999\u6e2f "
        },
        {
            "primary_geo": " \u305b\u304b\u3044\u306e\u304a\u308f\u308a / \u3071\u3093\u3060 / \u306f\u3063\u3071 / \u3072\u304b\u308b"
        },
        {
            "primary_geo": "\u5fc3\u306f\u3044\u3064\u3067\u3082\u6d5c\u677e\u306b\u2026"
        },
        {
            "primary_geo": "\u0e15\u0e49\u0e2d\u0e07\u0e15\u0e34\u0e14\u0e2a\u0e32\u0e18\u0e34\u0e15\u0e19\u0e30 \ud83d\ude4f\ud83c\udffb"
        },
        {
            "primary_geo": "Ohio"
        },
        {
            "primary_geo": "twilight city"
        },
        {
            "primary_geo": "Third planet from the sun."
        },
        {
            "primary_geo": "Aberdeen "
        },
        {
            "primary_geo": "\u3059\u304d\u306a\u3053\u3068bot"
        },
        {
            "primary_geo": "\u6771\u4eac\u90fd"
        },
        {
            "primary_geo": "\uacbd\ubd81"
        },
        {
            "primary_geo": "New York, USA"
        },
        {
            "primary_geo": "\ubbfc\uc724\uae30\u267e UB\u2661  ~  Unfollow Block \ud83d\udeab"
        },
        {
            "primary_geo": "Versailles"
        },
        {
            "primary_geo": "Malaysia"
        },
        {
            "primary_geo": "@EARTH\u30bb\u30ab\u30aa\u30ef\u30eb\u6703\u897f\u8328\u57ce\u652f\u90e8 \u652f\u90e8\u9577"
        },
        {
            "primary_geo": "\u300c\u30b3\u30b9\u30e2\u30d1\u30cb\u30c3\u30af\u300d\u306e\u975e\u5e38\u53e3"
        },
        {
            "primary_geo": "EaRth AiChi"
        },
        {
            "primary_geo": "\uff7f\uff98\uff75 \uff8a\uff7d\uff97\uff70 \uff73\uff9e\uff68\uff6f\uff82 \uff8f\uff70\uff81\ud83d\ude97"
        },
        {
            "primary_geo": "Liverpool "
        },
        {
            "primary_geo": "\u0e17\u0e35\u0e48\u0e43\u0e19\u0e2a\u0e31\u0e01\u0e41\u0e2b\u0e48\u0e07\u0e1a\u0e19\u0e42\u0e25\u0e01"
        },
        {
            "primary_geo": "180908-09\u270c\ufe0f\u270c\ufe0f"
        },
        {
            "primary_geo": "next \u2192 CAST 8\u670829\u65e5 \u65e5\u672c\u30ac\u30a4\u30b7\u30db\u30fc\u30eb"
        },
        {
            "primary_geo": "The War Room"
        },
        {
            "primary_geo": "STARLIGHT PARADE \ud83c\udf0c"
        },
        {
            "primary_geo": "France"
        },
        {
            "primary_geo": "Monterrey, M\u00e9xico"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "TK 2/4 \u540d\u53e4\u5c4b\u53c2\u6226\u6e08 \u30fb IT 5/25 \u5bcc\u58eb\u6025\u4e0b\u8eca\u6e08"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Denver, CO"
        },
        {
            "primary_geo": "Leeds, West Yorkshire, England"
        },
        {
            "primary_geo": "Orange County, California"
        },
        {
            "primary_geo": "San Diego"
        },
        {
            "primary_geo": "Jelly Fish"
        },
        {
            "primary_geo": "\u4e00\u5e74\u4e2d\u3001\u96ea\u306e\u964d\u308b\u3053\u306e\u56fd\u3067\u79c1\u306f\u751f\u307e\u308c\u305f\u306e"
        },
        {
            "primary_geo": "KAT-TUN\u304c\u6700\u5f37\u3067\u3054\u3081\u3093\u306a"
        },
        {
            "primary_geo": "Washington"
        },
        {
            "primary_geo": "\u53d7\u9a13\u751f\u3068\u304b\u95a2\u4fc2\u306a\u3044"
        },
        {
            "primary_geo": "(\u4eee)"
        },
        {
            "primary_geo": "\u30d5\u30ab\u30bb\u30b5\u30c8\u30b7    "
        },
        {
            "primary_geo": "Evanston, IL"
        },
        {
            "primary_geo": "\u65e5\u672c \u5e83\u5cf6"
        },
        {
            "primary_geo": "Sacramento, CA"
        },
        {
            "primary_geo": "Las Vegas, NV"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Los Angeles + DC"
        },
        {
            "primary_geo": "LINDEN NJ "
        },
        {
            "primary_geo": "IN THE MIDDLE OF NOWHERE"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Las Vegas, NV"
        },
        {
            "primary_geo": "Chicago"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Sardegna, Italia"
        },
        {
            "primary_geo": "\u751f\u6f14\u594f\u306e\u30d5\u30a1\u30f3\u30bf\u30b8\u30fc\u304a\u9858\u3044\u3057\u307e\u3059\uff01"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "B\u578b,168cm\u306b\u604b"
        },
        {
            "primary_geo": "London, UK"
        },
        {
            "primary_geo": "New York, NY"
        },
        {
            "primary_geo": "\u3042\u3063\u3061"
        },
        {
            "primary_geo": "\u9280\u6cb3\u8857"
        },
        {
            "primary_geo": "\u6642\u3005\u982d\u304c\u304a\u304b\u3057\u304f\u306a\u308b"
        },
        {
            "primary_geo": "Greenback Tn "
        },
        {
            "primary_geo": "TakaNishi G \u2192 Gifu U.Edu.\u2460 \ud83c\udfbc"
        },
        {
            "primary_geo": "\u3044\u308d\u3093\u306a\u30ea\u30a2\u53cb\u306b\u30d0\u30ec\u305f\u304b\u3089\u3086\u30fc\u3063\u304f\u308a\u30a2\u30ab\u79fb\u884c"
        },
        {
            "primary_geo": "God Bless America \ud83c\uddfa\ud83c\uddf8"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Winston-Salem, NC"
        },
        {
            "primary_geo": "Seoul, Republic of Korea"
        },
        {
            "primary_geo": "\u65e5\u672c"
        },
        {
            "primary_geo": "AAA \uff1d \u9178\u7d20"
        },
        {
            "primary_geo": "junghoseok"
        },
        {
            "primary_geo": "The Bahamas"
        },
        {
            "primary_geo": "\u677e\u6c5f\u5e02\u307f\u305a\u3046\u307f\u5317"
        },
        {
            "primary_geo": "New Mexico, USA"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "Beverly Hills, CA"
        },
        {
            "primary_geo": "\u65e5\u672c\u9752\u68ee"
        },
        {
            "primary_geo": "Canada - Earthling, Humanist.  CB Crouching goofy, hidden mickey. Trolls get rolled & silenced. Good Witch of the North"
        },
        {
            "primary_geo": "New York, USA"
        },
        {
            "primary_geo": "Houston, TX"
        },
        {
            "primary_geo": "Osasco"
        },
        {
            "primary_geo": "\u65e5\u672c"
        },
        {
            "primary_geo": "\u65e5\u672c"
        },
        {
            "primary_geo": "West Yorkshire. England."
        },
        {
            "primary_geo": "California Non-Metro"
        },
        {
            "primary_geo": "Fukuoka"
        },
        {
            "primary_geo": "\u65e5\u672c"
        },
        {
            "primary_geo": "AUSTRIA - EUROPE - WORLDWIDE"
        },
        {
            "primary_geo": "City Of Glasgow, Scotland, UK"
        },
        {
            "primary_geo": "INSOMNIA TRAIN \u5bcc\u58eb\u6025 \u5bae\u57ce \ud83d\ude82"
        },
        {
            "primary_geo": "(\u4e00)"
        },
        {
            "primary_geo": "\u5e83\u5cf6\u5e02"
        },
        {
            "primary_geo": "Aurora, IL"
        },
        {
            "primary_geo": "Manila, Philippines"
        },
        {
            "primary_geo": "Satire, USA"
        },
        {
            "primary_geo": "Courbevoie, Paris La Defense"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Denver, CO"
        },
        {
            "primary_geo": "FUKUOKA"
        },
        {
            "primary_geo": "Rostock, Deutschland"
        },
        {
            "primary_geo": "Roma, Lazio"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "California Non-Metro"
        },
        {
            "primary_geo": "Long Beach"
        },
        {
            "primary_geo": "\u68ee\u306e\u4e2d"
        },
        {
            "primary_geo": "Sacramento, CA"
        },
        {
            "primary_geo": "Oakland, CA"
        },
        {
            "primary_geo": "Fresno, CA"
        },
        {
            "primary_geo": "San Diego, CA"
        },
        {
            "primary_geo": "Anahei"
        },
        {
            "primary_geo": "italia"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Anaheim, CA"
        },
        {
            "primary_geo": "Berkeley, CA"
        },
        {
            "primary_geo": "Bakersfield, CA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "\u9759\u5ca1\u770c"
        },
        {
            "primary_geo": "Hello again, Mr.Heartache"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "\u6df1\u702c\u30e2\u30ca\u30ab\u4eba"
        },
        {
            "primary_geo": "USA"
        },
        {
            "primary_geo": "Brasil"
        },
        {
            "primary_geo": "\u798f\u5ca1"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "Carlsbad, CA"
        },
        {
            "primary_geo": "Berlin, Germany"
        },
        {
            "primary_geo": "\u3060\u3044\u3055\u304f\u305b\u3093\u3075"
        },
        {
            "primary_geo": "Texas"
        },
        {
            "primary_geo": "\u304b\u3044\u3068\ud83d\udc99"
        },
        {
            "primary_geo": "Michigan, USA"
        },
        {
            "primary_geo": "Houston, TX"
        },
        {
            "primary_geo": "en un lugar de la mancha!!!"
        },
        {
            "primary_geo": "Deutschland"
        },
        {
            "primary_geo": "Silicon Valley, US"
        },
        {
            "primary_geo": "\u795e\u5948\u5ddd"
        },
        {
            "primary_geo": "Texas, USA"
        },
        {
            "primary_geo": "New York, NY"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "\u795e\u5948\u5ddd\u30fb\u6771\u4eac\u30fb\u5c71\u68a8"
        },
        {
            "primary_geo": "Floripa"
        },
        {
            "primary_geo": "Illinois, USA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Portland, OR"
        },
        {
            "primary_geo": "Palo Alto, CA"
        },
        {
            "primary_geo": "OKINAWA"
        },
        {
            "primary_geo": "NYC | LA"
        },
        {
            "primary_geo": "Waco, TX"
        },
        {
            "primary_geo": "Bruy\u00e8res-Le-Chatel, France"
        },
        {
            "primary_geo": "\u6df1\u702c\u6167\u306e\u4eba\u751f\u304c\u597d\u304d\u3002"
        },
        {
            "primary_geo": "R.A.I.N.S \u2602\ufe0f"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Bronx, NY"
        },
        {
            "primary_geo": "\u3042\u3044\u3061"
        },
        {
            "primary_geo": "Strasbourg, France"
        },
        {
            "primary_geo": "Oklahoma"
        },
        {
            "primary_geo": "Malibu, California, USA"
        },
        {
            "primary_geo": "SEKAINOOWARI"
        },
        {
            "primary_geo": "\u4eac\u90fdJP \u6843\u5712TW"
        },
        {
            "primary_geo": "God's Country..."
        },
        {
            "primary_geo": "\u5468\u308a\u306b\u6d41\u3055\u308c\u306a\u3044\u4eba\u306b\u306a\u308b\u3002"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Marga-Marga, Chile"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Colorado"
        },
        {
            "primary_geo": "Lafayette, LA"
        },
        {
            "primary_geo": "West Hollywood, California"
        },
        {
            "primary_geo": "\u76f8\u65b9\u306f\u307f\u3046\ud83c\udf37\u30d8\u30c3\u30c0\u30fc\u306f\u307e\u3081\ud83c\udf31"
        },
        {
            "primary_geo": "Germany"
        },
        {
            "primary_geo": "Covina, CA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "West Yorks UK "
        },
        {
            "primary_geo": "\u00dcT: 41.933575,-88.082541"
        },
        {
            "primary_geo": "Chickasha, OK"
        },
        {
            "primary_geo": "\u5317\u6d77\u9053"
        },
        {
            "primary_geo": "M\u00e9xico D.F. "
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Santa Monica, CA"
        },
        {
            "primary_geo": "New York, NY"
        },
        {
            "primary_geo": "USA"
        },
        {
            "primary_geo": "FRANCE"
        },
        {
            "primary_geo": "6ix"
        },
        {
            "primary_geo": "Wien, \u00d6sterreich"
        },
        {
            "primary_geo": "Florida / Born in NewYork"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Illinois, USA"
        },
        {
            "primary_geo": "Longmont, CO"
        },
        {
            "primary_geo": "Huntington Beach, CA"
        },
        {
            "primary_geo": "Belgium"
        },
        {
            "primary_geo": "Washington, DC"
        },
        {
            "primary_geo": "\u5317\u6d77\u9053\u27aa\u798f\u4e95"
        },
        {
            "primary_geo": "Everywhere"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Kalaheo, HI"
        },
        {
            "primary_geo": "\u4e16\u2687\u754c\u2687\u672b\u2687\u65e5"
        },
        {
            "primary_geo": "\u65e5\u672c"
        },
        {
            "primary_geo": "Blips and Chitz "
        },
        {
            "primary_geo": "Chicagoland"
        },
        {
            "primary_geo": "Cleveland, OH"
        },
        {
            "primary_geo": "\u65e5\u672c \u6771\u4eac"
        },
        {
            "primary_geo": "Corvallis, OR"
        },
        {
            "primary_geo": "Maryland, USA"
        },
        {
            "primary_geo": "Bottesford, England"
        },
        {
            "primary_geo": "California Non-Metro"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "Hip-Hop, USA \u2022\uf8ff\u2022"
        },
        {
            "primary_geo": "Edinburgh, United Kingdom"
        },
        {
            "primary_geo": "INTJ"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "California Non-Metro"
        },
        {
            "primary_geo": "OH10"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "United Kingdom"
        },
        {
            "primary_geo": "\u306a\u3064\u306e\u304a\u3075\u3068\u3045\u3093\u306e\u3046\u3048\ud83c\udf5e"
        },
        {
            "primary_geo": "INSOMNIA TRAIN\u4f59\u97fb"
        },
        {
            "primary_geo": "Croydon, PA(Near Philly) USA"
        },
        {
            "primary_geo": "california"
        },
        {
            "primary_geo": "In #libreria"
        },
        {
            "primary_geo": "\u57fc\u7389 \u6625\u65e5\u90e8"
        },
        {
            "primary_geo": "USA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Worldwide"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Southern California"
        },
        {
            "primary_geo": "Fancytown, Colorado"
        },
        {
            "primary_geo": "\u4e09\u91cd \u56db\u65e5\u5e02\u5e02"
        },
        {
            "primary_geo": "Maryville, TN"
        },
        {
            "primary_geo": "Los Angeles, USA"
        },
        {
            "primary_geo": "New York City, NY"
        },
        {
            "primary_geo": "Utley, TX"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "@EARTH\uff7e\uff76\uff75\uff9c\uff99\u6703\u57fc\u7389\u652f\u90e8"
        },
        {
            "primary_geo": "United Kingdom"
        },
        {
            "primary_geo": "Miami, FL"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Bensonhurst, NYC"
        },
        {
            "primary_geo": "\u30c8\u30df\u3055\u3093\u306b\u30ea\u30d7\u8fd4\u8cb0\u3063\u305f\u65e5\u21d21/17"
        },
        {
            "primary_geo": "Irvine, CA"
        },
        {
            "primary_geo": "Kentucky, USA"
        },
        {
            "primary_geo": "South Florida"
        },
        {
            "primary_geo": "Johannesburg, South Africa"
        },
        {
            "primary_geo": "kanagawa"
        },
        {
            "primary_geo": "Hong Kong"
        },
        {
            "primary_geo": "\u591c\u7a7a\u306b\u5bb9\u8d66\u306a\u304f\u964d\u308b\u9283\u5f3e"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Bangkok Thailand"
        },
        {
            "primary_geo": "Monarch Beach, CA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "(Daniel Woodrum)"
        },
        {
            "primary_geo": "Los Angeles, California"
        },
        {
            "primary_geo": "United States of America "
        },
        {
            "primary_geo": "\ud83c\uddfa\ud83c\uddf8"
        },
        {
            "primary_geo": "Santa Monica, CA"
        },
        {
            "primary_geo": "NYC \u2022 SF \u2022 LA \u2022 UK \u2022 HIGH"
        },
        {
            "primary_geo": "seoul"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Brian@socialstartnow.com"
        },
        {
            "primary_geo": "The interwebs"
        },
        {
            "primary_geo": "\u6771\u4eac \u845b\u98fe\u533a"
        },
        {
            "primary_geo": "West Hollywood"
        },
        {
            "primary_geo": "Montreal"
        },
        {
            "primary_geo": "Saint-Denis, France"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Fairborn, Ohio"
        },
        {
            "primary_geo": "\u305d\u308c\u3068\u6226\u3046\u52c7\u6c17\u304c\u307b\u3057\u3044\u3093\u3060\u3002"
        },
        {
            "primary_geo": "Long Beach, CA"
        },
        {
            "primary_geo": "Catalonia"
        },
        {
            "primary_geo": "Coventry RI USA"
        },
        {
            "primary_geo": "Nairobi, Kenya"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "In the clouds"
        },
        {
            "primary_geo": "Bogor, Jawa Barat"
        },
        {
            "primary_geo": "Chicago"
        },
        {
            "primary_geo": "California Non-Metro"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Sachsen"
        },
        {
            "primary_geo": "Doylestown"
        },
        {
            "primary_geo": "\u5922\u304c\u3042\u308b\u304b\u3089\u50d5\u306e\u547d\u306f\u8f1d\u304f\u3093\u3060"
        },
        {
            "primary_geo": "Cagliari Sardinya Italy"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Muskegon, Mi"
        },
        {
            "primary_geo": "\u65e5\u672c \u5927\u962a"
        },
        {
            "primary_geo": "Ventura, CA & the World"
        },
        {
            "primary_geo": "Redding California"
        },
        {
            "primary_geo": "Terrassa, Barcelona"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Colorado, USA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "Wayne, PA"
        },
        {
            "primary_geo": "Pau, France"
        },
        {
            "primary_geo": "Avoca, PA"
        },
        {
            "primary_geo": "INSOMNIA TRAIN   in\u718a\u672c"
        },
        {
            "primary_geo": "#Florida #LoveFL #VisitFlorida #California"
        },
        {
            "primary_geo": "\u304f\u3089\u3048\u50d5\u306e\u30ab\u30a4\u30b7\u30f3\u306e\u4e00\u6483"
        },
        {
            "primary_geo": "Internet"
        },
        {
            "primary_geo": "Per\u00fa"
        },
        {
            "primary_geo": "Salt Lake City"
        },
        {
            "primary_geo": "Spliffs, VA USA"
        },
        {
            "primary_geo": "Illinois, USA"
        },
        {
            "primary_geo": "Chicago"
        },
        {
            "primary_geo": "Kentucky, USA"
        },
        {
            "primary_geo": "Albertville, AL"
        },
        {
            "primary_geo": "Arizona, USA"
        },
        {
            "primary_geo": "SEKAI NO OWARI"
        },
        {
            "primary_geo": "\u81ea\u5ba4"
        },
        {
            "primary_geo": "\u307f\u3063\u304d\u3043"
        },
        {
            "primary_geo": "LEEDS UNITED KINGDOM"
        },
        {
            "primary_geo": "\u5bae\u57ce"
        },
        {
            "primary_geo": "Detroit, MI"
        },
        {
            "primary_geo": "\u4e8c\u6b21\u5143(\u9858\u671b)"
        },
        {
            "primary_geo": "Ft. Lauderdale, Estados Unidos"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "OBX, USA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "TOKYO\u3068\u30bd\u30a6\u30eb\u306e\u72ed\u9593"
        },
        {
            "primary_geo": "War Zone"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "\u6a2a\u6d5c\u3068\u5ddd\u5d0e\u306e\u9593"
        },
        {
            "primary_geo": "USA"
        },
        {
            "primary_geo": "Saint James New York"
        },
        {
            "primary_geo": "Maryland, USA"
        },
        {
            "primary_geo": "South Carolina, USA"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "La Plata Buenos Aires Arg."
        },
        {
            "primary_geo": "Next\u25b7\u25b6\ufe0e\u25b7\u25b6\ufe0eJuly 28th"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "fukuoka japan"
        },
        {
            "primary_geo": "Washington, USA"
        },
        {
            "primary_geo": "Somewhere Out There"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "\u65e5\u672c \u5343\u8449"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "1600 W Slauson Ave P20\nLos Angeles, California"
        },
        {
            "primary_geo": "San Diego, CA"
        },
        {
            "primary_geo": "Long Beach, CA"
        },
        {
            "primary_geo": "Coral Springs, FL - USA"
        },
        {
            "primary_geo": "Briga novarese"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Nijmegen"
        },
        {
            "primary_geo": "\uff8a\uff8f\uff8f\uff82\u261e\uff82\uff78\uff8a\uff9e"
        },
        {
            "primary_geo": "Tiruchirapalli, India"
        },
        {
            "primary_geo": "clubEARTH"
        },
        {
            "primary_geo": "Inside Destiny"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Mainz | Wei\u00dfenfels"
        },
        {
            "primary_geo": "SAN FRANCISCO"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "North Carolina, USA"
        },
        {
            "primary_geo": "INSOMNIA TRAIN\u4f59\u97fb\u3069\u3053\u308d\u3058\u3083\u306a\u3044\u3002"
        },
        {
            "primary_geo": "Fresno, CA"
        },
        {
            "primary_geo": "St. Petersburg, FL "
        },
        {
            "primary_geo": "New Jersey, USA"
        },
        {
            "primary_geo": "Neuilly-sur-Seine, France"
        },
        {
            "primary_geo": "\ud83c\udf38"
        },
        {
            "primary_geo": "SEKAI NO OWARI"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "Antioch, California"
        },
        {
            "primary_geo": "Milano"
        },
        {
            "primary_geo": "Madrid, Espa\u00f1a"
        },
        {
            "primary_geo": "Brooklyn"
        },
        {
            "primary_geo": "Opinions are my own."
        },
        {
            "primary_geo": "Houston, TX"
        },
        {
            "primary_geo": "New Orleans, LA"
        },
        {
            "primary_geo": "Tokyo"
        },
        {
            "primary_geo": "Av. Paseo del Esp\u00edritu Santo."
        },
        {
            "primary_geo": "\u3072\u3084\u3057\u3093\u3059"
        },
        {
            "primary_geo": "Tampico, Tamaulipas"
        },
        {
            "primary_geo": "New"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "California"
        },
        {
            "primary_geo": "moyassion in\u3082\u3084\u3057\u540c\u76df"
        },
        {
            "primary_geo": "Laredo \u2708\ufe0f kyle TX"
        },
        {
            "primary_geo": "Ratingen, Deutschland"
        },
        {
            "primary_geo": "\u0423\u043a\u0440\u0430\u0457\u043d\u0430"
        },
        {
            "primary_geo": "Austria"
        },
        {
            "primary_geo": "Cedar Hill, TX"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Austin, TX"
        },
        {
            "primary_geo": "Huntsville, OH"
        },
        {
            "primary_geo": "Tulum MX"
        },
        {
            "primary_geo": "Fort Lauderdale, FL"
        },
        {
            "primary_geo": "Bama"
        },
        {
            "primary_geo": "Bekasi City- Indonesia"
        },
        {
            "primary_geo": "Teterow, Anklam, Deutschland, Selbst\u00e4ndig | J"
        },
        {
            "primary_geo": "CA and NV"
        },
        {
            "primary_geo": "Los Angeles, California"
        },
        {
            "primary_geo": "South of Hell w/TRump in offic"
        },
        {
            "primary_geo": "SEKAI NO OWARI"
        },
        {
            "primary_geo": "North San Francisco Bay"
        },
        {
            "primary_geo": "YOKOHAMA"
        },
        {
            "primary_geo": "Saint Louis"
        },
        {
            "primary_geo": "\u3075\u304b\u305b\u3055\u3093\u3068\u3055\u304a\u308a\u3061\u3083\u3093\u3068\u306a\u304b\u3058\u3093\u3068\u3089\u3076\u3055\u3093"
        },
        {
            "primary_geo": "Anaheim"
        },
        {
            "primary_geo": "Niles, IL"
        },
        {
            "primary_geo": "San Jose, CA"
        },
        {
            "primary_geo": "Dhaka, Bangladesh"
        },
        {
            "primary_geo": "Caracas"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "Deutschland"
        },
        {
            "primary_geo": "Oklahoma, USA"
        },
        {
            "primary_geo": "Yorkshire, England"
        },
        {
            "primary_geo": "Estonia Tartu"
        },
        {
            "primary_geo": "Owerri, Nigeria"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Florida, USA"
        },
        {
            "primary_geo": "\u82b1\u304c\u53eb\u3076\u611b\u306e\u4e16\u754c"
        },
        {
            "primary_geo": "Lafayette, LA"
        },
        {
            "primary_geo": "New York baby\u270c\ufe0f"
        },
        {
            "primary_geo": "Texas"
        },
        {
            "primary_geo": "United Kingdom"
        },
        {
            "primary_geo": "San Jose California "
        },
        {
            "primary_geo": "San Francisco, CA"
        },
        {
            "primary_geo": "Niort, France"
        },
        {
            "primary_geo": "San Francisco"
        },
        {
            "primary_geo": "AZ, CA, NJ, TX"
        },
        {
            "primary_geo": "Cincinnati, OH"
        },
        {
            "primary_geo": "\u3042\u3060\u540d\u21aa\ufe0e\u304a\u304a\u305b\u3053"
        },
        {
            "primary_geo": "cedar city utah"
        },
        {
            "primary_geo": "Las Vegas, NV, USA"
        },
        {
            "primary_geo": "Southern California"
        },
        {
            "primary_geo": "Fort Myers, FL"
        },
        {
            "primary_geo": "Westwood, Los Angeles"
        },
        {
            "primary_geo": "\"\u3082\u3046\u4e00\u5ea6\u9023\u308c\u3066\u884c\u3063\u3066\u3042\u306e\u4e16\u754c\u3078\""
        },
        {
            "primary_geo": "Toronto, Ontario, Canada."
        },
        {
            "primary_geo": "Menasha, WI"
        },
        {
            "primary_geo": "Manhattan Beach, CA"
        },
        {
            "primary_geo": "\u3044\u305a\u308c\u306f\u5168\u3066\u5931\u3046\u306e\u306b\u3069\u3046\u3057\u3066\u5927\u5207\u306a\u30e2\u30ce\u306f\u5897\u3048\u3066\u3044\u304f\u306e\uff1f"
        },
        {
            "primary_geo": "Cardiff"
        },
        {
            "primary_geo": "Planet Earth"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Panam\u00e1"
        },
        {
            "primary_geo": "worldwide"
        },
        {
            "primary_geo": "\u897f\u91ce\u5bb6\ud83d\udc31\u30fb\u30bb\u30ab\u30aa\u30ef\u30cf\u30a6\u30b9\ud83c\udf33"
        },
        {
            "primary_geo": "Down Town LA"
        },
        {
            "primary_geo": "Golden, CO"
        },
        {
            "primary_geo": "Minnesota, USA"
        },
        {
            "primary_geo": "IBU \u793e\u5b66"
        },
        {
            "primary_geo": "westcoast"
        },
        {
            "primary_geo": "Arizona, USA"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "SJK"
        },
        {
            "primary_geo": "Santa Monica, CA"
        },
        {
            "primary_geo": "Mexico City"
        },
        {
            "primary_geo": "\u3072\u3088\u308a\ud83d\udc23"
        },
        {
            "primary_geo": "Santa Monica, CA"
        },
        {
            "primary_geo": "Wakanda"
        },
        {
            "primary_geo": "Columbia, MO"
        },
        {
            "primary_geo": "Estados Unidos"
        },
        {
            "primary_geo": "Rio de Janeiro, Brasil"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Tennessee, USA"
        },
        {
            "primary_geo": "www.soundcloud.com/codyslot"
        },
        {
            "primary_geo": "\uff7e\uff76\uff75\uff9c\u3001\uff79\uff9e\uff7d\u6975\u3001amazarashi"
        },
        {
            "primary_geo": "Corporate Offices - CA & NV"
        },
        {
            "primary_geo": "Texas, USA"
        },
        {
            "primary_geo": "\u4f55\u5e74\u30de\u30a4\u30af\u30e9\u3084\u3063\u3066\u3093\u3060\uff01"
        },
        {
            "primary_geo": "Kansas, USA"
        },
        {
            "primary_geo": "\u8679\u306e\u8fbf\u308a\u7740\u3044\u305f\u6240\u306e\u5de8\u5927\u6a39\u306e\u4e0b\ud83c\udf08\ud83c\udf32"
        },
        {
            "primary_geo": "\u30ac\u30ea\u30a8\u30eb\u5cf6\u3042\u3079\u3093\u6751   \u904a\u3073\u968a"
        },
        {
            "primary_geo": "\u30c1\u30fc\u30d0\u304f\u3093\u306e\u304a\u9f3b  \u91a4\u6cb9\u306e\u8857"
        },
        {
            "primary_geo": "Long Island"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "Roseville, CA"
        },
        {
            "primary_geo": "San Diego, CA"
        },
        {
            "primary_geo": "Deutschland"
        },
        {
            "primary_geo": "Valencia, Espa\u00f1a"
        },
        {
            "primary_geo": "There's no place like home \ud83c\udf2a"
        },
        {
            "primary_geo": "Sunnyvale, CA"
        },
        {
            "primary_geo": "SVA\u306e\u4eba(\u4eee)"
        },
        {
            "primary_geo": "North Hollywood, California "
        },
        {
            "primary_geo": "Serbia"
        },
        {
            "primary_geo": "Whiting Indiana"
        },
        {
            "primary_geo": "\u65e5\u672c \u6771\u4eac"
        },
        {
            "primary_geo": "\u308b\u3068\u3074\u4e2d\u5fc3\u306e\u751f\u6d3b\ud83d\udc39\u26a1\ud83d\udc9b"
        },
        {
            "primary_geo": "Gij\u00f3n, Espa\u00f1a"
        },
        {
            "primary_geo": "PS   Paris17"
        },
        {
            "primary_geo": "Chennai"
        },
        {
            "primary_geo": "Memphis Tn-California"
        },
        {
            "primary_geo": "Florida, USA"
        },
        {
            "primary_geo": "Minneapolis, MN"
        },
        {
            "primary_geo": "Toronto - New York - LA"
        },
        {
            "primary_geo": "1123 Hudson St Hoboken NJ"
        },
        {
            "primary_geo": "NEXT\u9999\u6e2f(\u30b7\u30f3\u30ac\u30dd\u30fc\u30eb)\u30d6\u30ec\u30fc\u30e1\u30f3\u3001\u30d5\u30a1\u30f3\u30af\u30e9\u30d6LIVE"
        },
        {
            "primary_geo": "here and there"
        },
        {
            "primary_geo": "INSOMNIA TRAIN"
        },
        {
            "primary_geo": "Dallas, Texas"
        },
        {
            "primary_geo": "Riverdale, GA"
        },
        {
            "primary_geo": "Texas\ud83d\udcab utah "
        },
        {
            "primary_geo": "Westwood, CA"
        },
        {
            "primary_geo": "Los Angeles"
        },
        {
            "primary_geo": "Maryland"
        },
        {
            "primary_geo": "United States"
        },
        {
            "primary_geo": "#ATL #Orlando #Tampa"
        },
        {
            "primary_geo": "Florida, USA"
        },
        {
            "primary_geo": "Songkhla"
        },
        {
            "primary_geo": "BRONX, NY"
        },
        {
            "primary_geo": "\u30e9\u30d5\u30ec\u30b7\u30a2\u306e\u3088\u3046\u306b\u8a98\u3044\u8fbc\u307f"
        },
        {
            "primary_geo": "Illinois, USA"
        },
        {
            "primary_geo": "Eastbourne, UK"
        },
        {
            "primary_geo": "Per\u00f9"
        },
        {
            "primary_geo": "Vi\u00f1a del Mar, Chile"
        },
        {
            "primary_geo": "Capitol Heights Side"
        },
        {
            "primary_geo": "art and design"
        },
        {
            "primary_geo": "United Kingdom"
        },
        {
            "primary_geo": "Royal Oak, Michigan"
        },
        {
            "primary_geo": "Newport Beach, CA"
        },
        {
            "primary_geo": "San Diego, CA"
        },
        {
            "primary_geo": "Ann Arbor, Michigan"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "London, England"
        },
        {
            "primary_geo": "Madrid, Espa\u00f1a"
        },
        {
            "primary_geo": "Feliz y optimista"
        },
        {
            "primary_geo": "Dublin, Ireland"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "West Covina, CA"
        },
        {
            "primary_geo": "Chicago, New York, FL, CA"
        },
        {
            "primary_geo": "Oakdale, CA"
        },
        {
            "primary_geo": "Capitol Heights, MD"
        },
        {
            "primary_geo": "DN."
        },
        {
            "primary_geo": "Calgary"
        },
        {
            "primary_geo": "Lincs"
        },
        {
            "primary_geo": "Colorado, USA"
        },
        {
            "primary_geo": "Worldwide"
        },
        {
            "primary_geo": "USA"
        },
        {
            "primary_geo": "California, USA"
        },
        {
            "primary_geo": "Venezuela"
        },
        {
            "primary_geo": "\ubc30\uad6c @Sure_VolleyB \ud50c\ud14d @Sure_talk"
        },
        {
            "primary_geo": "Canada"
        },
        {
            "primary_geo": "Find me on Amazon goo.gl/RBMwuK"
        },
        {
            "primary_geo": "JAXON drums YYZ by RUSH below."
        },
        {
            "primary_geo": "\u00d4saka"
        },
        {
            "primary_geo": "San Diego, CA"
        },
        {
            "primary_geo": "South Florida"
        },
        {
            "primary_geo": "Palm Springs, CA"
        },
        {
            "primary_geo": "El Paso, TX"
        },
        {
            "primary_geo": "\u672d\u5e4c"
        },
        {
            "primary_geo": "Van Nuys, CA"
        },
        {
            "primary_geo": "USA"
        },
        {
            "primary_geo": "859 Rt 25 Wentworth, NH USA"
        },
        {
            "primary_geo": "Planet Earth "
        },
        {
            "primary_geo": "Venezuela"
        },
        {
            "primary_geo": "Chicago, IL"
        },
        {
            "primary_geo": "\ud83c\uddea\ud83c\uddf8"
        },
        {
            "primary_geo": "Puerto Rico, USA"
        },
        {
            "primary_geo": "Gulf Shores, Alabama"
        },
        {
            "primary_geo": "Washington DC"
        },
        {
            "primary_geo": "Sacramento, CA"
        },
        {
            "primary_geo": "London"
        },
        {
            "primary_geo": "San Jose, Cali\u2600"
        },
        {
            "primary_geo": "Where the Wild Things Are"
        },
        {
            "primary_geo": "Instagram: Realhunedp"
        },
        {
            "primary_geo": "Fresno, CA"
        },
        {
            "primary_geo": "Havana, Cuba"
        },
        {
            "primary_geo": "LOS ANGELES"
        },
        {
            "primary_geo": "Sacramento, California"
        },
        {
            "primary_geo": "Los Angeles, CA"
        },
        {
            "primary_geo": "Alberta, Canada"
        },
        {
            "primary_geo": "Hawaii, USA"
        }
    ]

# CALIFORNIA
'''
tf.idf calc
'''
# Inputs:
dict_file = "../data_California/tweets_geo.json"
extent_file = "../data_LiesPeopleTellThemselves/output_ordinates.json"

def calc_scoring(tweet_string, the_longitude, the_latitude):
	# open processed file
	# f = open(dict_file, 'r')

	# assign tf-idf scores
	vectorizer = TfidfVectorizer()
	m = vectorizer.fit_transform(the_tweets_geo)

	# create dictionary of unique int_id, weight pairs
	# TODO: don't need following?
	# uniqueScores = {}
	# cm = scipy.sparse.coo_matrix(m)
	# for i,j,v in zip(cm.row, cm.col, cm.data):
	#     uniqueScores[j] = v

	# get list of words by id
	vocab = vectorizer.get_feature_names()

	# test tweet analysis
	tweet = tweet_string
	a = vectorizer.build_analyzer()
	aTweet = a(tweet)

	score = 0
	for tWord in aTweet:
	    for i, vWord in enumerate(vocab):
	        if(tWord == vWord):
	            score += 1
	print("Tweet score:", score)

	'''
	extent calc
	'''

	'''
	Declare consts
	'''
	max_l2 = float('-inf')
	min_l2 = float('inf')
	num_data = 100
	mu_long = -117.1825381
	sigma = 4
	# longitudes = np.random.normal(mu_long, sigma, num_data)
	longitudes = list()


	mu_lat = 34.0555693
	sigma = 4
	# latitudes = np.random.normal(mu_lat, sigma, num_data)
	latitudes = list()

	avg_longitude = 0.0
	avg_latitude = 0.0

	'''
	Read in from output_coordinates
	'''
	# file_path = extent_file
	# json_data=open(file_path).read()
	data = the_tweets_geo_extent
	for item in data:
		print(item)
		if item['latitude'] != None and item['longitude'] != None:
			# print("lat:"+str(item['latitude'])+"long:"+str(item['longitude']))
			latitudes.append(item['latitude'])
			longitudes.append(item['longitude'])

	# for item in range(len(latitudes)):
	# 	print("@@@"+str(latitudes[item])+" " + str(longitudes[item]))
	'''
	Normalize score between 0 and 1
	'''
	def normalized(x, min_x, max_x):
		return (x-min_x)/(max_x-min_x)

	def l2norm(x, y):
		return math.pow(math.pow(x-avg_longitude,2.0) + math.pow(y-avg_latitude,2.0), 0.5)



	for i in range(num_data):
		avg_longitude = (avg_longitude * i + longitudes[i])/(i+1)
		avg_latitude = (avg_latitude * i + latitudes[i])/(i+1)

	print("avg_longitude:"+str(avg_longitude))
	print("avg_latitude:"+str(avg_latitude))

	# find min/max l2 norm to centroid
	for i in range(num_data):
		if l2norm(longitudes[i],latitudes[i]) > max_l2:
			max_l2 = l2norm(longitudes[i],latitudes[i]);
		if l2norm(longitudes[i],latitudes[i]) < min_l2:
			min_l2 = l2norm(longitudes[i],latitudes[i]);


	# '''
	# test 1
	# similar latitude and longitudes:
	# '''

	# long_test1 = -100.0
	# lat_test1 = 50.0

	# l2_test1 = l2norm(long_test1,lat_test1)
	# print("normalized score for test 1: " + str(normalized(l2_test1, min_l2, max_l2)))

	# '''
	# test2
	# very different latitude and longitude:
	# '''


	# long_test2 = 50.0
	# lat_test2 = -100.0

	# l2_test2 = l2norm(long_test2,lat_test2)
	# print("normalized score for test2: " + str(normalized(l2_test2, min_l2, max_l2)))


	'''not a test'''


	long_test3 = the_longitude
	lat_test3 = the_latitude

	l2_test3 = l2norm(long_test3,lat_test3)
	print("normalized score for test2: " + str(normalized(l2_test3, min_l2, max_l2)))


calc_scoring("something something California", -117.182541, 34.055569)