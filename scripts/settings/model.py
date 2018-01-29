class Tb_CoordenadaDet(object):
    def __init__(self):
        self.cg_codigo = 'CG_CODIGO'
        self.nc_nivcoo = 'NC_NIVCOO'
        self.ca_codcar = 'CA_CODCAR'
        self.cd_corest = 'CD_COREST'
        self.cd_cornor = 'CD_CORNOR'
        self.cd_numpol = 'CD_NUMPOL'
        self.cd_numver = 'CD_NUMVER'
        self.cd_verpol = 'CD_VERPOL'
        self.cd_tippol = 'CD_TIPPOL'
        self.cd_corest_e = 'CD_COREST_E'
        self.cd_cornor_e = 'CD_CORNOR_E'
        self.sc_coddat_e = 'SC_CODDAT_E'
        self.sc_coddat = 'SC_CODDAT'
        self.name = 'SC_V_COORDENADADET'

    def __str__(self):
        return self.name


class Vw_FraccionadosDet(object):
    def __init__(self):
        self.fd_codigo = 'FD_CODIGO'
        self.fd_numpol = 'FD_NUMPOL'
        self.fd_numver = 'FD_NUMVER'
        self.fd_numniv = 'FD_NUMNIV'
        self.fd_corest = 'FD_COREST'
        self.fd_cornor = 'FD_CORNOR'
        self.fd_corest_e = 'FD_COREST_E'
        self.fd_cornor_e = 'FD_CORNOR_E'
        self.fd_coddat_e = 'FD_CODDAT_E'
        self.name = 'SG_D_FRACCIONADOSDET'

    def __str__(self):
        return self.name
