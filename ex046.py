from time import sleep
import emoji


print('Prepare-se, os fogos vão começar!')
sleep(3)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BOOMMMMM!!! :boom: :boom: :boom: :boom: :boom:', use_aliases=True))
