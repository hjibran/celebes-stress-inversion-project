import numpy as np

#*************************************************************************#
#   function STRIKE_DIP_RAKE                                              #
#                                                                         #
#   calculation of strike, dip and rake from the fault normals and slip   #
#   directions                                                            #
#                                                                         #
#   input:  fault normal n                                                #
#           slip direction u                                              #
#                                                                         #
#   output: strike, dip and rake                                          #
#*************************************************************************#
def strike_dip_rake(n,u):

    n1 = n
    u1 = u
    	
    if (n1[3]>0): n1 = -n1; u1 = -u1; # vertical component is always negative!
            
    n2 = u
    u2 = n
        
    if (n2[3]>0): n2 = -n2; u2 = -u2;  # vertical component is always negative!
    
    ## ------------------------------------------------------------------------
    # 1st solution
    #--------------------------------------------------------------------------
    dip    = np.arccos(-n1[3])*180/np.pi
    strike = np.arcsin(-n1[1]/np.sqrt(n1[1]**2+n1[2]**2))*180/np.pi
    
    # determination of a quadrant
    if (n1[2]<0): strike=180-strike;
    
    rake = np.arcsin(-u1[3]/np.sin(dip*np.pi/180))*180/np.pi
    
    # determination of a quadrant
    cos_rake = u1[1]*np.cos(strike*np.pi/180)+u1[2]*np.sin(strike*np.pi/180)
    if (cos_rake<0): rake=180-rake;
    
    if (strike<0   ): strike = strike+360;
    if (rake  <-180): rake   = rake  +360;
    if (rake  > 180): rake   = rake  -360;  # rake is in the interval -180<rake<180
    
        
    strike1 = np.real(strike)
    dip1 = np.real(dip)
    rake1 = np.real(rake)
    
    ## ------------------------------------------------------------------------
    # 2nd solution
    #--------------------------------------------------------------------------
    dip    = np.arccos(-n2[3])*180/np.pi
    strike = np.arcsin(-n2[1]/np.sqrt(n2[1]**2+n2[2]**2))*180/np.pi
    
    # determination of a quadrant
    if (n2[2]<0): strike=180-strike;
    
    rake = np.arcsin(-u2[3]/np.sin(dip*np.pi/180))*180/np.pi
    
    # determination of a quadrant
    cos_rake = u2[1]*np.cos(strike*np.pi/180)+u2[2]*np.sin(strike*np.pi/180)
    if (cos_rake<0): rake=180-rake;
    
    if (strike<0   ): strike = strike+360;
    if (rake  <-180): rake   = rake  +360;
    if (rake  > 180): rake   = rake  -360;
        
    strike2 = np.real(strike)
    dip2 = np.real(dip)
    rake2 = np.real(rake)
    
    return strike1, dip1, rake1, strike2, dip2, rake2

#*************************************************************************#
#                                                                         #
#   function CONJUGATE_SOLUTIONS.m                                        #
#                                                                         #
#   calculation of conjugate focal mechnisms                              #
#                                                                         #
#   input: strike, dip and rake                                           #
#                                                                         #
#*************************************************************************#

def conjugate_solutions(strike, dip, rake):
    
    N = len(strike)
    
    n = np.zeros(N)
    u = np.zeros(N)
    
    strike1 = np.zeros(N)
    dip1 = np.zeros(N)
    rake1 = np.zeros(N)
    
    strike2 = np.zeros(N)
    dip2 = np.zeros(N)
    rake2 = np.zeros(N)
    
    #--------------------------------------------------------------------------
    # loop over focal mechanisms
    #--------------------------------------------------------------------------
    for i in range(N):
        
        n[1] = -np.sin(dip[i]*np.pi/180)*np.sin(strike[i]*np.pi/180)
        n[2] =  np.sin(dip[i]*np.pi/180)*np.cos(strike[i]*np.pi/180)
        n[3] = -np.cos(dip[i]*np.pi/180)
    
        u[1] =  np.cos(rake[i]*np.pi/180)*np.cos(strike[i]*np.pi/180) + np.cos(dip[i]*np.pi/180)*np.sin(rake[i]*np.pi/180)*np.sin(strike[i]*np.pi/180)
        u[2] =  np.cos(rake[i]*np.pi/180)*np.sin(strike[i]*np.pi/180) - np.cos(dip[i]*np.pi/180)*np.sin(rake[i]*np.pi/180)*np.cos(strike[i]*np.pi/180)
        u[3] = -np.sin(rake[i]*np.pi/180)*np.sin(dip[i]*np.pi/180)
       
        strike_1,dip_1,rake_1,strike_2,dip_2,rake_2 = strike_dip_rake(n,u)
        
        strike1[i] = strike_1
        dip1[i] = dip_1
        rake1[i] = rake_1
        
        strike2[i] = strike_2
        dip2[i] = dip_2
        rake2[i] = rake_2
        
    return strike1, dip1, rake1, strike2, dip2, rake2

