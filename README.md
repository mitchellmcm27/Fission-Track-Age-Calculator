# Fission-Track-Age-Calculator
Calculates fission track ages (mainly for apatite)

## Calculating Single Grain Ages

Single grain fission track ages in the FTAC are calculated as described by Hasebe (2004).
 
The general age equation is:
$$D_t=\frac{\lambda_f}{\lambda_d}N_{238}\Big[e^{\lambda_Dt}-1\Big]$$
Where $D_t$ is the number of decay events of 238U for time $t$ in a unit volume, $\lambda_f$ is the spontaneous 238U fission decay constant, $\lambda_d$ is the 238U total decay constant (essentially just the alpha-decay constant), $N_{238}$ is the number of 238U atoms in a unit volume, and $t$ is the apparent fission track age in years.

However, because the number of decay events is record by the observed spontaneous track density:

$$\rho=\frac{\lambda_f}{\lambda_d}N_{238}\Big[e^{\lambda_dt}-1\Big]Rq$$
Where $\rho$ is the spontaneous track density (defined as $\rho=N_s/A$ where $N_s$ is the number of counted tracks of unit area $A$) , $R$ is the etchable track range of a fission fragment (generally taken as half the confined track length), and $q$ is the detection efficiency---an etchant factor defined as the fraction of etched fission tracks intersecting the counting surface that are accounted for by the system. $N_{238}$ is calculated by using the content of uranium collected by the LA-ICP-MS following:

$$N_{238} = \frac{No \ C_U \ d}{M_{238U}}$$
Where $No$ is Avogadro's number, $C_U$ is the concentration of 238U (ppm) as measured by the ICP-MS, $d$ is the density of the mineral (apatite), and $M_{238U}$ is the atomic mass of 238U.

The final equation with respect to time becomes:
$$t=\frac{1}{\lambda_d}\ln\Bigg[1+\lambda_d \ \xi \ \frac{\rho}{C_U}\Bigg] \ \Longrightarrow \ \xi=\frac{M_{238U}}{\lambda_{f} \ No \ d \ R \ q}$$
Where, $M_{238U}$ is the atomic mass of 238U, $No$ is Avogadro's number, $d$ is the density of the mineral, $R$ is the etchable range of one fission fragment (generally taken as half the confined track length $l_0/2$), and $q$ is the detection efficiency factor.  Where the aggregate factor $\xi$ is made up of $M_{238U}$, $\lambda_{f} $, $No$, $d$, $R$ and $q$ previously defined variables.

To calculate the single grain age standard error ($\sigma\left[t\right]$):
$$\sigma\left[t\right] = t\sqrt{\frac{1}{N_s}+\left[\frac{\sigma[C_U]}{[C_U]}\right]^2}$$
Where, $N_s$ is the counted track density at the mineral surface $\sigma[C_U]$ is the propagated uncertainty of the 238U measurement and $C_U$ is the 238U measurement.

It becomes apparent in the age equation that when the track density $d$ = 0, the age is mathematically not resolvable. However, this is not true geologically and has been referred to as the "zero tracks" problem (e.g., Vermeesch, 2017).  In the past, for External Detector Method dating, one could add a half count (0.5) to the spontaneous and induced tracks to solve the problem. For the LA-ICP-MS dating method, the concentration of U is measured directly and does not require an induced track count; therefore this simple solution does not work. The solution to this problem is beyond the scope of this github, however it effectively relies on recasting the LA-ICP-MS age equation into an "EDM-like" form, the full details of which can be found in Vermeesch, (2017). Here a simplified version has been developed using $\xi$ over $\zeta$ and assuming: 1) There are no uncertainties associated with $\xi$ and 2) The grains a homogenous in 238U implying that one laser spot per grain is sufficient. This would not be used until later steps in the FTAC however it's better to introduce it now alongside the "normal" age equation.

Here, what the FTAC does in later steps is use a simple "if" statement to divert the single grain age equation from the one described above to the one described in Vermeesch (2017) if the track density $N_s$ is = 0.

The single grain age equation then becomes as follows when $N_s=0$
$$t_0=\frac{1}{\lambda_d}\ln\Bigg[1+\lambda_d \ \xi \ \rho_i \frac{N_s + 0.5}{N_i + 0.5}\Bigg]$$
Where $t_0$ is the single grain age for 0-track grains and $N_i$ is the EDM-like induced track count (calculated below).

$\rho_i$ converts the (log)normal distributed 238U measurement into a Poisson distributed EDM-like equivalent induced count over area $A$:
$$\rho_i=\frac{C_U}{A} \ \sigma[C_U]^2$$

And $N_i$ is simply:
$$N_i=\Bigg[\frac{C_U}{\sigma[C_U]}\Bigg]^2$$

Finally, in order to calculate the single grain age uncertainties associated with zero-track grains ( $\sigma\left[t_0\right]$ ), assuming there's no error associated with $\xi$:
$$\sigma\left[t_0\right]=t\Bigg[\frac{1}{N_s+0.5}+\frac{1}{N_i+0.5}\Bigg]^2$$

## Calculating Pooled and Central ages

