from loguru import logger
import asyncio
import transmissionrpc



class Timeer:
    def __init__(self):
        pass
    

    async def torrents_status_report_timer(tc):
        ''' get all torrents and report it status
        Args:
            tc : TransmissionClient
        '''
        while True:
            asyncio.sleep(60)
            try:
                torrents_list = tc.get_torrents()
                for t in torrents_list:
                    logger.info("{} : {}%".format(t.status,t.progress))
            except :
                continue
        return
    async def torrents_add_timer():
        pass

    def start():
        pass

    def stop():
        pass


