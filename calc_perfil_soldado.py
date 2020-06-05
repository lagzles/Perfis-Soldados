# -*- coding: cp1252 -*-
import propriedades_perfil_i as prop
import nbr8800 as nbr
import operator
import math as m

def calc_simples(d, tw, bf, tf, nsd, msdx, vsd, fy, E, G, l, kx, ky, kz):
    d = d / 10
    tw = tw / 10
    bf = bf / 10
    tf = tf / 10    
    
    A = prop.area(d,tw,bf,tf,bf,tf) # cm²
    tensaor = prop.tensaor(fy)

    cgx = prop.cgx(d)
    cgy = prop.cgy(bf)

    ix = prop.i_x(d, tf, bf, bf, tf, tw) # cm4
    iy = prop.i_y(d, tf, bf, bf, tf, tw) # cm4
    it = prop.i_t(tf, bf, tw, d) # cm4
    j = prop.j_(d, tw, tf, tf, bf, bf) # cm3
    cw = prop.cw(d, tf, bf) # cm3 
    zx = prop.zx(bf, tf, d, tw)
    zy = prop.zy(bf, tf, d, tw)
    kc = prop.kc(tf, d, tw)
    
    rx = prop.r_x(ix, A) # cm
    ry = prop.r_y(iy, A) # cm
    rt = prop.r_t(it, A) # cm
    ly = l * ky
    lx = l * kx
    lambda_y = prop.lambda_y(ly, ry)
    lambda_x = prop.lambda_x(lx, rx)

    wx = prop.wx(ix, d)
    wy = prop.wy(iy, d)

    ro = nbr.r_o(rx, ry, 0, 0) # cm

    if lambda_y > 260 and lambda_x > 260:        
        return (d/tw,'','','','','','')
    
    if lx / ro > 300 and ly / ro > 300:
        return (l/ro,'','','','','','')

    b = bf * 0.5
    h = d - 2 * tf

    vrd = nbr.verificacao_cisalhamento(d, tw, tf, fy)
    
    mrd_flm = nbr.verificacao_flexao_FLM(bf, tf, kc, wx, zx, tensaor, fy)
    mrd_fla = nbr.verificacao_flexao_FLA(d, tw, tf, wx, zx, fy) 
    mrd_flt = nbr.verificacao_flexao_FLT(ly, ry, iy, it, wx, zx, cw, tensaor, fy)

    mrd = min(mrd_flt, mrd_flm, mrd_fla)    
        
    ncrd = nbr.nc_rd(E, d, tw, bf, tf, bf, tf, ix, kx, l, iy, ky, l, G, j, cw, kz, l, ro, A, fy)
    
    eficiencia = nbr.atuacao_simultanea(nsd, ncrd, msdx, mrd, 1, 9999999999)

    e_nsd = nsd / ncrd
    e_flt = msdx / mrd_flt
    e_flm = msdx / mrd_flm
    e_fla = msdx / mrd_fla    
    
    nome = (str(d*10) + "x" + str(bf*10) + "x" + str(tw*10) + "x" + str(tf*10))

    peso = A * 7850 / 10000
    retorno = (nome, "{0:.2f} kg/m".format(peso),
               "{0:.1f}% ".format(eficiencia*100),
               "Nrd={0:.1f}%".format(e_nsd*100),
               "FLT={0:.1f}% ".format(e_flt*100),
               "FLA={0:.1f}% ".format(e_fla*100),
               "FLM={0:.1f}% ".format(e_flm*100),
               "FLM Y={0:.1f}% ".format(0*100))

    print("nsd={0:.1f} - nrd= {1:.1f}".format(nsd, ncrd))
    print("msd={0:.1f} - mrd= {1:.1f}".format(msdx, mrd))
    print("vsd={0:.1f} - vrd= {1:.1f}".format(vsd, vrd))
    print(nome + " - {0:.2f} kg/m".format(peso) + " - {0:.1f}% ".format(eficiencia*100))
    
    return retorno

#########################################    

