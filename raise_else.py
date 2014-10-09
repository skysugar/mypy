def f(n):
	try:
		for i in range(1,6):
			if i == n:
				raise
			else:
				print(i)
	except RuntimeError:
		print(i,"raise ok")
	else:
		print("-"*20) 				#如果没有错误会执行这里，有就不执行了
	finally:
		print("app run over .") 	#try执行完毕会执行这里

f(5)
print('='*5+"cut"+'='*5)
f(11)