# coding=utf-8
"""
引数にファイル名を入力すると、そのファイルに入力されている
数値を１行ずつ因数分解し、同ファイルへ出力する
素因数分解できない文字等には"ERROR"を返す
"""

import math
import sys

def _get_prime_number(num):
	"""Summary line.
	エラトステネスの篩を使い、素数を列挙する
	Args:
		num (int): 素因数分解を行う数値
	Returns:
		list: numまでの素数リスト
	"""

	sequence_list = [i for i in range(2, num + 1)]
	#2から入力値までの数列のリスト

	prime_list = []
	# 素数のリスト

	while True:
		prime = min(sequence_list)

		if float(prime) > math.sqrt(num):
			# 入力値の平方根以上は全てリストに加えて終了
			prime_list.extend(sequence_list)
			break
		else:
			prime_list.append(prime)

		i = 0
		while i < len(sequence_list):
			if sequence_list[i] % prime == 0:
				# 素数の倍数をリストから削除
				sequence_list.pop(i)
				continue
			i += 1
	return prime_list


def _check_num_error(num):
	"""Summary line.
	文字列の自然数判定
	Args:
		num (str): 判定する数値（文字列）
	Returns:
		bool: True/2以上の自然数 False/その他
	"""
	if not num.isdigit():
		# 文字列が数値かつ自然数ではない
		ans = False
	elif int(num) < 2:
		# 2より小さい自然数
		ans = False
	else:
		ans = True

	return ans

def _prime_factorization(num):
	"""Summary line.
	素数を使い、素因数分解を行う
	Args:
		num (int): 素因数分解を行う数値
	Returns:
		list: 素因数分解の解
	"""

	prime_list = _get_prime_number(num)
	# ２からnumまでの素数リストを作成

	temp_num = num
	ans_list = []
	i = 0
	while num >= prime_list[i]**2:
		# 対象数値の平方根の数まで処理を行う
		if temp_num % prime_list[i] == 0:
			ans_list.append(str(prime_list[i]))
			temp_num /= prime_list[i]
		else:
			i += 1

	if temp_num != 1:
		ans_list.append(str(int(temp_num)))

	return ans_list


file_name = sys.argv[1]
with open(file_name) as f:
	# ファイルの内容を読み込む
	reader = f.readlines()

for i, val in enumerate(reader):
	# ファイルの内容1行ごとに素因数分解を行う
	ans_list = []
	num = val.replace('\n', '')

	if _check_num_error(num):
		# 正しい引数だった場合、素因数分解
		ans_list = _prime_factorization(int(num))
	else:
		ans_list = ["ERROR"]

	reader[i] = num + "," + ",".join(ans_list)
	# 行の成形

for i in reader:
	# 標準出力
	print(i)