from requests_html import HTMLSession
import json, time

def get_last_percentage_above_20D( symbol):
    """
    COM = security("INDEX:SLTW", timeframe.period,close)
    CND = security("INDEX:SYTW", timeframe.period,close)
    CNS = security("INDEX:SPTW", timeframe.period,close)
    ENE = security("INDEX:SETW", timeframe.period,close)
    FIN = security("INDEX:SFTW", timeframe.period,close)
    HLT = security("INDEX:SVTW", timeframe.period,close)
    IND = security("INDEX:SITW", timeframe.period,close)
    MAT = security("INDEX:SBTW", timeframe.period,close)
    REI = security("INDEX:SSTW", timeframe.period,close)
    TEC = security("INDEX:SKTW", timeframe.period,close)
    UTL = security("INDEX:SUTW", timeframe.period,close)
    TTL=COM+CND+CNS+ENE+FIN+HLT+IND+MAT+REI+TEC+UTL
    TTLAV = TTL/11
    """
    session = HTMLSession()
    url     = 'https://www.barchart.com/stocks/quotes/$' + symbol + '/technical-chart?plot=BAR&volume=0&data=DO&density=X&pricesOn=1&asPctChange=0&logscale=0&sym=$MMTW&grid=1&height=500&studyheight=100'
    r       = session.get(url)
    r.html.render()

# with open('webcontent.html', 'w') as f:
    # json.dump(r.html.html, f)
    
    content = str(r.html.html)    
    keyword  = 'class=\"last-change\"'
    
    res = [i for i in range(len(content)) if content.startswith(keyword, i)] 
       
    subcontent = ''
    if( len(res) >= 2):
        subcontent = content[res[0]:res[1]]
    
    if (len( subcontent )>0):
        pos_tag_lastPrcie = [i for i in range(len(subcontent)) if subcontent.startswith('lastPrice', i)]
        pos_end_span = [i for i in range(len(subcontent)) if subcontent.startswith('</span>', i)]
        
        if( len( pos_end_span ) == 1 and len( pos_tag_lastPrcie ) == 1 ):
            lastPriceString = subcontent[pos_tag_lastPrcie[0]: pos_end_span[0]]
            
            if( len(lastPriceString ) > 0):
                pos_close_tag = [i for i in range(len(lastPriceString)) if lastPriceString.startswith('>', i)]
                
                if( len(pos_close_tag)==1 ):
                    print('Symbol: ', symbol, '-> ', lastPriceString[pos_close_tag[0]+1:])
        
print('Start at: ', time.time())

get_last_percentage_above_20D( 'SLTW' )
get_last_percentage_above_20D( 'SYTW' )
get_last_percentage_above_20D( 'SPTW' )
get_last_percentage_above_20D( 'SETW' )
get_last_percentage_above_20D( 'SFTW' )
get_last_percentage_above_20D( 'SVTW' )
get_last_percentage_above_20D( 'SITW' )
get_last_percentage_above_20D( 'SBTW' )
get_last_percentage_above_20D( 'SSTW' )
get_last_percentage_above_20D( 'SKTW' )
get_last_percentage_above_20D( 'SUTW' )
print('End at: ', time.time())
                                