#*************************************************************************#
#                                                                         #
#   function READ_MECHANISMS.m                                            #
#                                                                         #
#   reading the input focal mechansisms                                   #
#                                                                         #
#   input: name of the input file                                         #
#                                                                         #
#*************************************************************************#
def read_mechanisms(input_file):
    #--------------------------------------------------------------------------
    # reading data
    #--------------------------------------------------------------------------
    # [strike dip rake] = textread(input_file,'#f#f#f','commentstyle','matlab');
    strike, dip, rake = np.loadtxt(input_file, comments=['#','%'], unpack = True) 
    
    #--------------------------------------------------------------------------
    # eliminating badly conditioned focal mechanisms
    #--------------------------------------------------------------------------
    # excluding dip to be exactly zero
    dip_0 = (dip<1e-5);
    dip   = dip+dip_0*1e-2;
    
    # excluding rake to be exactly +/-90 degrees
    rake_90 = ((89.9999<abs(rake))&(abs(rake)<90.0001));
    rake    = rake+rake_90*1e-2;
    
    #--------------------------------------------------------------------------
    # conjugate solutions
    #--------------------------------------------------------------------------
    [strike1,dip1,rake1,strike2,dip2,rake2] = conjugate_solutions(strike,dip,rake);
    
    strike1 = strike1
    dip1 = dip1
    rake1 = rake1
    
    strike2 = strike2
    dip2 = dip2
    rake2 = rake2
    
    
    return strike1, dip1, rake1, strike2, dip2, rake2


