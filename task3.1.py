# 課題3.【プログラミング】
# ①	変数int xを引数として渡されると、xの約数を全て足し算した結果を返すプログラムを作成せよ。

# coding:utf-8
import math

def get_prime_number(num):
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

		if prime > math.sqrt(num):
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

def prime_factorization(num):
	"""Summary line.
	素数を使い、素因数分解を行う
	Args:
		num (int): 素因数分解を行う数値
	Returns:
		list: 素因数分解の解
	"""

	prime_list = get_prime_number(num)
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


try:
	while True:
		num = int(input())
		prime_list = prime_factorization(num)
		#素因数分解のリストを作成

		temp_num = 0
		power_num = 0
		sum_divisor = 0
		for i, val in enumerate(prime_list):
			#素因数分解を用いて約数の総和を求める公式
			if i == 0:
				temp_num = 1 + int(val)
				power_num = 2
			else:
				if val == prime_list[i-1]:
					#素数が直前と同じだった場合
					temp_num += int(val)**power_num
					power_num += 1
				else:
					if sum_divisor == 0:
						sum_divisor = temp_num
					else:
						sum_divisor *= temp_num
					temp_num = 1 + int(val)
					power_num = 2

		sum_divisor *= temp_num
		print(sum_divisor)
except EOFError:
	pass