
def main():
    v = 'one'
    if v == 'one':
        print('v is {}'.format(v))
    elif v == 'two':
        print('v is two')
    else:
        print('v is some other number')

    choices = dict(
           one = 'one',
           two = 'two',
           three = 'three',
           four = 'four'
            )
    x = 'one'
    y = 'seven'
    print(choices[x])
    # set default with get method
    print(choices.get(y, 'other'))

    t = "right" if 0 < 1 else "wrong"
    print(t)


    for key,value in enumerate(choices):
        print(key,value.value)

    
if __name__=="__main__":main()
