scores = [1, 3, 6, 10, 15, 25]

teams = '''
Florida
Albany/MSM
Colorado
Pittsburgh
VCU
SF Austin
UCLA
Tulsa
Ohio St.
Dayton
Syracuse
W. Michigan
New Mexico
Stanford
Kansas
E. Kentucky

Virginia
Coastal Carolina
Memphis
George Washington
Cincinnati
Harvard
Michigan St.
Delaware
North Carolina
Providence
Iowa St.
N.C. Central
Connecticut
St. Joseph\'s
Villanova
Milwaukee

Arizona
Weber St.
Gonzaga
Oklahoma St.
Oklahoma
N. Dakota St.
San Diego St.
New Mexico St.
Baylor
Nebraska
Creighton
La-Lafayette
Oregon
BYU
Wisconsin
American

Wichita St.
Cal Poly/Texas So
Kentucky
Kansas St.
St. Louis
NC State/Xavier
Louisville
Manhattan
UMass
Iowa/Tennessee
Duke
Mercer
Texas
Arizona St.
Michigan
Wofford
'''
teams = [t.strip() for t in teams.split('\n') if t.strip()]
assert len(teams) == 64
width = len(max(teams, key=len))

predictions = {
    'Ali':      [[0, 1, 0, 0,  0, 0, 1, 0,   0, 1, 0, 0,  0, 0, 1, 0,
                  0, 1, 0, 0,  0, 0, 0, 0,   0, 1, 0, 0,  0, 0, 1, 0],
                 [0, 0, 1, 1,  0, 0, 0, 1,   0, 0, 1, 1,  0, 0, 1, 1],
                 [0, 1, 0, 1,  1, 1, 0, 1],
                 [1, 1, 1, 1],
                 [1, 0],
                 [1]],

    'Bailey':   [[0, 1, 0, 0,  1, 0, 0, 0,   0, 0, 0, 0,  1, 0, 1, 0,
                  0, 1, 1, 0,  0, 0, 0, 0,   0, 0, 1, 0,  0, 0, 0, 0],
                 [0, 1, 1, 1,  0, 1, 1, 1,   0, 1, 1, 1,  0, 1, 1, 1],
                 [0, 0, 1, 0,  0, 0, 1, 1],
                 [0, 1, 0, 0],
                 [0, 1],
                 [0]],

    'Bob':      [[0, 1, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  0, 0, 0, 0,
                  0, 1, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  1, 0, 0, 0],
                 [0, 1, 1, 1,  0, 1, 1, 1,   0, 1, 1, 1,  0, 1, 1, 1],
                 [0, 1, 1, 1,  0, 1, 1, 0],
                 [0, 0, 0, 0],
                 [0, 1],
                 [1]],

    'Bruce':    [[0, 1, 1, 0,  0, 0, 0, 0,   0, 1, 0, 0,  0, 0, 1, 0,
                  0, 1, 0, 1,  1, 0, 0, 0,   0, 0, 0, 0,  1, 0, 0, 0],
                 [0, 1, 0, 1,  0, 1, 1, 1,   0, 1, 0, 0,  0, 1, 1, 1],
                 [0, 0, 1, 0,  0, 1, 1, 1],
                 [0, 0, 1, 1],
                 [0, 0],
                 [1]],

    'Dave':     [[0, 1, 0, 0,  1, 0, 0, 0,   0, 1, 0, 0,  0, 0, 1, 0,
                  0, 0, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  1, 0, 1, 0],
                 [0, 0, 0, 1,  0, 1, 1, 0,   0, 0, 1, 0,  0, 1, 1, 1],
                 [0, 1, 1, 0,  0, 0, 1, 0],
                 [0, 1, 1, 0],
                 [0, 1],
                 [0]],

    'Drew':     [[0, 0, 0, 0,  0, 0, 0, 0,   0, 0, 1, 0,  1, 0, 0, 0,
                  0, 0, 1, 0,  0, 0, 0, 0,   0, 1, 1, 0,  0, 0, 1, 1],
                 [0, 1, 0, 1,  0, 1, 1, 1,   0, 1, 0, 0,  0, 1, 1, 0],
                 [0, 1, 0, 1,  0, 1, 0, 1],
                 [0, 0, 0, 0],
                 [0, 0],
                 [1]],

    'Erik':     [[0, 0, 1, 0,  1, 0, 0, 0,   0, 1, 0, 0,  0, 0, 0, 0,
                  0, 0, 0, 0,  1, 0, 0, 0,   0, 0, 0, 0,  0, 0, 0, 0],
                 [0, 1, 1, 1,  0, 0, 1, 1,   0, 0, 1, 1,  0, 1, 1, 1],
                 [0, 0, 0, 1,  0, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 1],
                 [1]],


    'Gary':     [[0, 1, 1, 0,  0, 1, 0, 0,   0, 0, 1, 0,  0, 0, 1, 0,
                  0, 0, 0, 0,  0, 0, 0, 0,   0, 0, 1, 0,  1, 0, 1, 0],
                 [0, 1, 0, 1,  1, 1, 1, 1,   0, 1, 0, 0, 1, 1, 1, 1],
                 [0, 0, 1, 1,  0, 0, 0, 1],
                 [0, 0, 0, 0],
                 [0, 1],
                 [1]],

    'Glassman': [[0, 1, 0, 0,  1, 0, 1, 0,   0, 1, 0, 0,  0, 0, 1, 0,
                  0, 1, 0, 0,  0, 0, 0, 0,   0, 1, 0, 0,  0, 0, 1, 0],
                 [0, 0, 1, 1,  0, 0, 1, 1,   0, 0, 1, 1,  0, 0, 1, 1],
                 [0, 1, 0, 0,  0, 1, 0, 0],
                 [1, 0, 1, 1],
                 [1, 1],
                 [0]],

    'Jeremy':   [[0, 1, 0, 0,  0, 0, 1, 0,   0, 1, 1, 0,  1, 0, 0, 0,
                  0, 1, 0, 0,  1, 0, 0, 0,   1, 0, 1, 0,  0, 0, 0, 0],
                 [0, 1, 0, 1,  0, 1, 1, 1,   1, 0, 0, 1,  1, 0, 0, 1],
                 [0, 1, 1, 0,  1, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 1],
                 [0]],

    'Jessica':  [[0, 1, 0, 0,  0, 0, 0, 0,   0, 0, 1, 0,  0, 0, 0, 0,
                  0, 1, 1, 0,  0, 0, 0, 0,   0, 0, 0, 0,  0, 0, 1, 0],
                 [0, 1, 0, 1,  0, 1, 0, 1,   0, 1, 1, 1,  0, 1, 1, 1],
                 [0, 1, 1, 1,  0, 1, 1, 1],
                 [0, 0, 0, 0],
                 [1, 1],
                 [0]],

    'Justin':   [[0, 1, 0, 0,  1, 0, 1, 0,   0, 0, 1, 0,  0, 0, 0, 0,
                  0, 1, 0, 0,  0, 0, 0, 0,   0, 1, 0, 1,  0, 0, 1, 0],
                 [0, 1, 1, 0,  0, 1, 1, 1,   0, 1, 1, 0,  0, 0, 1, 1],
                 [0, 0, 1, 0,  1, 1, 0, 1],
                 [0, 1, 0, 1],
                 [0, 1, ],
                 [0]],

    'Katie':    [[0, 1, 1, 0,  0, 1, 0, 0,   0, 0, 1, 0,  1, 0, 0, 0,
                  0, 1, 0, 0,  1, 0, 0, 0,   0, 1, 1, 0,  1, 0, 1, 0],
                 [0, 1, 0, 1,  0, 1, 1, 1,   0, 1, 1, 1,  0, 1, 1, 1],
                 [0, 1, 1, 0,  0, 1, 1, 1],
                 [0, 0, 0, 1],
                 [1, 0],
                 [0]],

    'Kaveh':    [[0, 1, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  0, 0, 0, 0,
                  0, 1, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  1, 0, 1, 0],
                 [0, 1, 1, 1,  0, 1, 0, 1,   0, 1, 1, 1,  0, 1, 1, 1],
                 [0, 1, 1, 0,  0, 1, 1, 1],
                 [0, 0, 0, 0],
                 [0, 1],
                 [0]],

    'Lobato':   [[0, 1, 0, 0,  1, 0, 0, 0,   0, 1, 0, 0,  0, 0, 1, 0,
                  0, 1, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  1, 0, 0, 0],
                 [0, 0, 0, 0,  0, 1, 0, 1,  0, 0, 0, 1,  0, 1, 1, 1],
                 [0, 1, 0, 1,  0, 0, 1, 0],
                 [0, 1, 0, 0],
                 [0, 0],
                 [1]],

    'Nate':     [[0, 1, 0, 0,  0, 0, 1, 0,   0, 1, 0, 0,  0, 0, 0, 0,
                  0, 0, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  0, 0, 1, 0],
                 [0, 0, 1, 1,  0, 1, 0, 1,   0, 0, 1, 1,  0, 1, 0, 1],
                 [0, 0, 1, 1,  0, 1, 1, 1],
                 [0, 0, 0, 0],
                 [0, 1],
                 [0]],

    'Snider':   [[0, 1, 1, 0,  1, 0, 0, 0,   0, 1, 1, 0,  0, 0, 0, 0,
                  0, 0, 1, 0,  0, 0, 0, 0,   0, 0, 0, 0,  0, 0, 0, 0],
                 [0, 0, 1, 0,  0, 0, 1, 1,   0, 1, 1, 1,  0, 1, 1, 1],
                 [0, 1, 0, 1,  0, 0, 1, 1],
                 [0, 1, 0, 0],
                 [0, 1],
                 [1]],

    'Tom':      [[0, 1, 0, 0,  0, 0, 1, 0,   0, 0, 0, 0,  0, 0, 0, 0,
                  0, 1, 0, 0,  0, 0, 0, 0,   0, 0, 0, 0,  0, 0, 1, 0],
                 [0, 1, 1, 1,  0, 1, 1, 1,   0, 1, 0, 0,  0, 1, 1, 1],
                 [0, 1, 0, 0,  0, 1, 1, 0],
                 [0, 1, 0, 0],
                 [0, 0],
                 [1]],
    }
