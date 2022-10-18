# %%
# coding: utf-8

# %%
import numpy as np

def CentralAge(grain_ids, sga_ma, sga_ma_err, pooled_ma):
    """Calculates the central age of scattered single grain data using Newton-Raphson method.
    See p.100 of Galbraith (2005) for more info.
    Thanks to Christian Seiler for the VBA script this followed."""
    muest = float()
    mu = float()
    dmu = float()
    si = float()
    dsi = float()
    su = float()
    zu = float()
    c = float()
    b = float()
    f = float()
    df = float()
    fsum = float()
    dfsum = float()
    num = float()
    numsum = float()
    denom = float()
    denomsum = float()
    i = int()
    x = int()
    n = int()
    u = int()
    it = int()
    muest = np.log(pooled_ma)
    mu = muest
    it = 20

    #determine initial si
    for x in range(1, 17):
        fsum = 0
        dfsum = 0
        
        #calculate sums of single grain f and df for Newton-Raphson method
        for n in range(0, grain_ids.count()):
            rsu= 0 + n
            su = (sga_ma_err/sga_ma)[rsu]#relative signle grain error
            if isinstance(su, float):
                zu = np.log(sga_ma)[rsu]#ln of sga
                c = zu-mu
                b = (si**2)+(su**2)
                f = (c**2)/(b**2)-1/b
                df = 1/(b**2)-(2*c**2)/(b**3)  
                
                fsum = fsum + f
                dfsum = dfsum + df

        dsi = si-(fsum/dfsum)
            
        if  (si/mu) >100:
            si=0
        else:
            si=dsi 

   
    #iterate mu
    for i in range(1,it):
        numsum=0
        denomsum=0
        
        for u in range(0, grain_ids.count()):
            rsu= 0 + u
            su = (sga_ma_err/sga_ma)[rsu]
            if isinstance(su, float):
                zu = np.log(sga_ma)[rsu]
                num = zu/(si**2+su**2)
                denom = 1/(si**2+su**2)
                numsum = numsum+num
                denomsum = denomsum+denom  
        dmu = numsum/denomsum
        mu=dmu
        

    #iterate si
        for x in range(1,it):
            fsum = 0
            dfsum = 0
        #calculate sums of single grain f and df for Newton-Raphson method
            for n in range(0, grain_ids.count()):
                rsu= 0 + n
                su = (sga_ma_err/sga_ma)[rsu]
                if isinstance(su, float):
                    zu = np.log(sga_ma)[rsu]
                    c = zu-mu
                    b = (si**2)+(su**2)
                    f = (c**2)/(b**2)-1/b
                    df = 1/(b**2)-(2*c**2)/(b**3)
                    fsum = fsum+f
                    dfsum = dfsum+df
                
            dsi = si-(fsum/dfsum )
            
            if si == 0:
                break
            elif np.abs((dsi-si)/si) < (10**(-5)):
                break
                
            if  (si/mu) >100:
                si=0
            else:
                si=dsi    
     #central age
    global Central_age, Central_age_1sigma, Dispersion
    Central_age = np.exp(mu)
    Central_age_1sigma = ((1/denomsum)**(0.5))*(np.exp(mu))
    Dispersion = 100*si
    
    return (Central_age, Central_age_1sigma, Dispersion)


