from math import sin as sin
from math import cos as cos
from math import acos as acos
from math import pi as pi

# thing=raw_input('?')# raw data pasted by hand from http://www.infoplease.com/ipa/A0001769.html

# thing=thing.replace('\n','\t')
# thing=thing.split('\t')

# for x in range(len(thing)):
#     thing[x]=thing[x].replace(' ','')

thing=['Aberdeen,Scotland', '57', '9N', '2', '9W', '5:00p.m.',
      'Adelaide,Australia', '34', '55S', '138', '36E', '2:30a.m.1',
      'Algiers,Algeria', '36', '50N', '3', '0E', '6:00p.m.',
      'Amsterdam,Netherlands','52', '22N', '4', '53E', '6:00p.m.',
      'Ankara,Turkey', '39', '55N', '32', '55E', '7:00p.m.',
      'Asuncion,Paraguay', '25', '15S', '57', '40W', '1:00p.m.',
      'Athens,Greece', '37', '58N', '23', '43E', '7:00p.m.',
      'Auckland,NewZealand', '36', '52S', '174', '45E', '5:00a.m.1',
      'Bangkok,Thailand', '13', '45N', '100', '30E', 'midnight',
      'Barcelona,Spain', '41', '23N', '2', '9E', '6:00p.m.',
      'Beijing,China', '39', '55N', '116', '25E', '1:00a.m.1',
      'Belem,Brazil', '1', '28S', '48', '29W', '2:00p.m.',
      'Belfast,NorthernIreland', '54', '37N', '5', '56W', '5:00p.m.',
      'Belgrade,Serbia', '44', '52N', '20', '32E', '6:00p.m.',
      'Berlin,Germany', '52', '30N', '13', '25E', '6:00p.m.',
      'Birmingham,England', '52', '25N', '1', '55W', '5:00p.m.',
      'Bogota,Colombia', '4', '32N', '74', '15W', '12:00noon',
      'Bombay,India', '19', '0N', '72', '48E', '10:30p.m.',
      'Bordeaux,France', '44', '50N', '0', '31W', '6:00p.m.',
      'Bremen,Germany', '53', '5N', '8', '49E', '6:00p.m.',
      'Brisbane,Australia', '27', '29S', '153', '8E', '3:00a.m.1',
      'Bristol,England', '51', '28N', '2', '35W', '5:00p.m.',
      'Brussels,Belgium', '50', '52N', '4', '22E', '6:00p.m.',
      'Bucharest,Romania', '44', '25N', '26', '7E', '7:00p.m.',
      'Budapest,Hungary', '47', '30N', '19', '5E', '6:00p.m.',
      'BuenosAires,Argentina', '34', '35S', '58', '22W', '2:00p.m.',
      'Cairo,Egypt', '30', '2N', '31', '21E', '7:00p.m.',
      'Calcutta,India', '22', '34N', '88', '24E', '10:30p.m.',
      'Canton,China', '23', '7N', '113', '15E', '1:00a.m.1',
      'CapeTown,SouthAfrica', '33', '55S', '18', '22E', '7:00p.m.',
      'Caracas,Venezuela', '10', '28N', '67', '2W', '1:00p.m.',
      'Cayenne,FrenchGuiana', '4', '49N', '52', '18W', '2:00p.m.',
      'Chihuahua,Mexico', '28', '37N', '106', '5W', '10:00a.m.',
      'Chongqing,China', '29', '46N', '106', '34E', '1:00a.m.1',
      'Copenhagen,Denmark', '55', '40N', '12', '34E', '6:00p.m.',
      'Cordoba,Argentina', '31', '28S', '64', '10W', '2:00p.m.',
      'Dakar,Senegal', '14', '40N', '17', '28W', '5:00p.m.',
      'Darwin,Australia', '12', '28S', '130', '51E', '2:30a.m.1',
      'Djibouti,Djibouti', '11', '30N', '43', '3E', '8:00p.m.',
      'Dublin,Ireland', '53', '20N', '6', '15W', '5:00p.m.',
      'Durban,SouthAfrica', '29', '53S', '30', '53E', '7:00p.m.',
      'Edinburgh,Scotland', '55', '55N', '3', '10W', '5:00p.m.',
      'Frankfurt,Germany', '50', '7N', '8', '41E', '6:00p.m.',
      'Georgetown,Guyana', '6', '45N', '58', '15W', '1:00p.m.',
      'Glasgow,Scotland', '55', '50N', '4', '15W', '5:00p.m.',
      'GuatemalaCity,Guatemala', '14', '37N', '90', '31W', '11:00a.m.',
      'Guayaquil,Ecuador', '2', '10S', '79', '56W', '12:00noon',
      'Hamburg,Germany', '53', '33N', '10', '2E', '6:00p.m.',
      'Hammerfest,Norway', '70', '38N', '23', '38E', '6:00p.m.',
      'Havana,Cuba', '23', '8N', '82', '23W', '12:00noon',
      'Helsinki,Finland', '60', '10N', '25', '0E', '7:00p.m.',
      'Hobart,Tasmania', '42', '52S', '147', '19E', '3:00a.m.1',
      'HongKong,China', '22', '20N', '114', '11E', '1:00a.m.1',
      'Iquique,Chile', '20', '10S', '70', '7W', '1:00p.m.',
      'Irkutsk,Russia', '52', '30N', '104', '20E', '1:00a.m.',
      'Jakarta,Indonesia', '6', '16S', '106', '48E', 'midnight',
      'Johannesburg,SouthAfrica', '26', '12S', '28', '4E', '7:00p.m.',
      'Kingston,Jamaica', '17', '59N', '76', '49W', '12:00noon',
      'Kinshasa,Congo', '4', '18S', '15', '17E', '6:00p.m.',
      'KualaLumpur,Malaysia', '3', '8N', '101', '42E', '1:00a.m.1',
      'LaPaz,Bolivia', '16', '27S', '68', '22W', '1:00p.m.',
      'Leeds,England', '53', '45N', '1', '30W', '5:00p.m.',
      'Lima,Peru', '12', '0S', '77', '2W', '12:00noon',
      'Lisbon,Portugal', '38', '44N', '9', '9W', '5:00p.m.',
      'Liverpool,England', '53', '25N', '3', '0W', '5:00p.m.',
      'London,England', '51', '32N', '0', '5W', '5:00p.m.',
      'Lyons,France', '45', '45N', '4', '50E', '6:00p.m.',
      'Madrid,Spain', '40', '26N', '3', '42W', '6:00p.m.',
      'Manchester,England', '53', '30N', '2', '15W', '5:00p.m.',
      'Manila,Philippines', '14', '35N', '120', '57E', '1:00a.m.1',
      'Marseilles,France', '43', '20N', '5', '20E', '6:00p.m.',
      'Mazatlan,Mexico', '23', '12N', '106', '25W', '10:00a.m.',
      'Mecca,SaudiArabia', '21', '29N', '39', '45E', '8:00p.m.',
      'Melbourne,Australia', '37', '47S', '144', '58E', '3:00a.m.1',
      'MexicoCity,Mexico', '19', '26N', '99', '7W', '11:00a.m.',
      'Milan,Italy', '45', '27N', '9', '10E', '6:00p.m.',
      'Montevideo,Uruguay', '34', '53S', '56', '10W', '2:00p.m.',
      'Moscow,Russia', '55', '45N', '37', '36E', '8:00p.m.',
      'Munich,Germany', '48', '8N', '11', '35E', '6:00p.m.',
      'Nagasaki,Japan', '32', '48N', '129', '57E', '2:00a.m.1', 
      'Nagoya,Japan', '35', '7N', '136', '56E', '2:00a.m.1', 
      'Nairobi,Kenya', '1', '25S', '36', '55E', '8:00p.m.', 
      'Nanjing,China', '32', '3N', '118', '53E', '1:00a.m.1', 
      'Naples,Italy', '40', '50N', '14', '15E', '6:00p.m.', 
      'NewDelhi,India', '28', '35N', '77', '12E', '10:30p.m.', 
      'Newcastle-on-Tyne,England', '54', '58N', '1', '37W', '5:00p.m.', 
      'Odessa,Ukraine', '46', '27N', '30', '48E', '7:00p.m.', 
      'Osaka,Japan', '34', '32N', '135', '30E', '2:00a.m.1', 
      'Oslo,Norway', '59', '57N', '10', '42E', '6:00p.m.', 
      'PanamaCity,Panama', '8', '58N', '79', '32W', '12:00noon', 
      'Paramaribo,Suriname', '5', '45N', '55', '15W', '2:00p.m.', 
      'Paris,France', '48', '48N', '2', '20E', '6:00p.m.', 
      'Perth,Australia', '31', '57S', '115', '52E', '1:00a.m.1', 
      'Plymouth,England', '50', '25N', '4', '5W', '5:00p.m.', 
      'PortMoresby,PapuaNewGuinea', '9', '25S', '147', '8E', '3:00a.m.1', 
      'Prague,CzechRepublic', '50', '5N', '14', '26E', '6:00p.m.', 
      'Rangoon,Myanmar', '16', '50N', '96', '0E', '11:30p.m.', 
      'Reykjavik,Iceland', '64', '4N', '21', '58W', '5:00p.m.', 
      'RiodeJaneiro,Brazil', '22', '57S', '43', '12W', '2:00p.m.', 
      'Rome,Italy', '41', '54N', '12', '27E', '6:00p.m.', 
      'Salvador,Brazil', '12', '56S', '38', '27W', '2:00p.m.', 
      'Santiago,Chile', '33', '28S', '70', '45W', '1:00p.m.', 
      'St.Petersburg,Russia', '59', '56N', '30', '18E', '8:00p.m.', 
      'SaoPaulo,Brazil', '23', '31S', '46', '31W', '2:00p.m.', 
      'Shanghai,China', '31', '10N', '121', '28E', '1:00a.m.1', 
      'Singapore,Singapore', '1', '14N', '103', '55E', '1:00a.m.1', 
      'Sofia,Bulgaria', '42', '40N', '23', '20E', '7:00p.m.', 
      'Stockholm,Sweden', '59', '17N', '18', '3E', '6:00p.m.', 
      'Sydney,Australia', '34', '0S', '151', '0E', '3:00a.m.1', 
      'Tananarive,Madagascar', '18', '50S', '47', '33E', '8:00p.m.', 
      'Teheran,Iran', '35', '45N', '51', '45E', '8:30p.m.', 
      'Tokyo,Japan', '35', '40N', '139', '45E', '2:00a.m.1', 
      'Tripoli,Libya', '32', '57N', '13', '12E', '7:00p.m.', 
      'Venice,Italy', '45', '26N', '12', '20E', '6:00p.m.', 
      'Veracruz,Mexico', '19', '10N', '96', '10W', '11:00a.m.', 
      'Vienna,Austria', '48', '14N', '16', '20E', '6:00p.m.', 
      'Vladivostok,Russia', '43', '10N', '132', '0E', '3:00a.m.1', 
      'Warsaw,Poland', '52', '14N', '21', '0E', '6:00p.m.', 
      'Wellington,NewZealand', '41', '17S', '174', '47E', '5:00a.m.1', 
      'Zurich,Switzerland', '47', '21N', '8', '31E', '6:00p.m.']

