#Personal Budget Manager:


print('='*30)
print('Personal Budget Manager')
print('='*30)


Budget = []
Spending = []
Total_Income = 0
print(
      '1. Total Income\n',
      '2. Budget Allocation\n',
      '3. View History\n',
      '4. Budget Tracker\n',
      '5. Savings\n',
      '6. Exit\n')


def Bud():
    while True:
        Choice = input('\nEnter the selection (1-6) or type exit:')
        
        if Choice == 'exit' or Choice == '6':
            print("Thank you!")
            break

        elif Choice == '1':
            Total_Income = int(input('\nEnter the Total Income per Month:'))
            print(Total_Income)


        elif Choice == '2':
            item = input('\nEnter the Expense Name: ')
            amount = float(input('\nEnter the Amount: '))
            
            Budget_dict = {'item': item, 'amount': amount}
            Budget.append(Budget_dict)
            
            print('Budget Allocation is successful!!!')
            
            
        elif Choice == '3':
            print('\nOverall Budget:',(Budget))

            if not Budget:
                print('No budget allocated yet.')

            else:
                for B in Budget:
                    print(B['item'], ':', B['amount'])

                print('Total Budget:', sum(B['amount'] for B in Budget))

                

        elif Choice == '4':
            item = input('\nEnter the Expense Name: ')
            
            
            if not any(B['item'] == item for B in Budget):
                print('No budget found for this expense.')
                
            else:
                
                amount = float(input('Enter the Amount: '))
                Spending_dict = {'item': item, 'amount': amount}
                Spending.append(Spending_dict)

                Budget_Amount = sum(B['amount'] for B in Budget if B['item'] == item )

                Spending_Amount = sum(S['amount'] for S in Spending if S['item'] == item )


                Remaining = Budget_Amount - Spending_Amount

                if Spending_Amount <= Budget_Amount:
                    print('Spending is within the limit.')
                    print('Remaining Budget:', Remaining)

                else:
                    print('Warning: Budget Exceeded!')
                    print('Exceeded Amount:', abs(Remaining))
                    

        elif Choice == '5':
            print('\nSPENDING SUMMARY')

            if not Spending:
                print('No spending recorded yet.')

            else:
                for S in Spending:
                    print(S['item'], ':', S['amount'])
                print('Total Spending:', sum(S['amount'] for S in Spending))

        else:
            print('Please enter a valid selection.')

Bud()
                
            

      