Equation used to calculate the AFT pooled age modified after Donelick (2005), Hasebe (2004):
$$t_{pooled} = \frac{1}{\lambda_d} \ln\Bigg[1 + \xi \lambda_d \frac{ \sum\limits_{j}^{n} N_{sj}} { \sum\limits_{j}^{n} C_{Uj} A_j}\Bigg]$$


And to then calculate 1-sigma error, rearranged after Hasebe (2004):
$$\sigma_{pooled} = \frac{\sqrt{\sum\limits_{j}^{n}\Big[t_j - t_{pooled}\Big]^2 f(t_k)}}{\sqrt{n-1}}$$

Where $n$ is the number of grains counted in total and $f(t_k), f(t_j)$ are calculated as follows:
$$f(t_k) = \frac{f(t_j)}{\sum\limits_{j}^{n}f(t_j)}$$

and
$$f(t_j) =\Bigg[\frac{1}{\sqrt{2\pi} \Big(\frac{ \sigma\left[t_j\right]}{t_j}\Big)}\Bigg]$$


Following the calculation of the pooled ages and pooled age errors, the commonly used $\chi^2$ is calculated after Vermeesch (2017).

$$\chi^{2}_{stat} = \sum\limits_{j}^{n}\Big(\frac{z_j}{s_j}\Big)^2 - \frac{\Big[\sum\limits_{j}^{n} \Big(\frac{z_j}{s_j^2}\Big)\Big]^2}{\sum\limits_{j}^{n}\Big(\frac{1}{s_j^2}\Big)}$$

where
$$z_j = \ln\Big({t_j}\Big)$$

and
$$s_j =\frac{\sigma\left[t_j\right]}{t_j}$$


To calculate probability of null hypothesis given $\chi^2$ value (the $P(\chi^2)$ ), the FTAC takes use of a python package from scipy. The output is in percentage: 
$$P(\chi^2) = stats.chi2.sf(\chi^2, n-1)100$$



The central age is calculated after Galbraith (2005) using the Newton-Raphson method of approximation. The included script to calculate the central age is included in age is included in the files. The script was adapted from a VBA script previously developed for use in our lab by Christian Seiler.

## Estimating rmr0 from Dpar, calculating eCl

The FTAC will attempt to estimate the rmr0 from the measured Dpar values either by way of Ketcham (2007) or by Carlson (1999), Ketcham (1999) depending on multiple selections in step 2); a combination of the etchant used and the preferred model.

Estimated using the Ketcham (2007) For apatites etched with 5.0M HNO3:
$$r_{mr0D_{5.0}} = 0.84\left[\frac{4.58-(0.9231D_{par} + 0.2515)}{2.98}\right]^{0.21}$$

Estimated using the Carlson (1999), Ketcham (1999) For apatites etched with 5.0M HNO3:
$$r_{mr0D_{5.0}} = 1-exp\Big[0.647\left[(0.9231D_{par}+0.2515)-1.75\right]-1.834\Big]$$

Estimated using the Ketcham (2007) For apatites etched with 5.5M HNO3:
$$r_{mr0D_{5.5}} = 0.84\left[\frac{4.58-D_{par}}{2.98}\right]^{0.21}$$


Estimated using the Carlson (1999), Ketcham (1999) For apatites etched with 5.5M HNO3:
$$r_{mr0D_{5.5}} = 1-exp\Big[0.647(D_{par}-1.75)-1.834\Big]$$

The FTAC will estimate rmr0 from Dpar for both the FT Age results and FT length results. Estimating rmr0 for the age results is useful for comparison when rmr0 is measured by EPMA directly. For the length results, estimating rmr0 becomes crucial for modeling if rmr0 is measured directly for the age results yet not for the length results. 

Individual single grain rmr0's are normally calculated following one of two models.

The rmr0 model after Carlson (1999):

$$r_{mr0} = \Big[0.027 + 0.431\left|Cl-1\right| + 0.107 \left|OH-1\right| - 1.01Mn - 2.67Fe - 0.144Others\Big]^{0.25}$$
Where $Others$ is the sum of all cation substitutes except for Mn and Fe.

The rmr0 model after Ketcham (2007):
$$r_{mr0} = \Big[-0.0495 - 0.0348F + 0.3528\left|Cl-1\right| + 0.071 \left|OH-1\right| - 0.8592Mn - 1.2252Fe - 0.1721Others\Big]^{0.1433}$$
Where $Others$ is the sum of all cation substitutes except for Mn and Fe.

The FTAC does not calculate rmr0 directly. This is beyond the scope of the FTAC. However, the main differences between the Carlson (1999) and  Ketcham (2007) include the upper limits of each (0.84 for the Carlson (1999) model and 0.83 for the Ketcham (2007a) model) and the general spread in rmr0 has been noted to be larger using the Carlson (1999) model. What the FTAC does calculate using the rmr0 is the "effective Cl" (eCl) content in atoms per formula unit (apfu) using one of two equations. In this thesis, the model after Ketcham (2007) was used to calculate all rmr0 and eCl values.

Equation used to calculate eCl if rmr0 model is after Carlson (1999):
$$eCl =\frac{\ln(1-r_{mr0})+1.834}{2.107}$$

Equation used to calculate eCl if rmr0 model is after Ketcham (2007):
$$eCl  = 1-\left[\Big(\frac{r_{mr0}}{0.857015}\Big)^{(\frac{1}{0.23})}+0.13\right]$$

