import numpy as np

payschedule = []	

def loanbymth(financeamount,interest_perannum,tenor):
	intsallment = np.pmt(interest_perannum/12,tenor,-financeamount)
	for i in range(tenor+1):
		if i == 0: 
			accuprincpay = round(float(financeamount),6)
			payschedule.append(['Period,PrincPay,InterestPay,Installment,PrincipleBalance,Eir'])
			payschedule.append([i,0 ,0 ,0 , financeamount,interest_perannum/12])
		else:
			pp = np.ppmt(interest_perannum/12,i,tenor,-financeamount)
			ip = np.ipmt(interest_perannum/12,i,tenor,-financeamount)
			accuprincpay = round(accuprincpay - pp,6)
			payschedule.append([i,pp,ip*1,intsallment,accuprincpay,interest_perannum/12 ])
	return payschedule
	
if __name__ == '__main__':
	loanamt = 10000
	annualinterest_flat = 0.15
	loantenor = 60
	print('Program parameter Principle {} annum interest {}, month {}'.format(loanamt,annualinterest_flat,loantenor))
	print('-------------------------------------')
	paysch = loanbymth(loanamt,annualinterest_flat,loantenor)
	for py in paysch:
		print(py)