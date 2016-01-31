# -*- coding: utf-8 -*-
import sys
import json
import requests
# from bs4 import BeautifulSoup
from pyquery import PyQuery

html = u"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>はてな検索 書籍/映画/音楽: スマホ</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="text/css" http-equiv="Content-Style-Type"/>
<meta content="text/javascript" http-equiv="Content-Script-Type"/>
<link href="http://cdn.www.st-hatena.com/css/hatena/header.css" rel="stylesheet" type="text/css"/>
<link href="/css/search.css" rel="stylesheet" type="text/css"/>
<link href="http://search.hatena.ne.jp/opensearch/all.xml" rel="search" title="はてな検索" type="application/opensearchdescription+xml"/>
<link href="/css/asinsearch.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript">
function replaceImage(img) {
  if (img.width == '1' && img.src.match(/\.01\./)) {
    img.src = 'http://www.hatena.ne.jp/images/hatena_aws.gif';
  } else if (img.width == '1') {
    img.src = img.src.replace('.09.','.01.');
  }
}
</script>
<style type="text/css">
.asin-item {
  margin-left: 10px;
  margin-bottom: 30px;
}
</style>
</head>
<body onload="document.search.word.focus()">
<script charset="utf-8" src="http://cdn.www.st-hatena.com/js/header.ja.js" type="text/javascript"></script>
<div id="header"><div id="header-body"><a class="service-logo-container" href="/"><img alt="はてな検索" class="service-logo" src="/images/logo.png" title="はてな検索"/></a><ul class="service-menu"><li><a href="/help">ヘルプ</a></li><li class="global-logo"><a href="http://www.hatena.ne.jp/"><img alt="Hatena" src="http://cdn.www.st-hatena.com/images/header/global-logo.png"/></a></li></ul></div></div>
<table id="hatena-search-form">
<tr>
<td nowrap="" width="1%">
<h1><a href="./"><img alt="Search" height="36" src="/images/search_h.gif" width="120"/></a></h1>
</td>
<td nowrap="">
<ul id="hatena-search-menu">
<li><a href="/search?word=%A5%B9%A5%DE%A5%DB">すべて</a></li>
<li><a href="/keyword?word=%A5%B9%A5%DE%A5%DB">キーワード</a></li>
<li><a href="/websearch?word=%A5%B9%A5%DE%A5%DB">ウェブ</a></li>
<li><a href="/questsearch?word=%A5%B9%A5%DE%A5%DB">はてな質問</a></li>
<li><strong>書籍/映画/音楽</strong></li>
<li><a href="/rakutensearch?word=%A5%B9%A5%DE%A5%DB">楽天市場</a></li>
<li><a href="/videosearch?word=%A5%B9%A5%DE%A5%DB">動画</a></li>
</ul>
<form action="/asinsearch" class="headsearch" name="search">
<input maxlength="2048" name="word" size="20" type="text" value="スマホ"/>
<select id="type-selector" name="type"><option selected="" value="All">全て</option><option value="Books">和書</option><option value="ForeignBooks">洋書</option><option value="Music">ポピュラー音楽</option><option value="Classical">クラシック音楽</option><option value="DVD">DVD</option><option value="Electronics">家電&amp;カメラ</option><option value="Software">PCソフト</option><option value="VideoGames">TVゲーム</option><option value="Kitchen">ホーム&amp;キッチン</option><option value="Toys">おもちゃ</option><option value="SportingGoods">スポーツ&amp;アウトドア</option><option value="HealthPersonalCare">ヘルス&amp;ビューティ</option><option value="Watches">時計</option><option value="Baby">ベビー&amp;マタニティ</option><option value="Apparel">アパレル&amp;ファッション雑貨</option><option value="Grocery">食品&amp;飲料</option><option value="Jewelry">ジュエリー</option><option value="OfficeProducts">文房具・オフィス用品</option> </select>
<input type="submit" value="商品を検索"/>
</form>
</td>
</tr>
</table>
<div class="hatena-search-resultbar">

全てから <strong>スマホ</strong> の検索結果 (<strong>1</strong> - <strong>10</strong> 件目 )

