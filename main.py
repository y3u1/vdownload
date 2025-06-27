from lxml import etree
from unicodedata import category
import utils
from vitem import vitem
import io
import tc
from loguru import logger
import asyncio
import timer
global nyaa
url = "https://sukebei.nyaa.si/?page=rss"

def get_rss_feed(url) -> bytes:
    try:
      rep = utils.vreq(url)
      return rep
    except Exception as e:
        print(f"Error fetching RSS feed: {e}")
        return None
def parse_rss_feed(tree):
    # 获取所有的 item 元素
    global nyaa
    items = tree.findall(".//item")
    insert_count = 0
    for item in items:
        title = item.find("title").text
        link = item.find("link").text
        infoHash = item.find(f"{{{nyaa}}}infoHash").text
        size = item.find(f"{{{nyaa}}}size").text
        pub_date = item.find("pubDate").text
        category = item.find(f"{{{nyaa}}}category").text

        if not title or not link or not pub_date:
            print("Missing required fields in item, skipping...")
            continue
        try:
            pub_date = utils.to_timestamp(pub_date)
        except Exception as e:
            print(f"Error parsing publication date: {e}")
            pub_date = 0
        if not pub_date:
            print("Publication date is empty, skipping item...")
            continue
        aitem = vitem( name=title, link=link, infoHash=infoHash, size=size, date=pub_date,category=category)
        # 检查是否插入成功（未重复）
        try:
            aitem.save_to_db()
            insert_count += 1
        except Exception as e:
            # 如果插入失败（如唯一约束冲突），不计数
            pass
    logger.info(f"parse_rss_feed成功插入记录数: {insert_count}")

def parse_save(url):
    global nyaa
    rss_byte_stream = get_rss_feed(url)
    rss_file_stream = io.BytesIO( rss_byte_stream)
    logger.info(f"获取RSS订阅成功，开始解析...")
    # 定义解析器
    parser = etree.XMLParser(encoding="utf-8")
    # 解析 XML 文件
    tree = etree.parse(rss_file_stream, parser=parser)
    nyaa = tree.getroot().nsmap['nyaa']
    parse_rss_feed(tree)


if __name__ == "__main__":
   # parse_save(url)
    tc = tc.TC()
    timer = timer.Timer()
    tc.add_torrents("https://sukebei.nyaa.si/download/4333131.torrent")
    asyncio.run(timer.torrents_status_report_timer(tc))
                     
