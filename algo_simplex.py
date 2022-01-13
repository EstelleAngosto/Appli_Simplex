# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:16:35 2022

@author: Utilisateur
"""

import numpy as np

def col_piv (lp, last_col) :
    neg = False
    change = False
    n = np.size(lp)
    
    for i in range(n):
        if lp[i]<0:
            neg = True
    
    if neg :
        col_neg = 0
        for j in range(n):
            if lp[j]<0:
              if j!=last_col:
               if lp[j]<lp[col_neg]:
                   col_neg = j
                   change = True
        
        if change == True :
            return col_neg
        else:
           return -1
    else:
        return -1

def lin_piv (lp,line,col,colp) : 
    coefs = []
    linp = 0
    
    for i in range(1,line):
        coefs.append(lp[i,col-1]/lp[i,colp])
        
    for j in range(len(coefs)) :
        if coefs[j] < coefs[linp]:
            linp = j
    
    return linp+1

def calcul(lp,line,col,linp,colp):
    pivot = lp[linp,colp]

    new_matrice = np.empty((line,col))
    
    for i in range(col):
        new_matrice[linp,i] = lp[linp,i]/pivot
    
    for j in range(line):
        for k in range(col):
            if j!=linp : 
                new_matrice[j,k] = lp[j,k]-((lp[j,colp]/pivot)*new_matrice[linp,k])

    return new_matrice            
    
#%% Algo des simplex

def simplex(simplex):

    line, column = np.shape(simplex)

    col_pivot = col_piv(simplex[0,:],-1)
    print("Col pivot 1")

    while col_pivot != -1:
        last_col=col_pivot
        lin_pivot = lin_piv(simplex,line,column,col_pivot)
        print("line pivot")
        simplex = calcul(simplex, line, column, lin_pivot, col_pivot)
        print("calcul des lignes")
        col_pivot = col_piv(simplex[0,:],last_col)
        print(col_pivot)
        print(simplex)
        print("Nouveau tour")

    return(simplex)

def fonction_BigM(entier, matrice):
    
    M = 100000000000000
    line, column = np.shape(matrice)
    
    for j in range(column) :
        matrice[0,j]=matrice[0,j]-(M*matrice[entier,j])
        
    return matrice

def creation_matrice(liste_fct,liste_c1,liste_c2,liste_c3,liste_c4,type_c1,type_c2,type_c3,type_c4):
                
        M = 100000000000000
        
        BigM = False
        ligne_bigM = []
                
        if type_c1 == "inf":
            liste_fct[len(liste_fct)-2]=0
            liste_fct[len(liste_fct)-1]=1
            liste_fct.append(0)
            
            res_c1=liste_c1[len(liste_c1)-1]
            liste_c1[len(liste_c1)-2]=1
            liste_c1[len(liste_c1)-1]=0
            liste_c1.append(res_c1)
            

            res_c2=liste_c2[len(liste_c2)-1]
            liste_c2[len(liste_c2)-2]=0
            liste_c2[len(liste_c2)-1]=0
            liste_c2.append(res_c2)
            
            if len(liste_c3) != 0:
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=0
                liste_c3[len(liste_c3)-1]=0
                liste_c3.append(res_c3)
                
            if len(liste_c4) != 0:
                res_c4=liste_c4[len(liste_c4)-1]
                liste_c4[len(liste_c4)-2]=0
                liste_c4[len(liste_c4)-1]=0
                liste_c4.append(res_c4)
        
        if type_c1 == "egal" :
                
                BigM = True
                ligne_bigM.append(1)
                
                liste_fct[len(liste_fct)-2]=M
                liste_fct[len(liste_fct)-1]=1
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=1
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(res_c2)
            
                if len(liste_c3) != 0:
                    res_c3=liste_c3[len(liste_c3)-1]
                    liste_c3[len(liste_c3)-2]=0
                    liste_c3[len(liste_c3)-1]=0
                    liste_c3.append(res_c3)
                
                if len(liste_c4) != 0:
                    res_c4=liste_c4[len(liste_c4)-1]
                    liste_c4[len(liste_c4)-2]=0
                    liste_c4[len(liste_c4)-1]=0
                    liste_c4.append(res_c4)
        
        if type_c1 == 'sup' :
            
                BigM = True
                ligne_bigM.append(1)
                
                liste_fct[len(liste_fct)-2]=0
                liste_fct[len(liste_fct)-1]=M
                liste_fct.append(1)
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=1
                liste_c1[len(liste_c1)-1]=1
                liste_c1.append(0)
                liste_c1.append(res_c1)
                
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(0)
                liste_c2.append(res_c2)
                
                if len(liste_c3) != 0:
                    res_c3=liste_c3[len(liste_c3)-1]
                    liste_c3[len(liste_c3)-2]=0
                    liste_c3[len(liste_c3)-1]=0
                    liste_c3.append(0)
                    liste_c3.append(res_c3)
                    
                if len(liste_c4) != 0:
                    res_c4=liste_c4[len(liste_c4)-1]
                    liste_c4[len(liste_c4)-2]=0
                    liste_c4[len(liste_c4)-1]=0
                    liste_c4.append(0)
                    liste_c4.append(res_c4)
        
        print("Type_C1")
        
        if type_c2 == "inf":
            liste_fct[len(liste_fct)-2]=0
            liste_fct[len(liste_fct)-1]=1
            liste_fct.append(0)
            
            res_c1=liste_c1[len(liste_c1)-1]
            liste_c1[len(liste_c1)-2]=0
            liste_c1[len(liste_c1)-1]=0
            liste_c1.append(res_c1)
            
            res_c2=liste_c2[len(liste_c2)-1]
            liste_c2[len(liste_c2)-2]=1
            liste_c2[len(liste_c2)-1]=0
            liste_c2.append(res_c2)
            
            if len(liste_c3) != 0:
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=0
                liste_c3[len(liste_c3)-1]=0
                liste_c3.append(res_c3)
                
            if len(liste_c4) != 0:
                res_c4=liste_c4[len(liste_c4)-1]
                liste_c4[len(liste_c4)-2]=0
                liste_c4[len(liste_c4)-1]=0
                liste_c4.append(res_c4)
        
        if type_c2 == 'egal' :
            
                BigM = True
                ligne_bigM.append(2)
                
                liste_fct[len(liste_fct)-2]=M
                liste_fct[len(liste_fct)-1]=1
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=1
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(res_c2)
            
                if len(liste_c3) != 0:
                    res_c3=liste_c3[len(liste_c3)-1]
                    liste_c3[len(liste_c3)-2]=0
                    liste_c3[len(liste_c3)-1]=0
                    liste_c3.append(res_c3)
                
                if len(liste_c4) != 0:
                    res_c4=liste_c4[len(liste_c4)-1]
                    liste_c4[len(liste_c4)-2]=0
                    liste_c4[len(liste_c4)-1]=0
                    liste_c4.append(res_c4)

        if type_c2 == 'sup' :
                        
                BigM = True
                ligne_bigM.append(2)
            
                liste_fct[len(liste_fct)-2]=0
                liste_fct[len(liste_fct)-1]=M
                liste_fct.append(1)
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(0)
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=1
                liste_c2[len(liste_c2)-1]=1
                liste_c2.append(0)
                liste_c2.append(res_c2)
            
                if len(liste_c3) != 0:
                    res_c3=liste_c3[len(liste_c3)-1]
                    liste_c3[len(liste_c3)-2]=0
                    liste_c3[len(liste_c3)-1]=0
                    liste_c3.append(0)
                    liste_c3.append(res_c3)
                
                if len(liste_c4) != 0:
                    res_c4=liste_c4[len(liste_c4)-1]
                    liste_c4[len(liste_c4)-2]=0
                    liste_c4[len(liste_c4)-1]=0
                    liste_c4.append(0)
                    liste_c4.append(res_c4)                
        
        print("Type_C2")
        
        if type_c3!="":
            
            if type_c3 == "inf":
                liste_fct[len(liste_fct)-2]=0
                liste_fct[len(liste_fct)-1]=1
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(res_c2)
            
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=1
                liste_c3[len(liste_c3)-1]=0
                liste_c3.append(res_c3)
                
                if len(liste_c4) != 0:
                    res_c4=liste_c4[len(liste_c4)-1]
                    liste_c4[len(liste_c4)-2]=0
                    liste_c4[len(liste_c4)-1]=0
                    liste_c4.append(res_c4)
            
            if type_c3 == 'egal' :
                
                BigM = True
                ligne_bigM.append(3)
                
                liste_fct[len(liste_fct)-2]=M
                liste_fct[len(liste_fct)-1]=1
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(res_c2)
            
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=1
                liste_c3[len(liste_c3)-1]=0
                liste_c3.append(res_c3)
                
                if len(liste_c4) != 0:
                    res_c4=liste_c4[len(liste_c4)-1]
                    liste_c4[len(liste_c4)-2]=0
                    liste_c4[len(liste_c4)-1]=0
                    liste_c4.append(res_c4)
                
            if type_c3 == 'sup' :
                                
                BigM = True
                ligne_bigM.append(3)
                
                liste_fct[len(liste_fct)-2]=0
                liste_fct[len(liste_fct)-1]=M
                liste_fct.append(1)
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(0)
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(0)
                liste_c2.append(res_c2)
            
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=1
                liste_c3[len(liste_c3)-1]=1
                liste_c3.append(0)
                liste_c3.append(res_c3)
                
                if len(liste_c4) != 0:
                    res_c4=liste_c4[len(liste_c4)-1]
                    liste_c4[len(liste_c4)-2]=0
                    liste_c4[len(liste_c4)-1]=0
                    liste_c4.append(0)
                    liste_c4.append(res_c4)
        
        print("Type C3")        
        
        if type_c4 != "":
            
            if type_c4 == "inf":
                liste_fct[len(liste_fct)-2]=0
                liste_fct[len(liste_fct)-1]=1
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(res_c2)
            
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=0
                liste_c3[len(liste_c3)-1]=0
                liste_c3.append(res_c3)
                
                res_c4=liste_c4[len(liste_c4)-1]
                liste_c4[len(liste_c4)-2]=1
                liste_c4[len(liste_c4)-1]=0
                liste_c4.append(res_c4)
            
            if type_c4 == 'egal' :
                
                BigM = True
                ligne_bigM.append(4)
                
                BigM = True
                ligne_bigM.append(4)
                
                liste_fct[len(liste_fct)-2]=M
                liste_fct[len(liste_fct)-1]=1
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(res_c2)
            
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=0
                liste_c3[len(liste_c3)-1]=0
                liste_c3.append(res_c3)
                
                res_c4=liste_c4[len(liste_c4)-1]
                liste_c4[len(liste_c4)-2]=1
                liste_c4[len(liste_c4)-1]=0
                liste_c4.append(res_c4)
                
            if type_c4 == 'sup' :
                
                BigM = True
                ligne_bigM.append(4)
                                
                liste_fct[len(liste_fct)-2]=0
                liste_fct[len(liste_fct)-1]=M
                liste_fct.append(1)
                liste_fct.append(0)
            
                res_c1=liste_c1[len(liste_c1)-1]
                liste_c1[len(liste_c1)-2]=0
                liste_c1[len(liste_c1)-1]=0
                liste_c1.append(0)
                liste_c1.append(res_c1)
            
                res_c2=liste_c2[len(liste_c2)-1]
                liste_c2[len(liste_c2)-2]=0
                liste_c2[len(liste_c2)-1]=0
                liste_c2.append(0)
                liste_c2.append(res_c2)
            
                res_c3=liste_c3[len(liste_c3)-1]
                liste_c3[len(liste_c3)-2]=0
                liste_c3[len(liste_c3)-1]=0
                liste_c3.append(0)
                liste_c3.append(res_c3)
                
                res_c4=liste_c4[len(liste_c4)-1]
                liste_c4[len(liste_c4)-2]=1
                liste_c4[len(liste_c4)-1]=1
                liste_c4.append(0)
                liste_c4.append(res_c4)
               
        print(liste_fct)
        print(liste_c1)
        print(liste_c2)
        print(liste_c3)
        print(liste_c4)
        
        liste = []
        liste.append(liste_fct)
        liste.append(liste_c1)
        liste.append(liste_c2)
        
        if len(liste_c3) != 0 :
            liste.append(liste_c3)
            
        if len(liste_c4) != 0 :
            liste.append(liste_c4)
        
        matrice = np.array(liste)
        
        if BigM == True :
            for i in ligne_bigM:
                matrice = fonction_BigM(i,matrice)
        
        print(matrice)
        
        simplex(matrice)

# matrice = np.array([[-11,-16,-15,0,0,0,1,0],
#                     [1,2,1.5,1,0,0,0,12000],
#                     [0.66,0.66,1,0,1,0,0,4600],
#                     [0.5,0.33,0.5,0,0,1,0,2400]])

# matrice_simplex = simplex(matrice)
# print(matrice_simplex)