</div>
<div class="hatena-search-result">
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-electronics.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B00QN2N3BC"><img alt="Huawei SIMフリースマートフォン Ascend G620S（ブラック）（LTE対応） G620S-L02/BK" onload="replaceImage(this);" src="http://www.hatena.ne.jp/images/hatena_aws.gif" title="Huawei SIMフリースマートフォン Ascend G620S（ブラック）（LTE対応） G620S-L02/BK"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B00QN2N3BC">Huawei SIMフリースマートフォン Ascend G620S（ブラック）（LTE対応） G620S-L02/BK</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B00QN2N3BC"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B00QN2N3BC"/></a>
</h3>
<ul>
<li>
<!--a href="http://d.hatena.ne.jp/keyword/HUAWEI" class="keyword"-->HUAWEI<!--/a-->
</li>
<li><span class="asin-item-price">￥ 13,879</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-electronics.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B00NE9M7JG"><img alt="geanee FXC-5A SIMフリー スマートフォン イオンスマホ (Android4.4 / 5inch / 500万画素 / デュアル SIM / 通常 SIM /micro SIM / 512MB / 4GB / クアッドコア) FXC5A (本体, 白)" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/41tioww1pyL._SL75_.jpg" title="geanee FXC-5A SIMフリー スマートフォン イオンスマホ (Android4.4 / 5inch / 500万画素 / デュアル SIM / 通常 SIM /micro SIM / 512MB / 4GB / クアッドコア) FXC5A (本体, 白)"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B00NE9M7JG">geanee FXC-5A SIMフリー スマートフォン イオンスマホ (Android4.4 / 5inch / 500万画素 / デュアル SIM / 通常 SIM /micro SIM / 512MB / 4GB / クアッドコア) FXC5A (本体, 白)</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B00NE9M7JG"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B00NE9M7JG"/></a>
<a class="asinword" href="http://d.hatena.ne.jp/asin/B00NE9M7JG"><strong>2</strong>ブログ</a>
</h3>
<ul>
<li>
<!--a href="http://d.hatena.ne.jp/keyword/geanee" class="keyword"-->geanee<!--/a-->
</li>
<li><span class="asin-item-price">￥ 9,800</span><span class="percentagesaved">50%OFF</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-electronics.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B017X11ODU"><img alt="Covia SIMフリー スマートフォン 3G FLEAZ NEO ( Android5.1 / 4inch WVGA / W-CDMA / 標準SIM microSIM / 1GB / 8GB ) CP-B43" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/51Y9CGhTU6L._SL75_.jpg" title="Covia SIMフリー スマートフォン 3G FLEAZ NEO ( Android5.1 / 4inch WVGA / W-CDMA / 標準SIM microSIM / 1GB / 8GB ) CP-B43"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B017X11ODU">Covia SIMフリー スマートフォン 3G FLEAZ NEO ( Android5.1 / 4inch WVGA / W-CDMA / 標準SIM microSIM / 1GB / 8GB ) CP-B43</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B017X11ODU"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B017X11ODU"/></a>
</h3>
<ul>
<li>
<!--a href="http://d.hatena.ne.jp/keyword/covia" class="keyword"-->covia<!--/a-->

        / 2015-12-23
      </li>
<li><span class="asin-item-price">￥ 9,333</span><span class="percentagesaved">11%OFF</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-electronics.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B0099R7Y0O"><img alt="Sony Xperia tipo ST21i Red SIMフリー" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/41OdTzMsLXL._SL75_.jpg" title="Sony Xperia tipo ST21i Red SIMフリー"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B0099R7Y0O">Sony Xperia tipo ST21i Red SIMフリー</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B0099R7Y0O"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B0099R7Y0O"/></a>
<a class="asinword" href="http://d.hatena.ne.jp/asin/B0099R7Y0O"><strong>1</strong>ブログ</a>
</h3>
<ul>
<li>
</li>
<li><span class="asin-item-price">￥ 13,600</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-all.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B00IFK9IYQ"><img alt="京セラ 高耐久性スマートフォン TORQUE NTTドコモ SIMフリー 米国国防総省軍事規格対応 SKT-01" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/51E2QN%2B0bmL._SL75_.jpg" title="京セラ 高耐久性スマートフォン TORQUE NTTドコモ SIMフリー 米国国防総省軍事規格対応 SKT-01"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B00IFK9IYQ">京セラ 高耐久性スマートフォン TORQUE NTTドコモ SIMフリー 米国国防総省軍事規格対応 SKT-01</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B00IFK9IYQ"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B00IFK9IYQ"/></a>
</h3>
<ul>
<li>

        / 2014-03-25
      </li>
