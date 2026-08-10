# SH() Function for the calculation of the direction of maximum
#      horizontal stress.
#
#   Copyright (C) 1998-2007 Bjorn Lund
#
# This program is free software; you have the permission to use, copy, and
# distribute it, either verbatim or with modifications, either without cost
# or for a fee, as long as the copyright notice above is distributed with
# the software and you clearly state modifications made to the original code.
# If you use this algorithm for work that is to be published, please cite
# the paper:
# Lund and Townend, (2007). Calculating horizontal stress orientations
#    with full or partial knowledge of the tectonic stress tensor,
#    Geophys. J. Int., v.170, 1328-1335, doi: 10.1111/j.1365-246X.2007.03468.x.
#
#---------------------------------------------------------------------------
#
#   SH()
#      Calculate the direction of maximum horizontal stress using only the
#      directions of the principal stress and R = (S1 - S2)/(S1 - S3).
#      This function uses the methodology described in
#      Lund and Townend, (2007). Calculating horizontal stress orientations
#      with full or partial knowledge of the tectonic stress tensor,
#      Geophys. J. Int., doi: 10.1111/j.1365-246X.2007.03468.x.
#      In particular, SH() uses Equations 11 and 10 from the paper.
#
#   Input:
#      S1, S2, S3 are the principal stress orientations.
#                 The variables holds the coordinates in the North, East
#                 and Down geographical coordinate system as three
#                 component lists of floats, e.g. S1 = [s1N,s1E,s1D]
#      R is a single number describing the relative magnitude of S2 with
#        respect to S1 and S3. R = (S1 - S2)/(S1 - S3)
#
#   Returns:
#      The direction of SH from North, angle in radians
#
import math
EPS = 1.0e-8
UNDEF = -999

def SH(S1,S2,S3,R):

    # Check the input, should be unit vectors
    tmp = math.sqrt(S1[0]*S1[0] + S1[1]*S1[1] + S1[2]*S1[2])
    if tmp > EPS:
        S1[0] /= tmp
        S1[1] /= tmp
        S1[2] /= tmp
    tmp = math.sqrt(S2[0]*S2[0] + S2[1]*S2[1] + S2[2]*S2[2])
    if tmp > EPS:
        S2[0] /= tmp
        S2[1] /= tmp
        S2[2] /= tmp
    tmp = math.sqrt(S3[0]*S3[0] + S3[1]*S3[1] + S3[2]*S3[2])
    if tmp > EPS:
        S3[0] /= tmp
        S3[1] /= tmp
        S3[2] /= tmp
    # Check for orthogonality
    if S1[0]*S2[0] + S1[1]*S2[1] + S1[2]*S2[2] > 1.0e-4:
        print('SH(): S1 and S2 are not orthogonal!')
    if S1[0]*S3[0] + S1[1]*S3[1] + S1[2]*S3[2] > 1.0e-4:
        print('SH(): S1 and S3 are not orthogonal!')
    if S2[0]*S3[0] + S2[1]*S3[1] + S2[2]*S3[2] > 1.0e-4:
        print('SH(): S2 and S3 are not orthogonal!')
    # Check R
    if R < 0.0 or R > 1.0:
        print('SH(): R is out of range!')
        return UNDEF

    # Calculate the denominator and numerator in Eq. 11
    X = S1[0]*S1[0] - S1[1]*S1[1] + (1.0 - R)*(S2[0]*S2[0] - S2[1]*S2[1])
    Y = 2.0*(S1[0]*S1[1] + (1.0 - R)*(S2[0]*S2[1]))
    #print 'SH: X %f Y %f' % (X,Y)

    # Is the denominator (X here) from Eq. 11 in Lund and Townend (2007) zero?
    if math.fabs(X) < EPS:
        #print 'SH: X = 0 R = %.2f' % R
        # If so, the first term in Eq. 10 is zero and we are left with the
        # second term, which must equal zero for a stationary point.
        # The second term is zero either if
        # s1Ns1E + (1-R)*s2Ns2E = 0   (A)
        # or if
        # cos(2*alpha) = 0            (B)
        # If (A) holds, the direction of SH is undefined since Eq. 10 is zero
        # irrespective of the value of alpha. We therefore check for (A) first.
        # If (A) holds, R = 1 + s1Ns1E/s2Ns2E unless s2Ns2E = 0, in which case
        # s1Ns1E also has to be zero for (A) to hold.
        #
        if math.fabs(S2[0]*S2[1]) < EPS:
            # s2Ns2E = 0
	        #print 'SH: s2Ns2E = 0'
            if math.fabs(S1[0]*S1[1]) < EPS:
                #print 'SH: s1Ns1E = s2Ns2E = 0 => SH undefined'
                return UNDEF
            else:
                alpha = math.pi/4.0
        else:
            if math.fabs(R - (1.0 + S1[0]*S1[1]/S2[0]*S2[1])) < EPS:
                #print 'SH: R fits => SH undefined'
                return UNDEF
            else:
                alpha = math.pi/4.0

    # The denominator is non-zero
    else:
        #print 'SH: X != 0 Denominator non-zero'
        alpha = math.atan(Y/X)/2.0

    # Have we found a minimum or maximum? Use 2nd derivative to find out.
    # A negative 2nd derivative indicates a maximum, which is what we want.
    #print X,Y,alpha
    dev2 = -2.0*X*math.cos(2.0*alpha) - 2.0*Y*math.sin(2.0*alpha)
    #print 'SH: dev2 %f' % (dev2)
    if dev2 > 0:
        # We found a minimum. Add 90 degrees to get the maximum.
        alpha += math.pi/2.0

    # The resulting direction of SH is given as [0,180[ degrees.
    if alpha < 0:
        alpha += math.pi
    if alpha > math.pi or math.fabs(alpha - math.pi) < EPS:
        alpha -= math.pi

    return alpha