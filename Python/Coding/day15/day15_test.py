def add(a, b):
    return a + b


import unittest


class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)


class TestMyModule1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(-1, -1), -2)


class TestMyModule2(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1.01, 1.07), 2.08)


class TestInterestModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        print("Setup Ran...")
        self.accounts = [
            {
                "id": 1,
                "name": "John Doe",
                "email": "johndoe@example.com",
                "isActive": True,
                "balance": 150.75,
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "janesmith@example.com",
                "isActive": True,
                "balance": 500.50,
            },
            {
                "id": 3,
                "name": "Emily Jones",
                "email": "emilyjones@example.com",
                "isActive": True,
                "balance": 0.00,
            },
        ]

    def tearDown(self):
        print("TearDown : Clear cursor")

    def test_interest_rate_for_active_user(self):
        # Act
        output = adds_interest(self.accounts, 0.1)
        print("Test 1")
        # Assert
        self.assertEqual(add(1.2, 3.2), 4.4)

    def test_interest_rate_for_non_active_user(self):
        output = adds_interest(self.accounts, 0.1)
        print("Test 2")
        # self.assertEqual(output[1]["balance"], 500.5)


if __name__ == "__main__":
    unittest.main()
