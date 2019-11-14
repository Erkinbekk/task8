def choice_to_number(choice):
    if choice == 'Usain':
        return 1
    elif choice == 'Nelin':
        return 2
    elif choice == 'Aybek':
        return 3

def number_to_choice(number):
    if number == 1:
        return 'Usain'
    elif number == 2:
        return 'Nelin'
    elif number == 3:
        return 'Aybek'

def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Nelin') == 2
    assert choice_to_number('Aybek') == 3

def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Nelin'
    assert number_to_choice(3) == 'Aybek'

def test_all():
  try:
    test_choice_to_number()
    test_number_to_choice()

  except AssertionError:
    print('WRONG')
  else:
    print('SUCCESS')

test_all()