# 課題3.【プログラミング】
# ②-1素因数分解を再帰的に行う関数を作成せよ。

#coding:utf-8

file_name = "file.txt"

f = open(file)
reader = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ

for line in lines2:
	print line,
print







def get_prime_number (num):
	"""Summary line.
	エラトステネスの篩アルゴリズムを使い、素因数分解を行う
	Args:
		num (int): 素因数分解を行う数値
	Returns:
		list: 素因数分解された素数
	"""

	if not str(num).isdigit() or num < 2:
		#自然数かつ1以上の数値を判定
		return print('１より大きい自然数を入力してください')

	sequence_list = [i for i in range (2, num+1)]
	#2から入力値までの数列のリスト
	prime_list = []
	#素数のリスト

	while True:
		prime = min(sequence_list)

		if prime > math.sqrt(num):
			#入力値の平方根以上は全てリストに加えて終了
			prime_list.extend(sequence_list)
			break
		else:
			prime_list.append(prime)

		i = 0
		while i < len(sequence_list):
			if sequence_list[i] % prime == 0:
				#素数の倍数をリストから削除
				sequence_list.pop(i)
				continue
			i += 1

	return prime_list

num = 12
ans = get_prime_number(num)
print(ans)