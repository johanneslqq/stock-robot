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
    url     = 'https://www.chartmill.com/stock/quote/$' + symbol + '/analyst-ratings'
    r       = session.get(url)
       
    r.html.render()

    
    content = str(r.html.html)    
    keyword  = '&nbsp;&nbsp;'
        
    res = [i for i in range(len(content)) if content.startswith(keyword, i)] 
    
     
     
    # with open('debug_2.html', 'w') as f:
        # json.dump(content, f)
        
    subcontent = ''
    if( len(res) == 3):
        subcontent = content[res[1]:res[2]]
        sub_str_arr = subcontent.split(' ')
        
        if(len(sub_str_arr) >= 2):
            print('Symbol: ', symbol, '-> ', sub_str_arr[1])
           
    # if (len( subcontent )>0):
        # price_end_pos   = [i for i in range(len(subcontent)) if subcontent.startswith('<span>', i)]
        # price_start_pos = [i for i in range(len(subcontent)) if subcontent.startswith(')', i)]
        
        # if( len( price_end_pos ) >= 1 and len( price_start_pos ) >= 1):
            # lastPriceString = subcontent[price_start_pos[0] + 1: price_end_pos[0]]
            # print('Symbol: ', symbol, '-> ', lastPriceString[pos_close_tag[0]+1:])

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