#*************************************************************************#
#                                                                         #
#  function STABILITY_CRITERION                                           #
#                                                                         #
#  function calculates the fault instability and and identifies faults    #
#  with unstable nodal planes                                             #
#                                                                         #
#  input:  stress                                                         #
#          friction                                                       #
#          complementary focal mechanisms                                 #
#                                                                         #
#  output: focal mechanisms with correct fault orientations               #
#          instability of faults                                          #
#                                                                         #
#*************************************************************************#
def stability_criterion(tau,friction,strike1,dip1,rake1,strike2,dip2,rake2):
    
    import numpy as np
    #--------------------------------------------------------------------------
    # principal stresses
    #--------------------------------------------------------------------------
    sigma = np.sort(np.linalg.eigvals(tau))
    shape_ratio = (sigma[0]-sigma[1])/(sigma[0]-sigma[2])

    #--------------------------------------------------------------------------
    # principal stress directions
    #--------------------------------------------------------------------------
    diag_tensor, vector = np.linalg.eig(tau)
    
    value = np.linalg.eigvals(np.diag(diag_tensor))
    value_sorted=np.sort(value)
    j = np.argsort(value)
    
    sigma_vector_1  = np.array(vector[:,j[0]])
    sigma_vector_2  = np.array(vector[:,j[1]])
    sigma_vector_3  = np.array(vector[:,j[2]])
    
    #--------------------------------------------------------------------------
    #  two alternative fault normals
    #--------------------------------------------------------------------------
    # first fault normal
    n1_1 = -np.sin(dip1*np.pi/180)*np.sin(strike1*np.pi/180)
    n1_2 =  np.sin(dip1*np.pi/180)*np.cos(strike1*np.pi/180)
    n1_3 = -np.cos(dip1*np.pi/180)
    
    # second fault normal
    n2_1 = -np.sin(dip2*np.pi/180)*np.sin(strike2*np.pi/180)
    n2_2 =  np.sin(dip2*np.pi/180)*np.cos(strike2*np.pi/180)
    n2_3 = -np.cos(dip2*np.pi/180)
    
    #--------------------------------------------------------------------------
    # notation: sigma1 = 1 sigma2 = 1-2*shape_ratio sigma3 = -1
    #--------------------------------------------------------------------------
    # fault plane normals in the coordinate system of the principal stress axes
    n1_1_ = n1_1*sigma_vector_1[0] + n1_2*sigma_vector_1[1] + n1_3*sigma_vector_1[2]
    n1_2_ = n1_1*sigma_vector_2[0] + n1_2*sigma_vector_2[1] + n1_3*sigma_vector_2[2]
    n1_3_ = n1_1*sigma_vector_3[0] + n1_2*sigma_vector_3[1] + n1_3*sigma_vector_3[2]
    
    n2_1_ = n2_1*sigma_vector_1[0] + n2_2*sigma_vector_1[1] + n2_3*sigma_vector_1[2]
    n2_2_ = n2_1*sigma_vector_2[0] + n2_2*sigma_vector_2[1] + n2_3*sigma_vector_2[2]
    n2_3_ = n2_1*sigma_vector_3[0] + n2_2*sigma_vector_3[1] + n2_3*sigma_vector_3[2]
    
    #--------------------------------------------------------------------------
    # 1. alternative
    #--------------------------------------------------------------------------
    tau_shear_n1_norm   = np.sqrt(n1_1_**2+(1-2*shape_ratio)**2*n1_2_**2.+n1_3_**2-(n1_1_**2+(1-2*shape_ratio)*n1_2_**2-n1_3_**2)**2)
    tau_normal_n1_norm = (n1_1_**2+(1-2*shape_ratio)*n1_2_**2-n1_3_**2)

    #--------------------------------------------------------------------------
    # 2. alternative
    #--------------------------------------------------------------------------
    tau_shear_n2_norm   = np.sqrt(n2_1_**2+(1-2*shape_ratio)**2*n2_2_**2.+n2_3_**2-(n2_1_**2+(1-2*shape_ratio)*n2_2_**2-n2_3_**2)**2)
    tau_normal_n2_norm = (n2_1_**2+(1-2*shape_ratio)*n2_2_**2-n2_3_**2)
    
    #--------------------------------------------------------------------------
    # instability
    #--------------------------------------------------------------------------
    instability_n1 = (tau_shear_n1_norm - friction*(tau_normal_n1_norm-1))/(friction+np.sqrt(1+friction**2))
    instability_n2 = (tau_shear_n2_norm - friction*(tau_normal_n2_norm-1))/(friction+np.sqrt(1+friction**2))         

    instability = np.maximum(instability_n1, instability_n2)  
    i_index = np.zeros(instability.size)
    for i in range (instability.size):
        i_index[i] = 1 if instability_n1[i] == instability[i] else 2

    #--------------------------------------------------------------------------
    # identification of the fault according to the instability criterion
    #--------------------------------------------------------------------------
    strike = (i_index-1)*strike2+(2-i_index)*strike1
    dip    = (i_index-1)*dip2   +(2-i_index)*dip1
    rake   = (i_index-1)*rake2  +(2-i_index)*rake1 

    return strike,dip,rake,instability

str = [283, 21, 13]
dip = [80, 42, 80]
rak = [-13, 90, -129]
tau11 = 0.323285832573846
tau12 = -0.20306517140696242
tau13 = 0.20744665793076275
tau22 = -0.26096100956587637
tau23 = 0.7686277038238346
tau33 = -0.06232482300796935
tau = np.zeros([3,3])
tau[0][0] = tau11; tau[0][1] = tau12; tau[0][2] = tau13
tau[1][0] = tau12; tau[1][1] = tau22; tau[1][2] = tau23
tau[2][0] = tau13; tau[2][1] = tau23; tau[2][2] = tau33
friction = 0.6


str1, dip1, rak1, str2, dip2, rak2 = read_mechanisms("/mnt/d/celebes-stress-inversion-project/test/cls1.dat")
print(str1, "\n", dip1, "\n", rak1, "\n", str2, "\n", dip2, "\n", rak2, "\n", "\n")

strike,dipe,rake,instability=stability_criterion(tau,friction,str1, dip1, rak1, str2, dip2, rak2)
print(strike, "\n",dipe, "\n",rake, "\n",instability)