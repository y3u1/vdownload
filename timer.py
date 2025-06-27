from loguru import logger
import asyncio
import transmissionrpc
import tc


class Timer:
    def __init__(self):
        pass
    

    async def torrents_status_report_timer(self,tc):
        ''' get all torrents and report it status
        Args:
            tc : TransmissionClient
        '''
        logger.info("Torrents_status_report_timer start...")
        while True: 
            try:
                torrents_list = tc.client.get_torrents()
                if not torrents_list :
                    logger.info("No torrents running now")
                for t in torrents_list:
                    if t.status == "seeding":
                        t.stop()
                        tc.client.remove_torrent(t.id)
                        logger.info("remove seeding torrent : {}".format(t._get_name_string().decode()))
                        continue
                    logger.info("{} : {} : {}%".format(t._get_name_string().decode(),t.status,t.progress))
                await asyncio.sleep(60)
            except Exception as e:
                logger.debug("Error for {}".format(e))
                await asyncio.sleep(180)
        return
    async def torrents_add_timer():
        pass

    def start():
        pass

    def stop():
        pass