def calc_otimizado(nsd, msdx, vsd, fy, E, G, l, kx, ky, kz):
    lista_almas = (300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350)
    lista_espessuras = (3.75,4.75,6.35,7.94,9.52,12.7,15.88,19.0,22.2,25.4,31.75)
    lista_mesas = (150,175,200,225,250,275,300,325,350,375)

    perfis_peso = {}
    perfis_eficiencia = {}
    contador = 0

    for tw in lista_espessuras:
        tw = tw / 10.
        for d in lista_almas:
            d = float(d /10.)
            for tf in lista_espessuras:
                tf = tf / 10.    
                if tf >= tw:
                    for bf in lista_mesas:
                        bf = float(bf / 10.)
                   
                        A = prop.area(d,tw,bf,tf,bf,tf) # cm²
                        tensaor = prop.tensaor(fy)

                        cgx = prop.cgx(d)
                        cgy = prop.cgy(bf)

                        ix = prop.i_x(d, tf, bf, bf, tf, tw) # cm4
                        iy = prop.i_y(d, tf, bf, bf, tf, tw) # cm4
                        it = prop.i_t(tf, bf, tw, d) # cm4
                        j = prop.j_(d, tw, tf, tf, bf, bf) # cm3
                        cw = prop.cw(d, tf, bf) # cm3 
                        zx = prop.zx(bf, tf, d, tw)
                        zy = prop.zy(bf, tf, d, tw)
                        kc = prop.kc(tf, d, tw)
                        
                        rx = prop.r_x(ix, A) # cm
                        ry = prop.r_y(iy, A) # cm
                        rt = prop.r_t(it, A) # cm
                        ly = l * ky
                        lx = l * kx
                        lambda_y = prop.lambda_y(ly, ry)
                        lambda_x = prop.lambda_x(lx, rx)

                        wx = prop.wx(ix, d)
                        wy = prop.wy(iy, d)

                        ro = nbr.r_o(rx, ry, 0, 0) # cm

                        if lambda_y > 260 and lambda_x > 260:        
                            return (d/tw,'','','','','','')
                        
                        if lx / ro > 300 and ly / ro > 300:
                            return (l/ro,'','','','','','')

                        b = bf * 0.5
                        h = d - 2 * tf
                        
                        mrd_flm = nbr.verificacao_flexao_FLM(bf, tf, kc, wx, zx, tensaor, fy)
                        mrd_fla = nbr.verificacao_flexao_FLA(d, tw, tf, wx, zx, fy)
                        mrd_flt = nbr.verificacao_flexao_FLT(ly, ry, iy, it, wx, zx, cw, tensaor, fy)

                        mrd = min(mrd_flt, mrd_flm, mrd_fla)
                            
                        ncrd = nbr.nc_rd(E, d, tw, bf, tf, bf, tf, ix, kx, l, iy, ky, l, G, j, cw, kz, l, ro, A, fy)

                        vrd = nbr.verificacao_cisalhamento(d, tw, tf, fy)
                        
                        eficiencia = nbr.atuacao_simultanea(nsd, ncrd, msdx, mrd, 1, 9999999999)
                        eficiencia_corte = vsd / vrd
##                        print eficiencia_corte
                        
##                        if eficiencia > 1.03:
##                            break

                        e_nsd = nsd / ncrd
                        e_flt = msdx / mrd_flt
                        e_flm = msdx / mrd_flm
                        e_fla = msdx / mrd_fla
                        e_flmy = 0.0
                        
                        nome = (str(d*10) + "x" + str(bf*10) + "x" + str(tw*10) + "x" + str(tf*10))

                        peso = A * 7850.0 / 10000.0                        

                        if eficiencia <= 1.03 and eficiencia_corte <= 1.03:
                            contador = contador + 1
##                            print contador
                            perfis_peso[nome] = peso
                            perfis_eficiencia[nome] = ("{0:.1f}% ".format(eficiencia*100),
                                                       "Nrd={0:.1f}%".format(e_nsd*100),
                                                       "FLT={0:.1f}%".format(e_flt*100),
                                                       "FLA={0:.1f}%".format(e_fla*100),
                                                       "FLM={0:.1f}% ".format(e_flm*100),
                                                       "FLM Y={0:.1f}% ".format(e_flmy*100))

        if len(perfis_peso.keys()) > 0:
            foo = dict(perfis_peso)
    ##        print(foo)
            
            primeiro = min(foo.items(), key=operator.itemgetter(1))[0]
    ##      primeiro = min(foo.iteritems(), key=operator.itemgetter(1))[0]
            print(primeiro + " - {0:.2f} kg/m".format(foo[primeiro]) + " - "+(perfis_eficiencia[primeiro][0]))
            primeiro_completo = (primeiro, "{0:.2f} kg/m".format(foo[primeiro]), perfis_eficiencia[primeiro])
            foo.pop(primeiro)
            if len(perfis_peso.keys()) > 1:
        ##      segundo =  min(foo.iteritems(), key=operator.itemgetter(1))[0]
                segundo = min(foo.items(), key=operator.itemgetter(1))[0]
                print(segundo + " - {0:.2f} kg/m".format(foo[segundo]) + " -  "+(perfis_eficiencia[segundo][0]))
                segundo_completo = (segundo,"{0:.2f} kg/m".format(foo[segundo]), perfis_eficiencia[segundo])
                foo.pop(segundo)
                
            if len(perfis_peso.keys()) > 2:
        ##      terceiro =  min(foo.iteritems(), key=operator.itemgetter(1))[0]
                terceiro = min(foo.items(), key=operator.itemgetter(1))[0]
                print(terceiro + " - {0:.2f} kg/m".format(foo[terceiro]) + " - "+(perfis_eficiencia[terceiro][0]))
                terceiro_completo = (terceiro, "{0:.2f} kg/m".format(foo[terceiro]),perfis_eficiencia[terceiro])

            return (primeiro_completo, segundo_completo, terceiro_completo)
