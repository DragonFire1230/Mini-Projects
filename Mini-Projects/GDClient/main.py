print('GD Client by DragonFire')
import gd
print('Loaded GD')
import json
print('Loaded JSON')

try:
	with open('account.json') as accjson:
		accjson = json.load(accjson)
except FileNotFoundError:
    print('Critical Error Occured. Error: File "settings.json" not found')
    input('Press Enter to continue')
except PermissionError:
    print('Critical Error Occured. Error: Not permissions to view "settings.json"')
    input('Press Enter to continue')

client = gd.Client()

async def clientC():
	usernameAcc = accjson['usernameAcc']
	passwordAcc = accjson['passwordAcc']
	print()
	print('Trying login...')
	try:
		await client.login(usernameAcc, passwordAcc)
	except gd.errors.LoginFailure:
		print('Error occured: Uncorrect username or password')
		input('Press Enter to continue')
		sys.exit(0)

	print('Done')

	while True:
		print()
		command = input(f'{usernameAcc}> ')
		if command == 'help':
			print('getID        | Get you account and player id')
			print('daily        | Current daily')
			print('weekly       | Current weekly')
			print('friends      | You friends')
			print('commentLevel | Comment level')
		if command == 'getID':
			user = await client.search_user(usernameAcc)
			print(f'Your AccountID: {user.account_id}')
			print(f'Your PlayerID: {user.id}')

		if command == 'daily':
			daily = await client.get_daily()
			print(f"Current daily: {daily}")

		if command == 'weekly':
			weekly = await client.get_weekly()
			print(f"Current weekly: {weekly}")

		if command == 'friends':
			friends = await client.get_friends()
			if not friends:
				print("You don't have a friends")
			else:
				print(friends)

		if command == 'commentLevel':
			levelToCommentID = int(input('Level to comment ID> '))
			commentToLevel = input('Comment> ')
			level = await client.get_level(levelToCommentID)
			await level.comment(commentToLevel)
			print('Done')

		if command == 'exit': exit()

client.run(clientC())