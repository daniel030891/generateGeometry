# -*- coding: utf-8 -*-
from settings.model import *
from settings.config import *

# SC_V_COORDENADADET
class CoordenadaDet(Tb_CoordenadaDet):
    def __init__(self):
        super(self.__class__, self).__init__()
        self._code = None
        self.where = None
        self.sql = "SELECT {} FROM {} WHERE {} ORDER BY {}"
        self.fields = [
            self.cd_numpol,
            self.cd_numver,
            '',
            ''
        ]
        self.conn = ManageConnect('oracle').conn

    @property
    def getcode(self):
        return self._code

    def settable(self, code, wkid):
        src = str()
        self._code = code
        self.where = "{} = '{}'".format(
            self.cg_codigo, self._code
        )
        for k, v in Sreference().__dict__.items():
            if wkid in v:
                src = k
                break
            else:
                pass

        if src == 'wgs':
            self.fields[-1] = self.cd_corest_e
            self.fields[-2] = self.cd_cornor_e
        elif src == 'psad':
            self.fields[-1] = self.cd_corest
            self.fields[-2] = self.cd_cornor

        self.sql = self.sql.format(
            ', '.join(self.fields),
            self.name,
            self.where,
            self.cd_numpol + ", " + self.cd_numver
        )

    def getcoords(self):
        cursor = oracle.Cursor(self.conn)
        cursor.execute(self.sql)
        array = [x for x in cursor]
        cursor.close()
        values = set(map(lambda x: x[0], array))
        coords = [
            [[m[-2], m[-1]] for m in array if m[0] == x] for x in values
        ]
        return coords


# SG_D_FRACCIONADOSDET
class FraccionadosDet(Vw_FraccionadosDet):
    def __init__(self):
        super(self.__class__, self).__init__()
        self._code = None
        self.where = None
        self.sql = "SELECT {} FROM {} WHERE {} ORDER BY {}"
        self.fields = [
            self.fd_numpol,
            self.fd_numver,
            '',
            ''
        ]
        self.conn = ManageConnect('oracle').conn

    @property
    def getcode(self):
        return self._code

    def settable(self, code, wkid):
        src = str()
        self._code = code
        self.where = "{} = '{}'".format(
            self.fd_codigo, self._code
        )
        for k, v in Sreference().__dict__.items():
            if wkid in v:
                src = k
                break
            else:
                pass


        if src == 'wgs':
            self.fields[-1] = self.fd_corest_e
            self.fields[-2] = self.fd_cornor_e
        elif src == 'psad':
            self.fields[-1] = self.fd_corest
            self.fields[-2] = self.fd_cornor

        self.sql = self.sql.format(
            ', '.join(self.fields),
            self.name,
            self.where,
            self.fd_numpol + ", " + self.fd_numver
        )

    def getcoords(self):
        cursor = oracle.Cursor(self.conn)
        cursor.execute(self.sql)
        array = [x for x in cursor]
        cursor.close()
        values = set(map(lambda x: x[0], array))
        coords = [
            [[m[-2], m[-1]] for m in array if m[0] == x] for x in values
        ]
        return coords


class GetTable:
    def __init__(self, tb):
        # SC_V_COORDENADADET
        if tb == Tb_CoordenadaDet().name:
            self.table = CoordenadaDet()
        # SG_D_FRACCIONADOSDET
        elif tb == Vw_FraccionadosDet().name:
            self.table = FraccionadosDet()
