def linear_stress_inversion_Michael(strike1,dip1,rake1,strike2,dip2,rake2):
    
    import numpy as np
        
    N = np.size(strike1)
    
    strike = np.zeros((N))
    dip= np.zeros((N))
    rake = np.zeros((N))
    
    #--------------------------------------------------------------------------
    # focal mechanisms with randomly selected fault planes
    #--------------------------------------------------------------------------
    for i_mechanism in range (N):
        strike [i_mechanism] = strike1[i_mechanism]
        dip   [i_mechanism] = dip1   [i_mechanism]
        rake  [i_mechanism] = rake1  [i_mechanism]
    #--------------------------------------------------------------------------
    #  fault normals and slip directions
    #--------------------------------------------------------------------------
    u1 =  np.cos(rake*np.pi/180)*np.cos(strike*np.pi/180) + np.cos(dip*np.pi/180)*np.sin(rake*np.pi/180)*np.sin(strike*np.pi/180)
    u2 =  np.cos(rake*np.pi/180)*np.sin(strike*np.pi/180) - np.cos(dip*np.pi/180)*np.sin(rake*np.pi/180)*np.cos(strike*np.pi/180)
    u3 = -np.sin(rake*np.pi/180)*np.sin(dip*np.pi/180)
        
    n1 = -np.sin(dip*np.pi/180)*np.sin(strike*np.pi/180)
    n2 =  np.sin(dip*np.pi/180)*np.cos(strike*np.pi/180)
    n3 = -np.cos(dip*np.pi/180)
    
    #--------------------------------------------------------------------------
    # inverted matrix A
    #--------------------------------------------------------------------------
    A1 = np.zeros((N,5)); A2 = np.zeros((N,5)); A3 = np.zeros((N,5))
    a_vector= np.zeros((3*N+1,1))
    
    # matrix coefficients
    A11_n =  n1*(1  -n1**2)
    A21_n =       -n1 *n2**2
    A31_n =       -n1*n3**2
    A41_n =    -2*n1*n2*n3
    A51_n =  n3*(1-2*n1**2)
    A61_n =  n2*(1-2*n1**2)
    
    A12_n =       -n2*n1**2
    A22_n =  n2*(1-  n2**2)
    A32_n =       -n2*n3**2
    A42_n =  n3*(1-2*n2**2)
    A52_n =    -2*n1*n2*n3
    A62_n =  n1*(1-2*n2**2)
    
    A13_n =       -n3*n1**2
    A23_n =       -n3*n2**2
    A33_n =  n3*(1-  n3**2)
    A43_n =  n2*(1-2*n3**2)
    A53_n =  n1*(1-2*n3**2)
    A63_n =    -2*n1*n2*n3
    
    A1 = np.transpose([A11_n, A21_n, A31_n, A41_n, A51_n, A61_n])
    A2 = np.transpose([A12_n, A22_n, A32_n, A42_n, A52_n, A62_n])
    A3 = np.transpose([A13_n, A23_n, A33_n, A43_n, A53_n, A63_n])
    
    a_vector_1 = np.zeros((N))
    a_vector_2 = np.zeros((N))
    a_vector_3 = np.zeros((N))
    

    for i in range (N):
        a_vector_1[i] = np.transpose(u1[i])
        a_vector_2[i] = np.transpose(u2[i])
        a_vector_3[i] = np.transpose(u3[i])

    
    A = np.r_[A1, A2, A3]
    a_vector = np.r_[a_vector_1, a_vector_2, a_vector_3]
    
    # condition for zero trace of the stress tensor
    A = np.append(A, [[1., 1., 1., 0, 0, 0]], axis = 0)
    a_vector = np.append(a_vector, [0])

    #--------------------------------------------------------------------------
    # generalized inversion
    # np.pinv(A) gives sometimes complex-valued numbers
    #--------------------------------------------------------------------------
    stress_vector = np.real(np.dot(np.linalg.pinv(A), a_vector))
    print(stress_vector)
    
    stress_tensor = np.r_[np.c_[stress_vector[0], stress_vector[5], stress_vector[4]],
                     np.c_[stress_vector[5], stress_vector[1], stress_vector[3]],
                     np.c_[stress_vector[4], stress_vector[3], stress_vector[2]]]
    print(stress_tensor)
    sigma  = np.linalg.eigvals(stress_tensor)
    print(max(abs(sigma)))
    stress = stress_tensor/max(abs(sigma))
    print(stress)
    return stress 

s1 = [233]#, 91]
d1 = [38]#, 83]
r1 = [-96]#, 3]
s2 = [61]#, 1]
d2 = [53]#, 87]
r2 = [-85]#, 173]

tau = linear_stress_inversion_Michael(s1, d1, r1, s2, d2, r2)