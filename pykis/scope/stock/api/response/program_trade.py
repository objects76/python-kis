from ...._import import *

class KisStockProgramTrade(KisDynamic):
    bsop_hour:time
    '''영업 시간	String	Y	6	'''
    stck_prpr:int
    '''주식 현재가	String	Y	10'''
    prdy_vrss:int
    '''전일 대비	String	Y	10'''
    prdy_vrss_sign: Literal[1, 2, 3, 4, 5]
    '''	전일 대비 부호	String	Y	1'''
    prdy_ctrt:float
    '''전일 대비율	String	Y	82'''
    acml_vol:int
    '''누적 거래량	String	Y	18'''
    whol_smtn_seln_vol:int
    '''전체 합계 매도 거래량	String	Y	18'''
    whol_smtn_shnu_vol:int
    '''전체 합계 매수2 거래량	String	Y	18'''
    whol_smtn_ntby_qty:int
    '''전체 합계 순매수 수량	String	Y	18'''
    whol_smtn_seln_tr_pbmn:int
    '''전체 합계 매도 거래 대금	String	Y	18'''
    whol_smtn_shnu_tr_pbmn:int
    '''전체 합계 매수2 거래 대금	String	Y	18'''
    whol_smtn_ntby_tr_pbmn:int
    '''전체 합계 순매수 거래 대금	String	Y	18'''
    whol_ntby_vol_icdc:int
    '''전체 순매수 거래량 증감	String	Y	10'''
    whol_ntby_tr_pbmn_icdc:int
    '''전체 순매수 거래 대금 증감	String	Y	10'''

class KisStockProgramTrades(KisDynamicAPIResponse):
    '''시간별 프로그램 trade'''
    trades: list[KisStockProgramTrade]

    def __init__(self, data: dict, response: requests.Response):
        super().__init__(data, response)
        # print('debug KisStockProgramTrades:', data.keys())

        self.trades = [KisStockProgramTrade(trade) for trade in data['output']]