<li><span class="asin-item-price">￥ 23,980</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-all.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B01B5UM4H0"><img alt="スマホで稼げる メルカリ LINE MALL 副業入門" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/51Of5dOWKZL._SL75_.jpg" title="スマホで稼げる メルカリ LINE MALL 副業入門"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B01B5UM4H0">スマホで稼げる メルカリ LINE MALL 副業入門</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B01B5UM4H0"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B01B5UM4H0"/></a>
</h3>
<ul>
<li><!--a href="http://d.hatena.ne.jp/keyword/%CC%EE%C2%BC%B9%AC%BB%D2" class="keyword"--><a class="keyword" href="/asinsearch?word=野村幸子&amp;type=All">野村幸子</a></li>
<li>
<!--a href="http://d.hatena.ne.jp/keyword/%A5%BD%A1%BC%A5%C6%A5%C3%A5%AF%BC%D2" class="keyword"-->ソーテック社<!--/a-->

        / 2016-01-30
      </li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-electronics.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B00U5VMU2K"><img alt="(オーキー)Aukey スマートフォン車載ホルダー 360°回転可能 吸盤式 iPhone6 Sなど対応 HD-C4S" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/41uFymhVbeL._SL75_.jpg" title="(オーキー)Aukey スマートフォン車載ホルダー 360°回転可能 吸盤式 iPhone6 Sなど対応 HD-C4S"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B00U5VMU2K">(オーキー)Aukey スマートフォン車載ホルダー 360°回転可能 吸盤式 iPhone6 Sなど対応 HD-C4S</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B00U5VMU2K"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B00U5VMU2K"/></a>