p_width = len(max(predictions, key=len))


actual = [[0, 1, 1, 0,  1, 0, 1, 0,   0, 0, 1, 0,  0, 0, 0, 0,
           0, 0, 1, 0,  0, 0, 0, 0,   0, 0, 0, 0,  1, 1, 0, 0],
          [0, 1, 0, 0,  0, 1, 1, 0,   0, 1, 0, 1,  1, 1, 0, 1],
          [0, 0, 1, 1,  0, 1, 0, 1],
          [0, 1, 1, 0],
          [None, None],
          [None]]


for player in predictions:
    v = predictions[player]
    assert len(v) == 6
    assert [len(i) for i in v] == [32, 16, 8, 4, 2, 1]
    assert all(j in (0, 1) for i in v for j in i)


def make_tree(pred):
    prev = range(64)
    tree = [[None] * 2**i for i in range(6-1, -1, -1)]
    for col in range(len(pred)):
        for row in range(len(pred[col])):
            if pred[col][row] is None:
                tree[col][row] = None
            else:
                tree[col][row] = prev[2 * row + pred[col][row]]
        prev = tree[col]
    return tree


def print_player(player):
    if player == 'Actual':
        tree = make_tree(actual)
    else:
        tree = make_tree(predictions[player])
    print player
    for row in range(len(tree[0])):
        if not row % 8:
            print
        for col in range(6):
            team = tree[col][row / 2**col]
            if team is None:
                team = '???'
            else:
                team = teams[team]
            print '%-*s' % (width, team),
            if row & 2**col:
                break
        print
    print


