
The latest factoring (and discrete logarithm) records are depicted in Figure 2, culminating with the factorization of RSA-250 (a 829-bit composite number) in February 2020, for a computation cost of about 2,700 core-years.

These academic results are far from the limit of feasibility, especially for a state-level attacker. 
It is obvious that larger computations are possible, and it is widely accepted that 1024-bit factoring and discrete logarithm are feasible now, with hardware and software that currently exist.

A ballpark estimate is that factoring a 1024-bit key would be about 200 times harder than RSA-250, or around 500,000 core-years of computation.

[...]

Dealing with such a matrix would mobilize tens of thousands of CPU cores over several months, which is certainly feasible.

Source:
https://hal.science/hal-03691141/document

TLDR;
Based on this paper, breaking a 1024-bit key would take 500,000 core-years. That means that using a single core it would take 500,000 years. Using 500,000 cores it'd take one year.

If you want to rent servers to help you break one single 1024-bit RSA key, it would take you $38,000,000 and one year to crack, provided you rent from a service like [this](https://kingservers.com/en/intel-xeon-dedicated-servers/). Based on this, renting a 36 core server for one year cost about $2750.

Number of servers needed = (core years) / (no. cores of the server)

500,000 / 36 ≈ 13,889

2750*13,889 = $38,194,750

It would take around $38,194,750 to use a server hosting service to crack a single 1024-bit RSA key.