</h3>
<ul>
<li>
<!--a href="http://d.hatena.ne.jp/keyword/Aukey" class="keyword"-->Aukey<!--/a-->
</li>
<li><span class="asin-item-price">￥ 749</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-electronics.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B00VZB6Y30"><img alt="Acer Liquid Z200 Android 4.4 / AndroidデュアルSIM&amp;SIMロックフリー / 4inch ディスプレイ / RAM 512MB / ROM 4GB" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/51v8vxtGS2L._SL75_.jpg" title="Acer Liquid Z200 Android 4.4 / AndroidデュアルSIM&amp;SIMロックフリー / 4inch ディスプレイ / RAM 512MB / ROM 4GB"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B00VZB6Y30">Acer Liquid Z200 Android 4.4 / AndroidデュアルSIM&amp;SIMロックフリー / 4inch ディスプレイ / RAM 512MB / ROM 4GB</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B00VZB6Y30"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B00VZB6Y30"/></a>
</h3>
<ul>
<li>
<!--a href="http://d.hatena.ne.jp/keyword/Acer" class="keyword"-->Acer<!--/a-->
</li>
<li><span class="asin-item-price">￥ 6,980</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-electronics.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B005A2JHW0"><img alt="au HTC EVO WiMAX ISW11HT ブラック Android スマートフォン 白ロム 携帯電話本体" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/41cP5COkFML._SL75_.jpg" title="au HTC EVO WiMAX ISW11HT ブラック Android スマートフォン 白ロム 携帯電話本体"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B005A2JHW0">au HTC EVO WiMAX ISW11HT ブラック Android スマートフォン 白ロム 携帯電話本体</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B005A2JHW0"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B005A2JHW0"/></a>
<a class="asinword" href="http://d.hatena.ne.jp/asin/B005A2JHW0"><strong>8</strong>ブログ</a>
</h3>
<ul>
<li>
<!--a href="http://d.hatena.ne.jp/keyword/HTC" class="keyword"-->HTC<!--/a-->
</li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
<div class="asin-item" style="padding-left: 30px; background: url('http://d.hatena.ne.jp/images/hamazou_icons/icon-all.gif') no-repeat 0 0">
<div class="asin-item-image"><a href="http://d.hatena.ne.jp/asin/B00Q8AC356"><img alt="TaoTronics ゲル吸盤式 スマートフォン・携帯車載ホルダー TT-SH08" onload="replaceImage(this);" src="http://ecx.images-amazon.com/images/I/41mftNGW9YL._SL75_.jpg" title="TaoTronics ゲル吸盤式 スマートフォン・携帯車載ホルダー TT-SH08"/></a></div>
<div class="asin-item-info">
<h3><a href="http://d.hatena.ne.jp/asin/B00Q8AC356">TaoTronics ゲル吸盤式 スマートフォン・携帯車載ホルダー TT-SH08</a> <a class="bookmark-count" href="http://b.hatena.ne.jp/entry/www.amazon.co.jp/gp/product/B00Q8AC356"><img alt="" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/gp/product/B00Q8AC356"/></a>
<a class="asinword" href="http://d.hatena.ne.jp/asin/B00Q8AC356"><strong>2</strong>ブログ</a>
</h3>
<ul>
<li>
</li>
<li><span class="asin-item-price">￥ 1,099</span></li>
</ul>
</div>
<div class="asin-item-footer"></div>
</div>
</div>
<div id="hatena-search-pager">
<span class="hatena-search-pager-title">検索結果：</span>
<span class="hatena-search-pager-current">1</span>
<a href="?word=%A5%B9%A5%DE%A5%DB&amp;page=2&amp;type=All">2</a>
<a href="?word=%A5%B9%A5%DE%A5%DB&amp;page=3&amp;type=All">3</a>
<a href="?word=%A5%B9%A5%DE%A5%DB&amp;page=4&amp;type=All">4</a>
<a href="?word=%A5%B9%A5%DE%A5%DB&amp;page=5&amp;type=All">5</a>
<strong><a href="?word=%A5%B9%A5%DE%A5%DB&amp;page=2&amp;type=All">次へ</a></strong>
</div>
<div id="foot-search-amazon">
<span>ジャンルを絞って検索</span>
<form action="/asinsearch" class="headsearch" name="search">
<input maxlength="2048" name="word" size="20" type="text" value="スマホ"/>
<select id="type-selector" name="type"> <option value="All">全て</option> <option value="Books">和書</option> <option value="ForeignBooks">洋書</option> <option value="Music">ポピュラー音楽</option> <option value="Classical">クラシック音楽</option> <option value="DVD">DVD</option> <option value="Electronics">家電&amp;カメラ</option> <option value="Software">PCソフト</option> <option value="VideoGames">TVゲーム</option> <option value="Kitchen">ホーム&amp;キッチン</option> <option value="Toys">おもちゃ</option> <option value="SportingGoods">スポーツ&amp;アウトドア</option> <option value="HealthPersonalCare">ヘルス&amp;ビューティ</option> <option value="Watches">時計</option> <option value="Baby">ベビー&amp;マタニティ</option> <option value="Apparel">アパレル&amp;ファッション雑貨</option> <option value="Grocery">食品&amp;飲料</option> <option value="Jewelry">ジュエリー</option> <option value="OfficeProducts">文房具・オフィス用品</option> </select>
<input type="submit" value="商品を検索"/>
</form>
</div>
<div id="hatena-search-result-footer">
<p><a href="http://www.hatena.ne.jp/">はてな</a> - <a href="http://www.hatena.ne.jp/what">はてなについて</a></p>
<p id="copyright">Copyright (C) 2001-2016 hatena. All Rights Reserved.</p>
</div>
</body>
</html>
"""


def extract_items(html):
    items = []

    dom = PyQuery(html)
    dom('div.hatena-search-result div.asin-item').each(lambda i, node: items.append(PyQuery(node).html()))

    return items

def scraping(url, output_name):
    # get a HTML response
    # response = requests.get(url)
    # html = response.text.encode(response.encoding)  # prevent encoding errors

    # extract
    items = extract_items(html)

    print items[0]
#    ## description
#    description = header.find("meta", attrs={"name": "description"})
#    description_content = description.attrs['content'].text
#    # output
#    output = {"title": title, "description": description_content}
#    # write the output as a json file
#    with open(output_name, "w") as fout:
#        json = json.dump(output, fout, indent=4, sort_keys=True)
#
if __name__ == '__main__':
    print sys.getdefaultencoding()

    # argvs = sys.argv
    # if len(argvs) != 3:
    #     print "Usage: python scraping.py [url] [output]"
    #     exit()
    # url = argvs[1]
    # output_name = argvs[2]
    url = "http://search.hatena.ne.jp/asinsearch?word=%A5%B9%A5%DE%A5%DB&type=All"
    output_name = 'test.json'
    scraping(url, output_name)

#http://search.hatena.ne.jp/asinsearch?word=&type=All