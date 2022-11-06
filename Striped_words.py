#Given text with different words and/or numbers, separated by spaces and punctuation marks. Numbers do not count
# as words (as well as a mixture of letters and numbers). It is necessary to count words in which vowels alternate
# with consonants (striped words), that is, such words do not have two vowels or two consonants in a row.
# Single-letter words are not "striped" (don't count them). Letter case does not matter.
import re


def Striped_Words():

    Consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
                  'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    Vowels = ['a', 'e', 'i', 'o', 'u', 'y',
              'A', 'E', 'I', 'O', 'U', 'Y']

    Sum_of_words = 0
    Boolean_Label = False

    print('\nExercise 5 - Striped Words')
    print('Enter text')
    Text = input()

    Text = re.split('[., ]+', Text)

    if '' in Text:
        Text.remove('')


    #Перебор всех слов в тексте
    for Words in range(len(Text)):

        if Words == None:
            break


        #Преобразование слова в список
        Words_to_List = list(Text[Words])
        print(Words_to_List)

        #Если длина слова - нечетная
        if len(Words_to_List) == 1:
            continue

        #Условие для слов нечетной длины
        elif len(Words_to_List) % 2 != 0:

            #Просмотр каждой буквы в слове
            for Letters in range(0, len(Words_to_List) - 1):

                #Проверка содержится ли буква в согласных
                if Words_to_List[Letters] in Consonants:

                    Boolean_Label = True

                    #Проверка следующей буквы на гласную
                    if Words_to_List[Letters + 1] in Vowels:

                        Boolean_Label = True

                    else:

                        Boolean_Label = False
                        break


                #Если буква не согласная
                elif Words_to_List[Letters] in Vowels:

                    Boolean_Label = True

                    #Если следующая после гласной - согласная
                    if Words_to_List[Letters + 1] in Consonants:

                        Boolean_Label = True


                    #Если после гласного не идет согласная - записываем false - идем дальше
                    else:

                        Boolean_Label = False
                        break




                else:
                    continue

            #Если выполнились все условия, прибавляем к счетчику единицу
            if Boolean_Label == True:
                Sum_of_words += 1

        #Проверяем дальше если длина слова - четная
        else:
            if len(Words_to_List) % 2 == 0:

                # Просмотр каждой буквы в слове
                for Letters in range(0, len(Words_to_List) - 1):

                    # Проверка содержится ли буква в согласных
                    if Words_to_List[Letters] in Consonants:

                        Boolean_Label = True

                        # Проверка следующей буквы на гласную
                        if Words_to_List[Letters + 1] in Vowels:

                            Boolean_Label = True


                        else:

                            Boolean_Label = False
                            break


                    # Если первая буква не согласная
                    elif Words_to_List[Letters] in Vowels:

                        Boolean_Label = True


                        #Если следующая после гласной - согласная
                        if Words_to_List[Letters + 1] in Consonants:

                            Boolean_Label = True

                            # Если после главное не идет согласная - записываем false - идем дальше
                        else:

                            Boolean_Label = False
                            break

                    else:
                        continue

                if Boolean_Label == True:
                    Sum_of_words += 1
                    print('Сумма = ', Sum_of_words)

    print(Sum_of_words)



Striped_Words()