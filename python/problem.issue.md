一些有意思的python问题
===

获得所有参数组合
---

例如有一个url支持的key, value参数你有一个列表，你想生成所有的参数对儿


    # -*- coding: utf-8 -*-
    '''
        d = {
            'd1': [1, 2, 3]
            'd2': ['a', 'b']
            ...
            'dn': ['w1', 'w2', 'w3', 'w4']
        }
        -->

        [
            {
                'd1': 1, 'd2': 'a', ..., 'dn': 'w1',
            },
            {
                'd1': 1, 'd2': 'a', ..., 'dn': 'w2',
            }
            {
                'd1': 1, 'd2': 'a', ..., 'dn': 'w3',
            }
            ...
            {
                'd1': 1, 'd2': 'b', ..., 'dn': 'w1',
            },
            {
                'd1': 1, 'd2': 'b', ..., 'dn': 'w2',
            }
            {
                'd1': 1, 'd2': 'b', ..., 'dn': 'w3',
            }
            ...
            {
                'd1': 2, 'd2': 'a', ..., 'dn': 'w1',
            },
            {
                'd1': 2, 'd2': 'a', ..., 'dn': 'w2',
            }
            {
                'd1': 2, 'd2': 'a', ..., 'dn': 'w3',
            }
        ]
    '''
    from itertools import product

    def genarate_value(prefix, n):
        return ['{}{}'.format(prefix, i) for i in xrange(n)]

    d = {
        'd1': genarate_value('a', 4),
        'd2': genarate_value('b', 3),
        'd3': genarate_value('c', 6),
    }

    def _izip(key, values):
        '''
        key: [value1, value2, ...]
        -->
            (key, value1), (key, value2)
        '''
        return [(key, value) for value in values]


    def alot_params(params):
        return product(*(_izip(key, values) for key, values in params.iteritems()))

    result = [dict(each) for each in alot_params(d)]
    print result