def score_range(player, actual):
    p_tree = make_tree(predictions[player])
    a_tree = make_tree(actual)
    min_score = 0
    ns = len(scores)
    max_score = sum(2**(ns - i - 1) * scores[i] for i in range(ns))
    for col in range(len(p_tree)):
        for row in range(len(p_tree[col])):
            if p_tree[col][row] == a_tree[col][row]:
                min_score += scores[col]
            else:
                a = a_tree[col][row]
                if a is not None:
                    max_score -= scores[col]
                elif col:
                    contenders = p_tree[col - 1][2*row:2*row+2]
                    if None not in contenders and p_tree[col][row] not in contenders:
                        max_score -= scores[col]
    return (min_score, max_score)


def player_scores(actual):
    return [(p,) + score_range(p, actual) for p in predictions]


def show_scores(actual):
    for player in sorted(predictions, key=lambda p: score_range(p, actual)[0]):
        p_colon = player + ':'
        print '%-*s %3s %3s' % ((p_width + 1, p_colon) + score_range(player, actual))


def hypotheticals(a=actual):
    a = [col[:] for col in a]
    for i, col in enumerate(a):
        for j, row in enumerate(col):
            if row is None:
                for outcome in (0, 1):
                    a[i][j] = outcome
                    for hy in hypotheticals(a):
                        yield hy
                return
    yield a



# Example: check that actual data is entered correctly.
# print_player('Actual')


show_scores(actual)
print

print 'Possible Outcomes'
for hy in hypotheticals():
    h_tree = make_tree(hy)
    winner = h_tree[5][0]
    runner_up = [t for t in h_tree[4] if t != winner][0]
    print '%s beats %s' % (teams[winner], teams[runner_up])
    for (player, score, junk) in sorted(player_scores(hy), key=lambda ps: -ps[1])[:3]:
        p_colon = player + ':'
        print '%-*s %3s' % (p_width + 1, p_colon, score)
    print
