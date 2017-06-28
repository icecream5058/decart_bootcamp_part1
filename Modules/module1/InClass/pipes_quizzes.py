from nose.tools import assert_equal

def oct_17(answer=-1):
    try:
        assert_equal( 6, answer)
        print('number of Oct. 17 identified correctly.')
    except:
        print('number of Oct. 17 NOT identified correctly.')

def concepts(answer=-1):
    try:
        assert_equal(526703, answer)
        print('number of concepts identified correctly.')
    except:
        print('number of concepts NOT identified correctly.')

def relationships(answer=-1):
    try:
        assert_equal( 7043, answer)
        print('number of relationships identified correctly.')
    except:
        print('number of relationships NOT identified correctly.')


