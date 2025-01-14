score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num' : 5})
print('В команде Волшебники данных участников: %(team1_num)s!' % {'team1_num' : 6})
print('Итого сегодня в командах участников: %(team1_num)s и %(team_num2)s!' % {'team1_num': 5, 'team_num2': 6})
print('Команда Мастера кода решила задач: {score_1}!'.format(score_1 = 40))
print('Команда Волшебники данных решила задач: {score_2}!'.format(score_2 = 42))
print('Мастера кода решили задачи за {team1_time}с!'.format(team1_time = 1552.512))
print('Мастера кода решили задачи за {team2_time}с!'.format(team2_time = 2153.31451))
print(f'Команды решили {score_1} и {score_2} задач.')

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники данных!'
    else:
        return 'Ничья!'

challenge_result = challenge_result()
print(f'Результат битвы: {challenge_result}')

def tasks_total():
    return score_1 + score_2

def time_avg():
    tasks_total = score_1 + score_2
    return round((team1_time + team2_time) / tasks_total, 1)

tasks_total = tasks_total()
time_avg = time_avg()

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')