# Fission-Track-Age-Calculator
Calculates fission track ages (mainly for apatite)

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
