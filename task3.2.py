# 課題3.【プログラミング】
# ②-1素因数分解を再帰的に行う関数を作成せよ。

#coding:utf-8
def Factoring (num):
	"""Summary line.
	エラトステネスの篩アルゴリズムを使い、素因数分解を行う
	Args:
		num (int): 素因数分解を行う数値
	Returns:
		list: 素因数分解された素数
	"""

	count = 2

	if num.isdigit() or num < 2:
		#自然数かつ1以上の数値を判定
		return print('１より大きい自然数を入力してください')

	sequence_list = [i for i in range (2, num+1)]
	#2から入力値までの数列のリストを作成
	prime_list = []
	#素数のリスト

	while True:
		prime = min(sequence_list)

		if prime > math.sqrt(num):
			#入力値の平方根以上を全て代入する
			prime_list.extend(sequence_list)
			break

		while i < len(sequence_list):
			if num % i == 0:
				prime_list.append(i)






def eratosthenes(limit):
	A = [i for i in range(2, limit+1)]
	P = []
	time = 0

	while True:
		prime = min(A)

		if prime > math.sqrt(limit):
			break

		P.append(prime)

		i = 0
		while i < len(A):
			if A[i] % prime == 0:
				A.pop(i)
				continue
			i += 1

	for a in A:
		P.append(a)

	return len(P)