# will clean this up later

def lat(a,b):
    if b[-1]=='N':
        return float(a)+float(b[:-1])/60.0
    elif b[-1]=='S':
        return -float(a)-float(b[:-1])/60.0
    else:
        return 'something went wrong'




def longi(a,b):
    if b[-1]=='E':
        return float(a)+float(b[:-1])/60.0
    elif b[-1]=='W':
        return -float(a)-float(b[:-1])/60.0
    else:
        return 'something went wrong'





def octopus(something): # local timezone
    if something=='12:00noon':
        return 12.0
    elif something=='midnight':
        return 0.0
    elif 'a' in something:
        banana=something.index(':')
        return float(something[:banana])+float(something[banana+1:banana+3])/60.0
    elif 'p' in something:
        banana=something.index(':')
        return float(something[:banana])+float(something[banana+1:banana+3])/60.0+12.0


class thingy:
    def __init__(self, place, lat, longi, time):
        self.place=place
        self.lat=lat
        self.longi=longi
        self.time=time


thingamabob=[]
for w in range(len(thing)/6):
    thingamabob.append(thingy(thing[6*w],lat(thing[6*w+1],thing[6*w+2]),longi(thing[6*w+3],thing[6*w+4],),octopus(thing[6*w+5])))




flightspeed=900 # customisable, do it later
currenttime=18 # customisable
currentlocation='London,England' # customisable
mcdonaldsopen=6 # NOT customisable. nowhere does mcdonalds have these before 6am. except victoria station
mcdonaldsclose=10.5 # nor this one. ever seen a mcdonalds breakfast available after half ten?


