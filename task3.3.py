# coding=utf-8
"""課題3.【プログラミング】
③任意のURL（Aとする）と、特定の文字列（Bとする）を指定して実行すると、Aを起点としてURLを辿り、
Bの文字列が出現されるURLまで最も短時間にたどり着き、そのURL経路を出力するプログラムを作成せよ。

target_urlに特定のURL_Aを
target_strに特定の文字列_Bを
入力し実行すると、URL経路を出力する
"""

import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

target_url = "http://hoge.com"
# 任意のURL_A
target_str = "fuga"
# 特定の文字列_B

domain = "{uri.scheme}://{uri.netloc}/".format(uri=urlparse(target_url))
# breadcrumb_list = []
# パンくずリスト

def _search_target_url(breadcrumb_list, url):
	"""Summary line.
		特定の文字列Bが含まれるurlを検索する
		Args:
			breadcrumb_list (list): パンくずリスト
			url(str):特定の文字列Bの検索対象url
		Returns:
			list: パンくずリスト
		"""
	try: urllib.request.urlopen(url, timeout=20).read()
	except: return breadcrumb_list
	# エラーがあった場合はそのままリストを返す

	temp_breadcrumb_list = []
	# 余分なurlを排除したリスト
	soup = BeautifulSoup(urllib.request.urlopen(url, timeout=20).read(), "lxml")
	# urlからhtmlの情報を取得
	for link in soup.find_all('a'):
		# urlからaタグのみを順に抽出(list内の部分一致検索が無いようなので、一度全て回す)
		link_url = link.get('href')
		# href内のurlを代入
		if "://" not in link_url:
			# linkが相対パスだった場合
			link_url = urljoin(url, link_url)

		if target_str in link_url:
			# 文字列Bがurlに含まれていた場合
			ret_list = breadcrumb_list + [link_url]
			return ret_list
		else:
			if domain not in link_url or link_url in breadcrumb_list:
				# 外部のurl,過去に検索したurlの場合、発散してしまうので処理しない
				continue
			else:
				temp_breadcrumb_list.append(link_url)

	for link in temp_breadcrumb_list:
		# 上のループで対象のurlに特定の文字列Bに部分一致するurlが無かった場合
		next_breadcrumb_list = breadcrumb_list + [link]
		temp_breadcrumb_list = _search_target_url(next_breadcrumb_list, link)
		if temp_breadcrumb_list != next_breadcrumb_list:
			# 返り値が引数と違っていた場合（対象URLがあった場合）
			return temp_breadcrumb_list

	return breadcrumb_list

breadcrumb_list = _search_target_url([target_url], target_url)
breadcrumb_str = ">".join(breadcrumb_list)
print(breadcrumb_str)
