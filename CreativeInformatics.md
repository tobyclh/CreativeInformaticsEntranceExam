## Problem 2  
1. $f(t) = F$  
$F - Mgsin(\theta) = net force$  
$velocity(t) = (F - Mgsin(\theta)) * t$  
$position(t) = (F - Mgsin(\theta)) * t^2/2$  

2. 




## Problem 3
1. Pipeline hazard  
    Pipeline hazard refers to situations that prevent the next __instruction__ from being carried out.
    There are three main types of hazard, including data hazard, control hazard and structural hazard.  
    1. __Data hazard__ is when data is dependent to each other.  
    A = B + 4  
    B = A + B  
    Second instruction is dependent on the first equation.
    2. __Structual Hazard__ occurs when 2 instructions requires a given hardware, for example, when 2 instructions requries accessing the same memory address.
    3. __Control Hazard__ occurs when branching, given 2 branches which the CPU does not know the outcome in advance, it cannot evaluate the consequence instructions before the branches outcome have been finalized.      
    
    Fixing pipeline hazard  
    1. __Data hazard__ can be eliminated with out-of-order execution, that is, uses the otherwise idle cycle to process instruction that is programmed to be executed later and free of dependency.
    2. __Structual Hazard__ can be fixed by programmer explicitly use different hardware resources. Or it can be done by duplicated certain resource.
    3. __Control Hazard__ can be elimiated using branch prediction, which make educated guess on which branch will be taken and act accordingly.      
2. Register renaming  
    Register renaming is a pipeline technique to eliminate WAR / WAW hazard. Architectural registers are a name/location pair with dynamic mapping that is editted as new instructions come in. Algorithms handling register renaming includes Tomasulo data structure.
3. Kalman Filter  
    Kalman filter is a classic optimization approach for estimating the true value of a variable through noisy observations through iterative sampling. At heart Kalman filter treats noise as an addictive Gaussian noise added to the true value observed. Kalman filter tries to estimate the mean and covarience of the gaussian noise using maximum likihood. It does so by comparing a newly observed sample with its' own prediction, and updating the prediction to describe such new sample "better".
4. Regular Lanaguage 
5. Public Key cryptography an certification authority 