def distance(lat1, long1, lat2, long2): # distance in km between two points
    return 6371.01 * (acos((cos(lat1/180.0*pi) * cos(lat2/180.0*pi) * cos(long1/180.0*pi - long2/180.0*pi)) + (sin(lat1/180.0*pi) * sin(lat2/180.0*pi))))



def answer(lat1, long1, lat2, long2, currenttime, timezonehere, timezonethere, flightspeed):
    timediff=distance(lat1, long1, lat2, long2)/flightspeed
    arrivetime=(currenttime+timediff+timezonethere-timezonehere)%24
    if arrivetime>mcdonaldsopen and arrivetime<mcdonaldsclose:
        return timediff
    else:
        return (mcdonaldsopen-arrivetime)%24+timediff



for x in thingamabob:
    if x.place==currentlocation:
        lat1=x.lat
        long1=x.longi
        timezonehere=x.time

whatever=['blahblahblah',103]
for z in thingamabob:
    theanswer=answer(lat1, long1, z.lat, z.longi, currenttime, timezonehere, z.time, flightspeed)
    if theanswer<whatever[1]:
        whatever=[z.place,theanswer] # should return somewhere in russia for now

print "Your fastest route to a McDonald's Breakfast would be to go to", whatever[0], "and it will take you", whatever[1], "hours"
