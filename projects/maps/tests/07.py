test = {
  'name': 'Problem 7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a9bfecde83c364e5016f8ac70d28a8b4',
          'choices': [
            r"""
            takes in a restaurant and returns the predicted rating for that
            restaurant
            """,
            r"""
            takes in a restaurant and returns the predicted location of
            that restaurant
            """,
            'returns the r_squared value'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What does a predictor function returned by
          find_predictor do?
          """
        },
        {
          'answer': '1120a82876dd18c5c5bce8094b70f402',
          'choices': [
            'the restaurants in restaurants',
            'the names of restaurants in restaurants',
            'the extracted feature value for each restaurant in restaurants',
            'the restaurants reviewed by user'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the list xs in the body of find_predictor represent?'
        },
        {
          'answer': 'bd3d200adeeb6d968d5129c42ce2db73',
          'choices': [
            'the average rating for the restaurants in restaurants',
            "user's ratings for the restaurants in restaurants",
            'the names for the restaurants reviewed by user',
            'the names for the restaurants in restaurants'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the list ys in the body of find_predictor represent?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('John D.', [
          ...     make_review('A', 1),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 2.5),
          ... ])
          >>> restaurant = make_restaurant('New', [-10, 2], [], 2, [
          ...         make_review('New', 4),
          ... ])
          >>> cluster = [
          ...     make_restaurant('B', [4, 2], [], 1, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3),
          ...     ]),
          ... ]
          >>> pred, r_squared = find_predictor(user, cluster, restaurant_price)
          >>> round(pred(restaurant), 5)
          4.0
          >>> round(r_squared, 5)
          1.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('John D.', [
          ...     make_review('A', 1),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 2.5),
          ... ])
          >>> restaurant = make_restaurant('New', [-10, 2], [], 2, [
          ...         make_review('New', 4),
          ... ])
          >>> cluster = [
          ...     make_restaurant('B', [4, 2], [], 1, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3),
          ...     ]),
          ... ]
          >>> pred, r_squared = find_predictor(user, cluster, lambda r: mean(restaurant_ratings(r)))
          >>> round(pred(restaurant), 5)
          3.9359
          >>> round(r_squared, 5)
          0.99256
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('John D.', [
          ...     make_review('A', 1),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 2.5),
          ... ])
          >>> restaurant = make_restaurant('New', [-10, 2], [], 2, [
          ...         make_review('New', 4),
          ... ])
          >>> cluster = [
          ...     make_restaurant('B', [4, 2], [], 1, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3),
          ...     ]),
          ... ]
          >>> pred, r_squared = find_predictor(user, cluster, lambda r: len(restaurant_ratings(r)))
          >>> round(pred(restaurant), 5)
          3.5
          >>> round(r_squared, 5)
          0.12903
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> test.swap_implementations(recommend)
      >>> from recommend import *
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
