from ._import import *

def program_trade(
    self: 'KisStockScope',
) -> 'KisStockProgramTrades':
    '''주식, ETF, ETN의 호가 정보를 가져옵니다.'''
    return self.client.request(
        'get',
        '/uapi/domestic-stock/v1/quotations/program-trade-by-stock',
        headers={
            'tr_id': 'FHPPG04650100'
        },
        params={
            # 'FID_COND_MRKT_DIV_CODE': 'J',
            'FID_INPUT_ISCD': self.code,
        },
        # page=KisPage.first(),

        response=KisStockProgramTrades
    )
